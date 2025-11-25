@echo off
REM 🚀 Quick Deployment Script for Movie Recommendation System (Windows)

echo 🎬 Movie Recommendation System - Deployment Helper
echo ==================================================
echo.

REM Check if Git is initialized
if not exist ".git" (
    echo ❌ Git repository not found. Please run this from the project root.
    exit /b 1
)

echo 📋 What would you like to do?
echo.
echo 1. Push to GitHub (first time)
echo 2. Push updates to GitHub
echo 3. Deploy to Railway (Backend)
echo 4. Deploy to Railway (Frontend)
echo 5. Deploy both to Railway
echo 6. Check Git LFS status
echo.
set /p choice="Enter your choice (1-6): "

if "%choice%"=="1" (
    echo.
    set /p repo_url="Enter your GitHub repository URL (e.g., https://github.com/username/repo.git): "
    git remote add origin %repo_url%
    git branch -M main
    git push -u origin main
    echo ✅ Code pushed to GitHub!
) else if "%choice%"=="2" (
    git add .
    set /p commit_msg="Enter commit message: "
    git commit -m "%commit_msg%"
    git push
    echo ✅ Updates pushed to GitHub!
) else if "%choice%"=="3" (
    echo 🚂 Deploying backend to Railway...
    cd backend
    railway up
    cd ..
    echo ✅ Backend deployed!
) else if "%choice%"=="4" (
    echo 🚂 Deploying frontend to Railway...
    cd frontend
    railway up
    cd ..
    echo ✅ Frontend deployed!
) else if "%choice%"=="5" (
    echo 🚂 Deploying both backend and frontend to Railway...
    cd backend
    railway up
    cd ../frontend
    railway up
    cd ..
    echo ✅ Both deployed!
) else if "%choice%"=="6" (
    echo 📊 Git LFS Status:
    git lfs ls-files
    echo.
    echo 📦 Git LFS Storage:
    git lfs env
) else (
    echo ❌ Invalid choice
    exit /b 1
)

echo.
echo 🎉 Done!
pause
