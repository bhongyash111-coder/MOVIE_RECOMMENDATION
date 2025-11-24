import pickle
import pandas as pd
import numpy as np

class MovieRecommender:
    def __init__(self, movies_path='movies.pkl', similarity_path='similarity.pkl'):
        """Initialize the movie recommender with pre-trained data."""
        self.movies = pickle.load(open(movies_path, 'rb'))
        self.similarity = pickle.load(open(similarity_path, 'rb'))
    
    def recommend_movies(self, movie_name, top_n=5):
        """
        Get movie recommendations based on a given movie name.
        
        Args:
            movie_name (str): Name of the movie to find recommendations for
            top_n (int): Number of recommendations to return
            
        Returns:
            list: List of recommended movie titles
        """
        try:
            # Find the movie index
            movie_index = self.movies[self.movies['title'] == movie_name].index
            
            if len(movie_index) == 0:
                return []
            
            movie_index = movie_index[0]
            
            # Get similarity scores
            distances = self.similarity[movie_index]
            
            # Get top similar movies (excluding the movie itself)
            movies_list = sorted(
                list(enumerate(distances)), 
                reverse=True, 
                key=lambda x: x[1]
            )[1:top_n+1]
            
            # Extract movie titles
            recommended_movies = []
            for i in movies_list:
                recommended_movies.append(self.movies.iloc[i[0]]['title'])
            
            return recommended_movies
            
        except Exception as e:
            print(f"Error in recommendation: {e}")
            return []
    
    def get_all_movies(self):
        """Get all available movie titles."""
        return self.movies['title'].tolist()
    
    def search_movies(self, query):
        """Search for movies by title (case-insensitive)."""
        query = query.lower()
        return self.movies[
            self.movies['title'].str.lower().str.contains(query)
        ]['title'].tolist()

