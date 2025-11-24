import requests
from config import Config

class TMDBClient:
    def __init__(self):
        self.api_key = Config.TMDB_API_KEY
        self.base_url = "https://api.themoviedb.org/3"
        self.image_base_url = "https://image.tmdb.org/t/p/w500"
    
    def search_movie(self, movie_title):
        """Search for a movie by title and return TMDB data."""
        url = f"{self.base_url}/search/movie"
        params = {
            'api_key': self.api_key,
            'query': movie_title,
            'language': 'en-US',
            'page': 1
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            
            if data['results']:
                movie = data['results'][0]
                return {
                    'id': movie['id'],
                    'title': movie['title'],
                    'poster_path': f"{self.image_base_url}{movie['poster_path']}" if movie['poster_path'] else None,
                    'overview': movie['overview'],
                    'release_date': movie['release_date'],
                    'vote_average': movie['vote_average']
                }
            return None
        except Exception as e:
            print(f"Error searching movie: {e}")
            return None
    
    def get_movie_poster(self, movie_title):
        """Get movie poster URL by title."""
        movie_data = self.search_movie(movie_title)
        return movie_data['poster_path'] if movie_data else None
    
    def get_trending_movies(self, limit=20):
        """Get trending movies from TMDB."""
        url = f"{self.base_url}/trending/movie/week"
        params = {
            'api_key': self.api_key,
            'language': 'en-US',
            'page': 1
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            
            movies = []
            for movie in data['results'][:limit]:
                movies.append({
                    'id': movie['id'],
                    'title': movie['title'],
                    'poster_path': f"{self.image_base_url}{movie['poster_path']}" if movie['poster_path'] else None,
                    'overview': movie['overview'],
                    'release_date': movie['release_date'],
                    'vote_average': movie['vote_average']
                })
            
            return movies
        except Exception as e:
            print(f"Error getting trending movies: {e}")
            return []
    
    def get_movie_details(self, movie_id):
        """Get detailed movie information by TMDB ID."""
        url = f"{self.base_url}/movie/{movie_id}"
        params = {
            'api_key': self.api_key,
            'language': 'en-US'
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            
            return {
                'id': data['id'],
                'title': data['title'],
                'poster_path': f"{self.image_base_url}{data['poster_path']}" if data['poster_path'] else None,
                'overview': data['overview'],
                'release_date': data['release_date'],
                'vote_average': data['vote_average'],
                'runtime': data['runtime'],
                'genres': [genre['name'] for genre in data['genres']]
            }
        except Exception as e:
            print(f"Error getting movie details: {e}")
            return None
    
    def get_similar_movies(self, movie_id):
        """Get similar movies from TMDB."""
        url = f"{self.base_url}/movie/{movie_id}/similar"
        params = {
            'api_key': self.api_key,
            'language': 'en-US',
            'page': 1
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            
            movies = []
            for movie in data['results'][:5]:  # Limit to 5 movies
                movies.append({
                    'id': movie['id'],
                    'title': movie['title'],
                    'poster_path': f"{self.image_base_url}{movie['poster_path']}" if movie['poster_path'] else None,
                    'overview': movie['overview'],
                    'release_date': movie['release_date'],
                    'vote_average': movie['vote_average']
                })
            
            return movies
        except Exception as e:
            print(f"Error getting similar movies: {e}")
            return []

