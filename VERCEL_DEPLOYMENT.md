# Vercel Deployment Guide

## Important Considerations

### 1. **Dataset Issue**
Your `steam_reviews.csv` file (8GB) is too large for Vercel:
- Vercel has a 50MB deployment size limit
- The CSV is already excluded in `.gitignore` (good!)
- **Solution**: You'll need to either:
  - Host the CSV file externally (AWS S3, Google Cloud Storage)
  - Use a smaller sample dataset
  - Use a cloud database instead

### 2. **Model Files**
- `model.pkl` and `vectorizer.pkl` are included in the repo
- Ensure they're under 50MB total for Vercel deployment

## Deployment Steps

### Method 1: Vercel CLI (Recommended)

1. **Install Vercel CLI**:
   ```bash
   npm install -g vercel
   ```

2. **Login to Vercel**:
   ```bash
   vercel login
   ```

3. **Deploy from this directory**:
   ```bash
   vercel
   ```
   
4. **Follow the prompts**:
   - Set up and deploy: Yes
   - Which scope: (choose your account)
   - Link to existing project: No
   - Project name: game-recommendation
   - In which directory is your code located: ./
   - Want to override the settings: No

5. **For production deployment**:
   ```bash
   vercel --prod
   ```

### Method 2: Vercel Dashboard (GitHub Integration)

1. **Go to Vercel Dashboard**: https://vercel.com/new

2. **Import Git Repository**:
   - Click "Add New..." → "Project"
   - Select "Import Git Repository"
   - Choose your GitHub repo: `Harish-1828/game_recommendation`

3. **Configure Project**:
   - Framework Preset: Other
   - Root Directory: ./
   - Build Command: (leave empty)
   - Output Directory: (leave empty)
   - Install Command: `pip install -r requirements.txt`

4. **Environment Variables** (if needed):
   Add any environment variables your app needs

5. **Deploy**:
   - Click "Deploy"
   - Wait for deployment to complete

## ⚠️ Known Limitations

### This Flask app may face issues on Vercel:

1. **Serverless Function Timeout**: 
   - Free tier: 10s execution limit
   - Paid tier: 60s execution limit
   - Loading large models/CSV might timeout

2. **Stateless Functions**:
   - `user_feedback.csv` won't persist between requests
   - Need external database for user feedback

3. **Cold Starts**:
   - First request may be slow (loading models)

## Alternative Deployment Platforms

If Vercel doesn't work well, consider:

### **Render.com** (Recommended for Flask)
- Better Python/Flask support
- Free tier available
- Can handle larger files
- Easy deployment: https://render.com/

### **Railway.app**
- Great Flask support
- Free tier with good limits
- Simple deployment

### **Heroku**
- Classic Flask hosting
- Free tier (with limitations)
- Proven track record

### **PythonAnywhere**
- Specifically designed for Python apps
- Free tier available
- Very easy Flask deployment

## Troubleshooting

### If deployment fails:

1. **Check Vercel logs**:
   ```bash
   vercel logs
   ```

2. **Reduce CSV file size**: Modify `app.py` line that loads reviews:
   ```python
   reviews_df = pd.read_csv('steam_reviews.csv', nrows=1000)  # Load only 1000 rows
   ```

3. **Check deployment size**:
   ```bash
   vercel inspect
   ```

## Post-Deployment

After successful deployment:
1. Test all routes (home, search, game details, recommendations)
2. Verify models load correctly
3. Test the recommendation system
4. Note: User feedback won't save (need database integration)

## Questions?

If Vercel deployment fails, let me know and I can help you:
- Set up an alternative platform
- Optimize the app for serverless
- Configure a cloud database for the CSV data
