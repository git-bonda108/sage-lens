# 🚀 Complete Deployment Guide: Sage-Lens

This guide covers deployment to Streamlit Cloud for the Sage-Lens application.

## 📋 Pre-Deployment Checklist

- [x] Code is tested locally
- [x] All dependencies listed in `requirements-sage-lens.txt`
- [x] `.gitignore` excludes `.env` files
- [x] API keys are ready (not committed to repo)
- [x] Repository is on GitHub
- [x] Streamlit Cloud account is set up

## 🔧 Step-by-Step Deployment

### 1. Prepare Your Code

#### Verify File Structure
```
SDLC/
├── sage-lens.py              # Main application file
├── requirements-sage-lens.txt # Dependencies
├── .gitignore                # Excludes .env
├── README_SAGE_LENS.md        # Documentation
└── .env                       # Local only (not in git)
```

#### Check Dependencies
Ensure `requirements-sage-lens.txt` includes:
- streamlit>=1.31.0
- python-dotenv>=1.0.1
- openai>=1.14.0
- anthropic>=0.69.0
- tavily-python>=0.3.0
- youtube-search>=2.1.0
- requests>=2.31.0

### 2. Push to GitHub

```bash
# Initialize git (if not already done)
git init

# Add all files (except .env which is in .gitignore)
git add .

# Commit
git commit -m "Initial commit: Sage-Lens AI Research Engine"

# Add remote (replace with your repo URL)
git remote add origin https://github.com/yourusername/your-repo.git

# Push to main branch
git branch -M main
git push -u origin main
```

### 3. Deploy to Streamlit Cloud

1. **Go to Streamlit Cloud**
   - Visit: https://share.streamlit.io/
   - Sign in with GitHub

2. **Create New App**
   - Click **"New app"**
   - Select your repository
   - Choose branch: `main`
   - **Main file path**: `sage-lens.py`
   - **Python version**: 3.10 (recommended)

3. **Configure Secrets**
   - Click **"Advanced settings"**
   - Go to **"Secrets"** tab
   - Add your API keys:

```toml
[secrets]
OPENAI_API_KEY = "sk-proj-..."
ANTHROPIC_API_KEY = "sk-ant-api03-..."
TAVILY_API_KEY = "tvly-dev-..."
SERPER_API_KEY = "xoM7QXTQZt5tMMmEGokLhi6w"
```

4. **Deploy**
   - Click **"Deploy"**
   - Wait for build to complete (2-5 minutes)
   - App will be available at: `https://your-app-name.streamlit.app`

### 4. Verify Deployment

After deployment, verify:
- ✅ App loads without errors
- ✅ No authentication errors in logs
- ✅ Can enter research topic
- ✅ Generate button works
- ✅ Content generation succeeds
- ✅ Web references appear
- ✅ Video guides load

## 🔍 Troubleshooting Deployment

### Build Fails

**Error**: "Module not found"
- **Solution**: Check `requirements-sage-lens.txt` includes all dependencies
- Verify package names are correct (case-sensitive)

**Error**: "Python version incompatible"
- **Solution**: Use Python 3.9+ (recommended: 3.10)

### App Crashes on Load

**Error**: "OPENAI_API_KEY is not set"
- **Solution**: Add API keys to Streamlit Secrets
- Verify secret names match exactly (case-sensitive)

**Error**: "Authentication error"
- **Solution**: Verify API keys are correct and active
- Check keys have sufficient credits/quota

### Runtime Errors

**Error**: "Search error"
- **Solution**: Tavily/Serper keys are optional
- App will work without them (just no web search)

**Error**: "Timeout errors"
- **Solution**: Check API provider status
- Verify network connectivity

## 📊 Monitoring

### Streamlit Cloud Dashboard

Monitor your app:
- **Logs**: View real-time logs in Streamlit Cloud
- **Metrics**: Track app usage and performance
- **Errors**: Review error logs for issues

### API Usage Monitoring

Monitor API costs:
- **OpenAI**: https://platform.openai.com/usage
- **Anthropic**: https://console.anthropic.com/settings/usage
- Set up billing alerts

## 🔄 Updating Your App

### Code Updates

1. Make changes locally
2. Test thoroughly
3. Commit and push:
   ```bash
   git add .
   git commit -m "Update: description of changes"
   git push origin main
   ```
4. Streamlit Cloud auto-deploys on push

### Secret Updates

1. Go to Streamlit Cloud → Your App → Settings
2. Update secrets as needed
3. App will restart automatically

## 🎯 Best Practices

1. **Version Control**
   - Always test locally before pushing
   - Use meaningful commit messages
   - Tag releases for important updates

2. **Security**
   - Never commit API keys
   - Use Streamlit Secrets for production
   - Rotate keys regularly

3. **Performance**
   - Monitor API usage and costs
   - Optimize prompts to reduce tokens
   - Cache results when possible

4. **Documentation**
   - Keep README updated
   - Document API changes
   - Update deployment guide for new steps

## 📞 Support Resources

- **Streamlit Cloud Docs**: https://docs.streamlit.io/streamlit-community-cloud
- **OpenAI API Docs**: https://platform.openai.com/docs
- **Anthropic API Docs**: https://docs.anthropic.com
- **Streamlit Forum**: https://discuss.streamlit.io

## ✅ Post-Deployment Checklist

- [ ] App is accessible via public URL
- [ ] All features work correctly
- [ ] API keys are configured
- [ ] No errors in logs
- [ ] Documentation is updated
- [ ] Monitoring is set up
- [ ] Team has access (if applicable)

---

**Your app is now live! 🎉**

