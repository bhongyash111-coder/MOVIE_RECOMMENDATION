# 🚀 Deployment Guide

## Quick Start - Push to GitHub

Your project is now ready to be pushed to GitHub with Git LFS handling the large files!

### Step 1: Create a GitHub Repository

1. Go to [GitHub](https://github.com)
2. Click the "+" icon → "New repository"
3. Name it: `movie-recommendation-system`
4. **DO NOT** initialize with README (we already have one)
5. Click "Create repository"

### Step 2: Push Your Code

Run these commands in your terminal:

```bash
# Add all files
git add .

# Commit
git commit -m "Initial commit: Movie Recommendation System"

# Add your GitHub repository as remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/movie-recommendation-system.git

# Push to GitHub
git push -u origin main
```

**Note:** If you get an error about 'master' vs 'main', run:
```bash
git branch -M main
git push -u origin main
```

---

## 🌐 Hosting Options

### Option 1: Railway (Recommended - Easy & Free)

**Why Railway?**
- ✅ Free tier available
- ✅ Handles large files well
- ✅ Already configured in your project
- ✅ Supports both Python and Node.js

**Steps:**

1. **Install Railway CLI:**
```bash
npm install -g @railway/cli
```

2. **Login to Railway:**
```bash
railway login
```

3. **Deploy Backend:**
```bash
cd backend
railway init
railway up
```

4. **Deploy Frontend:**
```bash
cd ../frontend
railway init
railway up
```

5. **Set Environment Variables** (in Railway dashboard):
   - `MONGODB_URI` (if using MongoDB)
   - `JWT_SECRET_KEY`

**Get your live URL from the Railway dashboard!**

---

### Option 2: Render (Free Tier Available)

**Backend:**
1. Go to [Render](https://render.com)
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Select the `backend` directory
5. Settings:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python app.py`
   - **Environment:** Python 3

**Frontend:**
1. Click "New +" → "Static Site"
2. Connect your GitHub repository
3. Select the `frontend` directory
4. Settings:
   - **Build Command:** `npm install && npm run build`
   - **Publish Directory:** `build`

---

### Option 3: Vercel (Frontend) + Railway (Backend)

**Frontend on Vercel:**
```bash
cd frontend
npm install -g vercel
vercel
```

**Backend on Railway:**
```bash
cd backend
railway up
```

---

### Option 4: Netlify (Frontend) + Render (Backend)

**Frontend on Netlify:**
1. Go to [Netlify](https://netlify.com)
2. Drag and drop the `frontend/build` folder
3. Or connect GitHub repository

**Backend on Render:**
Follow Option 2 backend steps above.

---

## 🔧 Important Configuration

### Update Frontend API URL

After deploying the backend, you'll get a URL like:
`https://your-backend.railway.app`

You need to update the frontend to use this URL instead of `localhost:5000`.

**If you have the source code:**
Find the API configuration file and update the base URL.

**If using the build:**
You'll need to rebuild the frontend with the new API URL.

---

## 📊 Git LFS Limits

**GitHub:**
- Free: 1GB storage, 1GB bandwidth/month
- Your files: ~230MB (should be fine!)

**If you exceed limits:**
- Upgrade GitHub LFS ($5/month for 50GB)
- Or use alternative storage (see below)

---

## 💾 Alternative: Cloud Storage for Large Files

If you don't want to use Git LFS, you can store large files externally:

### Using Google Drive

1. Upload `similarity.pkl` and `movies.pkl` to Google Drive
2. Get shareable links
3. Modify `app.py` to download files on startup:

```python
import os
import requests

def download_file(url, filename):
    if not os.path.exists(filename):
        print(f"Downloading {filename}...")
        response = requests.get(url)
        with open(filename, 'wb') as f:
            f.write(response.content)

# At the start of app.py
download_file('YOUR_GOOGLE_DRIVE_LINK', 'movies.pkl')
download_file('YOUR_GOOGLE_DRIVE_LINK', 'similarity.pkl')
```

---

## ✅ Checklist Before Deployment

- [ ] Git LFS is installed and configured
- [ ] `.gitattributes` file exists
- [ ] `.gitignore` file exists
- [ ] All sensitive data is in `.env` (not committed)
- [ ] README.md is complete
- [ ] Backend runs locally without errors
- [ ] Frontend builds successfully
- [ ] API endpoints are tested

---

## 🐛 Common Issues

### "This exceeds GitHub's file size limit"
- Make sure Git LFS is installed: `git lfs install`
- Verify `.gitattributes` exists
- Run: `git lfs migrate import --include="*.pkl,*.csv"`

### "Port already in use"
- Backend: Change port in `app.py`
- Frontend: Set `PORT=3001` in environment

### "Module not found"
- Backend: `pip install -r requirements.txt`
- Frontend: `npm install`

---

## 🎉 You're Ready!

Your project is now configured for deployment. Choose your preferred hosting platform and follow the steps above!

**Need help?** Check the main README.md for more details.
