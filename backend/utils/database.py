from pymongo import MongoClient
from config import Config

class DatabaseManager:
    def __init__(self):
        self.client = MongoClient(Config.MONGODB_URI)
        self.db = self.client.movie_recommender
        self.users = self.db.users
    
    def create_user(self, email, password):
        """Create a new user in the database."""
        # Check if user already exists
        if self.users.find_one({'email': email}):
            return None, "User already exists"
        
        # Hash the password
        from utils.auth import AuthManager
        auth_manager = AuthManager()
        hashed_password = auth_manager.hash_password(password)
        
        # Create user document
        user_doc = {
            'email': email,
            'password': hashed_password,
            'created_at': datetime.utcnow()
        }
        
        try:
            result = self.users.insert_one(user_doc)
            return str(result.inserted_id), None
        except Exception as e:
            return None, str(e)
    
    def authenticate_user(self, email, password):
        """Authenticate a user and return user ID if successful."""
        user = self.users.find_one({'email': email})
        if not user:
            return None, "User not found"
        
        from utils.auth import AuthManager
        auth_manager = AuthManager()
        
        if auth_manager.verify_password(password, user['password']):
            return str(user['_id']), None
        else:
            return None, "Invalid password"
    
    def get_user_by_id(self, user_id):
        """Get user by ID."""
        from bson import ObjectId
        try:
            return self.users.find_one({'_id': ObjectId(user_id)})
        except:
            return None

# Import datetime for the database operations
from datetime import datetime

