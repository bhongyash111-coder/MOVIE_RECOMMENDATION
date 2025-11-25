#!/bin/bash

# 🚀 Quick Deployment Script for Movie Recommendation System

echo "🎬 Movie Recommendation System - Deployment Helper"
echo "=================================================="
echo ""

# Check if Git is initialized
if [ ! -d ".git" ]; then
    echo "❌ Git repository not found. Please run this from the project root."
    exit 1
fi

echo "📋 What would you like to do?"
echo ""
echo "1. Push to GitHub (first time)"
echo "2. Push updates to GitHub"
echo "3. Deploy to Railway (Backend)"
echo "4. Deploy to Railway (Frontend)"
echo "5. Deploy both to Railway"
echo "6. Check Git LFS status"
echo ""
read -p "Enter your choice (1-6): " choice

case $choice in
    1)
        echo ""
        read -p "Enter your GitHub repository URL (e.g., https://github.com/username/repo.git): " repo_url
        git remote add origin "$repo_url"
        git branch -M main
        git push -u origin main
        echo "✅ Code pushed to GitHub!"
        ;;
    2)
        git add .
        read -p "Enter commit message: " commit_msg
        git commit -m "$commit_msg"
        git push
        echo "✅ Updates pushed to GitHub!"
        ;;
    3)
        echo "🚂 Deploying backend to Railway..."
        cd backend
        railway up
        cd ..
        echo "✅ Backend deployed!"
        ;;
    4)
        echo "🚂 Deploying frontend to Railway..."
        cd frontend
        railway up
        cd ..
        echo "✅ Frontend deployed!"
        ;;
    5)
        echo "🚂 Deploying both backend and frontend to Railway..."
        cd backend
        railway up
        cd ../frontend
        railway up
        cd ..
        echo "✅ Both deployed!"
        ;;
    6)
        echo "📊 Git LFS Status:"
        git lfs ls-files
        echo ""
        echo "📦 Git LFS Storage:"
        git lfs env
        ;;
    *)
        echo "❌ Invalid choice"
        exit 1
        ;;
esac

echo ""
echo "🎉 Done!"
