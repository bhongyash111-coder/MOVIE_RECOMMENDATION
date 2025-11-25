# 🚀 EASY DEPLOYMENT OPTIONS

Your code is on GitHub! Now here are the **easiest** ways to deploy without complex CLI setup:

---

## ✅ **OPTION 1: Render (Easiest - No CLI Required)**

### **Backend Deployment:**

1. Go to [Render.com](https://render.com) and sign up/login
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub account
4. Select repository: `MOVIE_RECOMMENDATION`
5. Configure:
   - **Name:** `movie-recommender-backend`
   - **Root Directory:** `backend`
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python app.py`
6. Click **"Create Web Service"**

**Environment Variables to Add:**
- `MONGODB_URI` = (your MongoDB connection string, or leave default)
- `JWT_SECRET_KEY` = `your-secret-key-123`

### **Frontend Deployment:**

1. Click **"New +"** → **"Static Site"**
2. Select repository: `MOVIE_RECOMMENDATION`
3. Configure:
   - **Name:** `movie-recommender-frontend`
   - **Root Directory:** `frontend`
   - **Build Command:** `npm install && npm run build`
   - **Publish Directory:** `build`
4. Click **"Create Static Site"**

**After backend is deployed:**
- You'll need to update the frontend to use the backend URL
- Rebuild the frontend with the new API URL

---

## ✅ **OPTION 2: Railway (Web Dashboard - No CLI)**

### **Backend Deployment:**

1. Go to [Railway.app](https://railway.app) and sign up/login
2. Click **"New Project"** → **"Deploy from GitHub repo"**
3. Select `MOVIE_RECOMMENDATION`
4. Railway will auto-detect the backend
5. Add environment variables:
   - `MONGODB_URI` = (your MongoDB connection)
   - `JWT_SECRET_KEY` = `your-secret-key-123`
6. Click **"Deploy"**

### **Frontend Deployment:**

1. In the same project, click **"New Service"**
2. Select **"GitHub Repo"** → `MOVIE_RECOMMENDATION`
3. Set root directory to `frontend`
4. Railway will auto-detect and deploy

---

## ✅ **OPTION 3: Vercel (Frontend) + Render (Backend)**

### **Backend on Render:**
Follow Option 1 backend steps above

### **Frontend on Vercel:**

1. Go to [Vercel.com](https://vercel.com) and sign up/login
2. Click **"Add New"** → **"Project"**
3. Import `MOVIE_RECOMMENDATION` from GitHub
4. Configure:
   - **Framework Preset:** `Create React App`
   - **Root Directory:** `frontend`
   - **Build Command:** `npm run build`
   - **Output Directory:** `build`
5. Click **"Deploy"**

---

## ✅ **OPTION 4: Netlify (Frontend Only)**

1. Go to [Netlify.com](https://netlify.com) and sign up/login
2. Click **"Add new site"** → **"Import an existing project"**
3. Connect GitHub and select `MOVIE_RECOMMENDATION`
4. Configure:
   - **Base directory:** `frontend`
   - **Build command:** `npm run build`
   - **Publish directory:** `frontend/build`
5. Click **"Deploy site"**

---

## 🎯 **RECOMMENDED APPROACH:**

**Use Render for both Backend and Frontend** (Option 1)
- ✅ Free tier available
- ✅ Easy to use web interface
- ✅ Handles large files well
- ✅ Auto-deploys from GitHub
- ✅ No CLI installation needed

---

## 📝 **Important Notes:**

### **For Backend:**
- Your large `.pkl` files are in the GitHub repo (via Git LFS)
- Render/Railway will download them automatically
- Make sure to set environment variables

### **For Frontend:**
- After deploying the backend, you'll get a URL like:
  `https://movie-recommender-backend.onrender.com`
- You need to update the frontend to use this URL instead of `localhost:5000`
- Then rebuild and redeploy the frontend

---

## 🔧 **Update Frontend API URL:**

Since you don't have the source code for the frontend, you have two options:

1. **Use the built version as-is** (will only work locally)
2. **Ask me to help you configure the API URL** for production

---

## 🆘 **Need Help?**

Let me know which platform you want to use, and I can guide you through the specific steps!

**Easiest path:**
1. Deploy backend on Render (5 minutes)
2. Get the backend URL
3. Update frontend API configuration
4. Deploy frontend on Render/Netlify

---

**Your GitHub repo:** https://github.com/bhongyash111-coder/MOVIE_RECOMMENDATION

Ready to deploy! 🚀
