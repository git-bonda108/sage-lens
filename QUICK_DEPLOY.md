# ⚡ Quick Deployment Guide

## ✅ Current Status

- ✅ SERPER_API_KEY updated: `xoM7QXTQZt5tMMmEGokLhi6w`
- ✅ Streamlit restarted on port 8501
- ✅ All API keys configured in `.env`

## 🚀 Quick Start

### Local Access
Open your browser to: **http://localhost:8501**

### Verify Setup
```bash
# Check if Streamlit is running
curl http://localhost:8501/_stcore/health

# View logs
# Check terminal where Streamlit is running
```

## 📦 Deployment Options

### 1. Streamlit Cloud (Easiest)

1. Push to GitHub:
   ```bash
   git add .
   git commit -m "Ready for deployment"
   git push origin main
   ```

2. Go to https://share.streamlit.io/
3. Connect repository
4. Set main file: `sage_lens_enhanced.py`
5. Add secrets in Settings → Secrets:
   ```toml
   [secrets]
   OPENAI_API_KEY = "your-key"
   ANTHROPIC_API_KEY = "your-key"
   TAVILY_API_KEY = "your-key"
   SERPER_API_KEY = "xoM7QXTQZt5tMMmEGokLhi6w"
   ```
6. Deploy!

### 2. Docker (Recommended for Production)

```bash
# Build
docker build -t sage-lens .

# Run
docker run -d -p 8501:8501 \
  -e OPENAI_API_KEY="your-key" \
  -e SERPER_API_KEY="xoM7QXTQZt5tMMmEGokLhi6w" \
  sage-lens
```

### 3. Heroku

```bash
heroku create your-app-name
heroku config:set SERPER_API_KEY="xoM7QXTQZt5tMMmEGokLhi6w"
git push heroku main
```

## 📝 Environment Variables

Current `.env` configuration:
- ✅ OPENAI_API_KEY
- ✅ ANTHROPIC_API_KEY
- ✅ TAVILY_API_KEY
- ✅ SERPER_API_KEY = `xoM7QXTQZt5tMMmEGokLhi6w`

## 🔧 Troubleshooting

### Restart Streamlit
```bash
pkill -f streamlit
cd sage-lens
streamlit run sage_lens_enhanced.py
```

### Check Status
```bash
# Check if running
lsof -i :8501

# View process
ps aux | grep streamlit
```

### Common Issues
- **Port in use**: Change port with `--server.port 8502`
- **API errors**: Verify keys in `.env`
- **Import errors**: Run `pip install -r requirements.txt`

## 📚 Full Documentation

See `DEPLOYMENT_INSTRUCTIONS.md` for complete deployment guide.

---

**Ready to use!** 🎉

