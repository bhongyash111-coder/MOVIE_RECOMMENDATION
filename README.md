# 🎬 Movie Recommendation System

A full-stack movie recommendation application built with Flask (backend) and React (frontend). Get personalized movie recommendations based on content similarity using machine learning.

## ✨ Features

- 🎯 **Smart Recommendations**: Get movie suggestions based on content similarity
- 🔍 **Search Functionality**: Search for movies in our extensive database
- 📊 **Trending Movies**: Browse popular and trending movies
- 🎨 **Modern UI**: Beautiful, responsive interface built with React and Tailwind CSS
- 🔐 **User Authentication**: Register and login (optional for recommendations)

## 🚀 Tech Stack

### Backend
- **Flask**: Python web framework
- **Scikit-learn**: Machine learning for recommendations
- **Pandas & NumPy**: Data processing
- **MongoDB**: User data storage
- **JWT**: Authentication tokens
- **TMDB API**: Movie metadata and posters

### Frontend
- **React**: UI framework
- **React Router**: Navigation
- **Axios**: HTTP client
- **Tailwind CSS**: Styling

## 📦 Installation

### Prerequisites
- Python 3.8+
- Node.js 14+
- Git LFS (for large files)

### Backend Setup

1. Navigate to backend directory:
```bash
cd backend
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file (optional):
```env
MONGODB_URI=your_mongodb_connection_string
JWT_SECRET_KEY=your_secret_key
```

4. Run the backend server:
```bash
python app.py
```

Backend will run on `http://localhost:5000`

### Frontend Setup

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm start
```

Frontend will run on `http://localhost:3000`

## 🌐 Deployment

### Using Railway (Recommended)

Both backend and frontend have `railway.toml` configuration files ready for deployment.

1. Install Railway CLI:
```bash
npm install -g @railway/cli
```

2. Login to Railway:
```bash
railway login
```

3. Deploy backend:
```bash
cd backend
railway up
```

4. Deploy frontend:
```bash
cd frontend
railway up
```

### Using Vercel (Frontend)

```bash
cd frontend
npm install -g vercel
vercel
```

### Using Netlify (Frontend)

```bash
cd frontend
npm run build
# Drag and drop the 'build' folder to Netlify
```

## 📁 Project Structure

```
MOVIE_RECOMMENDATIONs/
├── backend/
│   ├── app.py                 # Main Flask application
│   ├── config.py              # Configuration settings
│   ├── requirements.txt       # Python dependencies
│   ├── movies.pkl            # Movie dataset (Git LFS)
│   ├── similarity.pkl        # Similarity matrix (Git LFS)
│   ├── utils/
│   │   ├── recommend.py      # Recommendation engine
│   │   ├── tmdb_client.py    # TMDB API client
│   │   ├── database.py       # Database operations
│   │   └── auth.py           # Authentication logic
│   └── railway.toml          # Railway deployment config
│
├── frontend/
│   ├── build/                # Production build
│   ├── public/               # Static assets
│   ├── package.json          # Node dependencies
│   ├── tailwind.config.js    # Tailwind configuration
│   ├── netlify.toml          # Netlify deployment config
│   ├── vercel.json           # Vercel deployment config
│   └── railway.toml          # Railway deployment config
│
├── .gitattributes            # Git LFS configuration
├── .gitignore                # Git ignore rules
└── README.md                 # This file
```

## 🔑 API Endpoints

### Public Endpoints
- `GET /api/health` - Health check
- `POST /api/register` - Register new user
- `POST /api/login` - Login user
- `GET /api/trending` - Get trending movies
- `GET /api/search?q=query` - Search movies
- `POST /api/recommend` - Get recommendations (no auth required)

### Protected Endpoints (Optional)
- `POST /api/recommend-any` - Get recommendations for any movie

## 🎯 Usage

1. **Browse Movies**: View trending movies on the home page
2. **Search**: Use the search bar to find specific movies
3. **Get Recommendations**: Type a movie name to get similar movie suggestions
4. **Register/Login**: Optional - create an account for personalized features

## 📝 Environment Variables

### Backend (.env)
```env
MONGODB_URI=mongodb://localhost:27017/movie_recommender
JWT_SECRET_KEY=your-secret-key-here
FLASK_ENV=development
```

### Frontend
The frontend is configured to connect to `http://localhost:5000` in development. For production, update the API URL in the build.

## 🐛 Troubleshooting

### Large Files Issue
This project uses Git LFS for large files (`.pkl` and `.csv`). Make sure Git LFS is installed:
```bash
git lfs install
```

### Backend Not Starting
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check if port 5000 is available
- Verify `.pkl` files are present in the backend directory

### Frontend Not Loading
- Clear npm cache: `npm cache clean --force`
- Delete `node_modules` and reinstall: `rm -rf node_modules && npm install`
- Check if backend is running on port 5000

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

**Yash**

## 🙏 Acknowledgments

- TMDB API for movie data
- The Movie Database (TMDB) for movie posters and information
- Scikit-learn for machine learning capabilities
