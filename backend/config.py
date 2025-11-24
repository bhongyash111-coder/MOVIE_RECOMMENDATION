import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    TMDB_API_KEY = "8265bd1679663a7ea12ac168da84d2e8"
    MONGODB_URI = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/movie_recommender')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'your-secret-key-change-this-in-production')
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')

