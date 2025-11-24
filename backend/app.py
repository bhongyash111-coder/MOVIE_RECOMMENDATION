from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from utils.recommend import MovieRecommender
from utils.tmdb_client import TMDBClient
from utils.database import DatabaseManager
from utils.auth import AuthManager
from functools import wraps

app = Flask(__name__)
CORS(app)

# Initialize components
recommender = MovieRecommender('movies.pkl', 'similarity.pkl')
tmdb_client = TMDBClient()
db_manager = DatabaseManager()
auth_manager = AuthManager()

def token_required(f):
    """Decorator to require JWT token for protected routes."""
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing'}), 401
        
        try:
            if token.startswith('Bearer '):
                token = token[7:]  # Remove 'Bearer ' prefix
            
            user_id = auth_manager.verify_token(token)
            if user_id is None:
                return jsonify({'message': 'Token is invalid'}), 401
            
            return f(user_id, *args, **kwargs)
        except Exception as e:
            return jsonify({'message': 'Token is invalid'}), 401
    
    return decorated

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({'status': 'healthy', 'message': 'Movie Recommendation API is running'})

@app.route('/api/register', methods=['POST'])
def register():
    """Register a new user."""
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        
        if not email or not password:
            return jsonify({'message': 'Email and password are required'}), 400
        
        user_id, error = db_manager.create_user(email, password)
        if error:
            return jsonify({'message': error}), 400
        
        token = auth_manager.generate_token(user_id)
        return jsonify({
            'message': 'User created successfully',
            'token': token,
            'user_id': user_id
        }), 201
        
    except Exception as e:
        return jsonify({'message': 'Registration failed'}), 500

@app.route('/api/login', methods=['POST'])
def login():
    """Login a user."""
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        
        if not email or not password:
            return jsonify({'message': 'Email and password are required'}), 400
        
        user_id, error = db_manager.authenticate_user(email, password)
        if error:
            return jsonify({'message': error}), 401
        
        token = auth_manager.generate_token(user_id)
        return jsonify({
            'message': 'Login successful',
            'token': token,
            'user_id': user_id
        }), 200
        
    except Exception as e:
        return jsonify({'message': 'Login failed'}), 500

@app.route('/api/trending', methods=['GET'])
def get_trending_movies():
    """Get popular movies from our dataset with TMDB data."""
    try:
        limit = request.args.get('limit', 20, type=int)
        
        # Get movies from our dataset
        all_movies = recommender.get_all_movies()
        
        # Select a random sample of popular movies
        import random
        sample_movies = random.sample(all_movies, min(limit, len(all_movies)))
        
        # Get TMDB data for each movie
        movies_with_data = []
        for movie_title in sample_movies:
            movie_data = tmdb_client.search_movie(movie_title)
            if movie_data:
                movies_with_data.append(movie_data)
                if len(movies_with_data) >= limit:
                    break
        
        return jsonify({'movies': movies_with_data}), 200
    except Exception as e:
        return jsonify({'message': 'Failed to fetch trending movies'}), 500

@app.route('/api/popular', methods=['GET'])
def get_popular_movies():
    """Get popular movies from our dataset."""
    try:
        limit = request.args.get('limit', 20, type=int)
        
        # Get movies from our dataset
        all_movies = recommender.get_all_movies()
        
        # Select a random sample
        import random
        sample_movies = random.sample(all_movies, min(limit, len(all_movies)))
        
        return jsonify({'movies': sample_movies}), 200
    except Exception as e:
        return jsonify({'message': 'Failed to fetch popular movies'}), 500

@app.route('/api/recommend', methods=['POST'])
def recommend_movies():
    """Get movie recommendations for a given movie."""
    try:
        data = request.get_json()
        movie_title = data.get('movie_title')
        
        if not movie_title:
            return jsonify({'message': 'Movie title is required'}), 400
        
        # Get recommendations from our model
        recommended_titles = recommender.recommend_movies(movie_title, top_n=5)
        
        if not recommended_titles:
            return jsonify({'message': 'Movie not found or no recommendations available'}), 404
        
        # Get TMDB data for each recommended movie
        recommended_movies = []
        for title in recommended_titles:
            movie_data = tmdb_client.search_movie(title)
            if movie_data:
                recommended_movies.append(movie_data)
        
        return jsonify({
            'original_movie': movie_title,
            'recommendations': recommended_movies
        }), 200
        
    except Exception as e:
        return jsonify({'message': 'Failed to get recommendations'}), 500

@app.route('/api/recommend-any', methods=['POST'])
def recommend_any_movie():
    """Get recommendations for any movie, even if not in our dataset."""
    try:
        data = request.get_json()
        movie_title = data.get('movie_title')
        
        if not movie_title:
            return jsonify({'message': 'Movie title is required'}), 400
        
        # First try to get recommendations from our model
        recommended_titles = recommender.recommend_movies(movie_title, top_n=5)
        
        if not recommended_titles:
            # If movie not found in our dataset, get similar movies from TMDB
            tmdb_movie = tmdb_client.search_movie(movie_title)
            if not tmdb_movie:
                return jsonify({'message': 'Movie not found'}), 404
            
            # Get similar movies from TMDB
            similar_movies = tmdb_client.get_similar_movies(tmdb_movie['id'])
            recommended_movies = similar_movies[:5]
            
            return jsonify({
                'original_movie': movie_title,
                'recommendations': recommended_movies,
                'source': 'tmdb'
            }), 200
        
        # Get TMDB data for each recommended movie
        recommended_movies = []
        for title in recommended_titles:
            movie_data = tmdb_client.search_movie(title)
            if movie_data:
                recommended_movies.append(movie_data)
        
        return jsonify({
            'original_movie': movie_title,
            'recommendations': recommended_movies,
            'source': 'dataset'
        }), 200
        
    except Exception as e:
        return jsonify({'message': 'Failed to get recommendations'}), 500

@app.route('/api/search', methods=['GET'])
def search_movies():
    """Search for movies by title."""
    try:
        query = request.args.get('q', '')
        if not query:
            return jsonify({'message': 'Search query is required'}), 400
        
        # Search in our local database first
        local_results = recommender.search_movies(query)
        
        # Also search TMDB for more comprehensive results
        tmdb_results = []
        for title in local_results[:5]:  # Limit to first 5 local results
            movie_data = tmdb_client.search_movie(title)
            if movie_data:
                tmdb_results.append(movie_data)
        
        return jsonify({
            'query': query,
            'results': tmdb_results
        }), 200
        
    except Exception as e:
        return jsonify({'message': 'Search failed'}), 500

@app.route('/api/movies', methods=['GET'])
def get_all_movies():
    """Get all available movies from our dataset."""
    try:
        movies = recommender.get_all_movies()
        return jsonify({'movies': movies}), 200
    except Exception as e:
        return jsonify({'message': 'Failed to fetch movies'}), 500

@app.route('/api/movie/<movie_title>', methods=['GET'])
def get_movie_details(movie_title):
    """Get detailed information about a specific movie."""
    try:
        movie_data = tmdb_client.search_movie(movie_title)
        if not movie_data:
            return jsonify({'message': 'Movie not found'}), 404
        
        return jsonify({'movie': movie_data}), 200
    except Exception as e:
        return jsonify({'message': 'Failed to fetch movie details'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

