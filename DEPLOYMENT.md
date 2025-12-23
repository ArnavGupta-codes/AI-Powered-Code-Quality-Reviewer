# Deployment Guide

This guide explains how to deploy the AI Code Quality Reviewer for recruiters and others to use.

## Option 1: Deploy to Render (Recommended - Free)

### Prerequisites
- GitHub account with your repository pushed
- Render account (https://render.com)

### Steps

1. **Sign up on Render**
   - Go to https://render.com
   - Click "Sign up" and connect your GitHub account

2. **Create a new Web Service**
   - Click "New +" → "Web Service"
   - Select your AI-Powered-Code-Quality-Reviewer repository
   - Click "Connect"

3. **Configure the service**
   - **Name:** ai-code-quality-reviewer
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
   - **Instance Type:** Free

4. **Add environment variables** (if needed)
   - No additional variables required

5. **Deploy**
   - Click "Create Web Service"
   - Wait for deployment (2-3 minutes)
   - Your app will be live at: `https://ai-code-quality-reviewer.onrender.com`

## Option 2: Deploy to Railway (Free)

1. **Sign up on Railway**
   - Go to https://railway.app
   - Click "Sign up with GitHub"

2. **Import your project**
   - Click "New Project" → "Deploy from GitHub"
   - Select your repository
   - Click "Deploy"

3. **Configure**
   - Railway auto-detects Python
   - Set Start Command: `gunicorn app:app`

4. **Deploy**
   - Railway automatically deploys when you push to GitHub
   - Access your app via the provided domain

## Option 3: Deploy to Heroku (Paid after free tier)

1. **Install Heroku CLI**
   ```bash
   brew tap heroku/brew && brew install heroku
   ```

2. **Login to Heroku**
   ```bash
   heroku login
   ```

3. **Create Heroku app**
   ```bash
   heroku create ai-code-quality-reviewer
   ```

4. **Add Procfile**
   ```bash
   echo "web: gunicorn app:app" > Procfile
   ```

5. **Deploy**
   ```bash
   git push heroku main
   ```

## Option 4: Deploy to PythonAnywhere (Free)

1. **Sign up at PythonAnywhere**
   - Go to https://www.pythonanywhere.com
   - Create a free account

2. **Clone your repository**
   - Use the Bash console in PythonAnywhere
   ```bash
   git clone https://github.com/ArnavGupta-codes/AI-Powered-Code-Quality-Reviewer.git
   ```

3. **Create a Flask web app**
   - Go to "Web" tab
   - Add a new Flask web app
   - Configure to point to your app.py

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Reload app**
   - Click "Reload" in the Web tab

## Local Testing Before Deployment

1. **Install additional dependencies**
   ```bash
   pip install flask gunicorn
   ```

2. **Run locally**
   ```bash
   python app.py
   ```

3. **Access at** http://localhost:5000

## Sharing with Recruiters

Once deployed, share the URL:

- **Direct link:** https://your-deployed-url.com
- **GitHub:** Include the link in your GitHub README
- **Resume:** Add "Live Demo" link to your resume
- **Portfolio:** Feature it prominently

## Performance Tips

- Cold starts might take 10-30 seconds on free tier
- Consider upgrading to paid tier if slow
- Monitor free tier monthly bandwidth limits

## Troubleshooting

### 500 Error
- Check application logs on the deployment platform
- Ensure all dependencies in requirements.txt are installed
- Verify models are in the correct path

### File Upload Issues
- Check file size limit (currently 16MB)
- Verify file format is supported (.cpp, .java, .py)

### Slow Performance
- Free tier may be slow initially
- Deploy to a paid tier for better performance
- Consider using cloud storage for models

## Updating Your Deployment

Simply push changes to GitHub:
```bash
git add .
git commit -m "Update feature"
git push origin main
```

Most platforms auto-deploy on push.

## Next Steps

1. Deploy to your chosen platform
2. Test with recruiters
3. Gather feedback
4. Improve features
5. Scale if needed
