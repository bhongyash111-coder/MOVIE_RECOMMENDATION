# 🚂 RAILWAY DEPLOYMENT GUIDE

## ⚠️ Important: Your Project Structure

Your project has **TWO separate applications**:
- `backend/` - Python Flask API
- `frontend/` - React app

You need to deploy them as **TWO SEPARATE Railway services**.

---

## 🎯 DEPLOYMENT STEPS

### **Method 1: Using Railway Web Dashboard (EASIEST)**

#### **Step 1: Deploy Backend**

1. Go to [Railway.app](https://railway.app)
2. Click **"New Project"**
3. Select **"Deploy from GitHub repo"**
4. Choose: `bhongyash111-coder/MOVIE_RECOMMENDATION`
5. Railway will create a service - click **"Settings"**
6. **Important:** Set **Root Directory** to `backend`
7. Under **"Deploy"**, set:
   - **Build Command:** (leave empty, Railway auto-detects)
   - **Start Command:** `python app.py`
8. Add **Environment Variables**:
   - `PORT` = `5000`
   - `MONGODB_URI` = `mongodb://localhost:27017/movie_recommender` (or your MongoDB URL)
   - `JWT_SECRET_KEY` = `your-secret-key-change-this`
9. Click **"Deploy"**

**Wait for deployment to complete** (5-10 minutes due to large files)

#### **Step 2: Deploy Frontend**

1. In the same Railway project, click **"New Service"**
2. Select **"GitHub Repo"** → `MOVIE_RECOMMENDATION`
3. Click **"Settings"**
4. **Important:** Set **Root Directory** to `frontend`
5. Under **"Deploy"**, set:
   - **Build Command:** `npm install && npm run build`
   - **Start Command:** `npx serve -s build`
6. Add **Environment Variables**:
   - `REACT_APP_API_URL` = `<your-backend-url-from-step-1>`
7. Click **"Deploy"**

---

### **Method 2: Using Railway CLI (Advanced)**

If you want to use the CLI, you need to deploy from within each directory:

#### **Deploy Backend:**

```bash
cd backend
railway login
railway init
railway up
cd ..
```

#### **Deploy Frontend:**

```bash
cd frontend
railway login
railway link  # Link to the same project
railway up
cd ..
```

---

## 🔧 TROUBLESHOOTING

### **Error: "Railpack could not determine how to build the app"**

**Cause:** You tried to deploy from the root directory, which contains both backend and frontend.

**Solution:** Deploy each folder separately by setting the **Root Directory** in Railway settings.

### **Error: "Large files not found"**

**Cause:** Git LFS files might not be downloaded.

**Solution:** Railway should automatically handle Git LFS. If not:
1. Check your GitHub repository has LFS files
2. Verify `.gitattributes` is committed
3. Try redeploying

### **Backend deploys but crashes**

**Check:**
1. Environment variables are set correctly
2. Port is set to the Railway-provided `PORT` variable
3. Large `.pkl` files are present

---

## 📝 ALTERNATIVE: Use Render Instead

If Railway is giving you trouble, **Render.com** is easier for this type of project:

### **Render Backend:**
1. Go to [Render.com](https://render.com)
2. New → Web Service
3. Connect GitHub → Select repo
4. **Root Directory:** `backend`
5. **Build Command:** `pip install -r requirements.txt`
6. **Start Command:** `python app.py`
7. Deploy!

### **Render Frontend:**
1. New → Static Site
2. Connect GitHub → Select repo
3. **Root Directory:** `frontend`
4. **Build Command:** `npm install && npm run build`
5. **Publish Directory:** `build`
6. Deploy!

---

## ✅ RECOMMENDED APPROACH

**Use Render.com instead of Railway** for this project because:
- ✅ Better support for monorepos
- ✅ Easier to configure root directories
- ✅ Better free tier for static sites
- ✅ Handles Git LFS automatically

---

## 🆘 NEED HELP?

Let me know if you:
1. Want to try Render instead (easier)
2. Need help with Railway configuration
3. Want to deploy to a different platform

Your code is ready - just need to choose the right deployment method!
