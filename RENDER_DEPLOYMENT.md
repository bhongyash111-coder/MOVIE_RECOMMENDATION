# 🚀 RENDER DEPLOYMENT GUIDE

## ✅ Your Project is Ready for Render!

All Railway files have been removed. Your project is now optimized for Render deployment.

---

## 📋 STEP-BY-STEP DEPLOYMENT

### **Step 1: Sign Up for Render**

1. Go to [render.com](https://render.com)
2. Click **"Get Started for Free"**
3. Sign up with **GitHub** (easiest option)
4. Authorize Render to access your repositories

---

### **Step 2: Deploy Backend**

1. **Click "New +"** → **"Web Service"**

2. **Connect Repository:**
   - Find and select: `bhongyash111-coder/MOVIE_RECOMMENDATION`
   - Click "Connect"

3. **Configure Service:**
   
   | Setting | Value |
   |---------|-------|
   | **Name** | `movie-recommender-backend` |
   | **Region** | Choose closest to you (e.g., Singapore) |
   | **Branch** | `main` |
   | **Root Directory** | `backend` |
   | **Runtime** | `Python 3` |
   | **Build Command** | `pip install -r requirements.txt` |
   | **Start Command** | `python app.py` |
   | **Instance Type** | `Free` |

4. **Add Environment Variables:**
   
   Click **"Advanced"** → **"Add Environment Variable"**
   
   Add these three variables:
   
   ```
   FLASK_ENV = production
   JWT_SECRET_KEY = movie-recommender-secret-2025-render
   MONGODB_URI = mongodb://localhost:27017/movie_recommender
   ```

5. **Click "Create Web Service"**

6. **Wait for deployment** (5-10 minutes)
   - Render will automatically download Git LFS files
   - You'll see build logs in real-time
   - Wait for "Live" status

7. **Copy your backend URL:**
   - It will look like: `https://movie-recommender-backend.onrender.com`
   - **Save this URL** - you'll need it for the frontend!

---

### **Step 3: Deploy Frontend**

1. **Click "New +"** → **"Static Site"**

2. **Connect Repository:**
   - Select: `bhongyash111-coder/MOVIE_RECOMMENDATION`
   - Click "Connect"

3. **Configure Static Site:**
   
   | Setting | Value |
   |---------|-------|
   | **Name** | `movie-recommender-frontend` |
   | **Branch** | `main` |
   | **Root Directory** | `frontend` |
   | **Build Command** | `npm install && npm run build` |
   | **Publish Directory** | `build` |

4. **Click "Create Static Site"**

5. **Wait for deployment** (3-5 minutes)

6. **Get your frontend URL:**
   - It will look like: `https://movie-recommender-frontend.onrender.com`

---

### **Step 4: Test Your Deployment**

1. **Test Backend:**
   ```
   https://your-backend-url.onrender.com/api/health
   ```
   
   Should return:
   ```json
   {
     "status": "healthy",
     "message": "Movie Recommendation API is running"
   }
   ```

2. **Test Frontend:**
   - Open: `https://your-frontend-url.onrender.com`
   - You should see the Movie Recommender homepage

---

## 🔧 IMPORTANT: Update Frontend API URL

Your frontend is currently configured to use `localhost:5000`. After deploying, you need to update it to use your Render backend URL.

**We'll do this in the next step once both services are deployed.**

---

## 📊 What to Expect

### **Backend Deployment:**
- ⏱️ **Time:** 5-10 minutes
- 📦 **Git LFS:** Automatically downloads 230MB of files
- ✅ **Status:** Look for "Live" badge

### **Frontend Deployment:**
- ⏱️ **Time:** 3-5 minutes
- 📦 **Build:** Creates optimized production bundle
- ✅ **Status:** Look for "Live" badge

---

## 🎯 Deployment Checklist

- [ ] Signed up for Render
- [ ] Connected GitHub account
- [ ] Deployed backend service
- [ ] Added environment variables
- [ ] Backend shows "Live" status
- [ ] Copied backend URL
- [ ] Deployed frontend static site
- [ ] Frontend shows "Live" status
- [ ] Tested `/api/health` endpoint
- [ ] Opened frontend URL

---

## 🆘 Troubleshooting

### **Backend fails to start:**
- Check environment variables are set correctly
- Look for Python errors in logs
- Verify Git LFS files downloaded (check file sizes in logs)

### **Frontend shows blank page:**
- Check browser console for errors
- Verify build completed successfully
- Check if API URL needs updating

### **Git LFS files not downloading:**
- Render should handle this automatically
- Check build logs for "Downloading LFS files"
- File sizes should be: similarity.pkl ~185MB, movies.pkl ~2.2MB

---

## 🎉 After Successful Deployment

Once both services are deployed:

1. **Copy both URLs**
2. **Test the backend** health endpoint
3. **Open the frontend** in browser
4. **Let me know** and I'll help you connect them!

---

## 💡 Pro Tips

- **Free tier limitations:**
  - Backend may sleep after 15 min of inactivity
  - First request after sleep takes ~30 seconds
  - Upgrade to paid tier for always-on service

- **Custom domains:**
  - You can add custom domains in Render dashboard
  - Free SSL certificates included

- **Auto-deploy:**
  - Render auto-deploys when you push to GitHub
  - No manual redeployment needed!

---

## 📝 Files in Your Project

✅ **Kept:**
- `backend/Procfile` - Heroku compatibility
- `frontend/netlify.toml` - Netlify compatibility
- `frontend/vercel.json` - Vercel compatibility
- `backend/render.yaml` - Render configuration
- `render.yaml` - Render blueprint (optional)

❌ **Removed:**
- `backend/railway.toml` - Railway config (not needed)
- `backend/nixpacks.toml` - Railway config (not needed)
- `backend/railway-build.sh` - Railway script (not needed)
- `frontend/railway.toml` - Railway config (not needed)

---

## 🚀 Ready to Deploy!

Your repository is clean and ready for Render deployment.

**Next step:** Go to [render.com](https://render.com) and follow the steps above!

Let me know when you've deployed and I'll help you connect the frontend to the backend! 🎊
