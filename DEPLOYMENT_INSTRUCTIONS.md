# 🚀 Deployment Instructions - Sage-Lens Enhanced

Complete deployment guide for Sage-Lens Enhanced on various platforms.

## 📋 Table of Contents

1. [Prerequisites](#prerequisites)
2. [Local Deployment](#local-deployment)
3. [Streamlit Cloud Deployment](#streamlit-cloud-deployment)
4. [Docker Deployment](#docker-deployment)
5. [Production Deployment](#production-deployment)
6. [Troubleshooting](#troubleshooting)

---

## Prerequisites

### Required API Keys

- **OPENAI_API_KEY** (Required) - Get from [OpenAI Platform](https://platform.openai.com/api-keys)
- **ANTHROPIC_API_KEY** (Optional but recommended) - Get from [Anthropic Console](https://console.anthropic.com/settings/keys)
- **TAVILY_API_KEY** (Optional) - Get from [Tavily](https://tavily.com/)
- **SERPER_API_KEY** (Optional) - Get from [Serper.dev](https://serper.dev/)

### System Requirements

- Python 3.9 or higher
- pip or conda package manager
- Git (for version control)

---

## Local Deployment

### Step 1: Clone and Setup

```bash
# Clone the repository
git clone https://github.com/git-bonda108/sage-lens.git
cd sage-lens

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install OpenAI Agents SDK (optional but recommended)
pip install openai-agents
```

### Step 2: Configure Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY="sk-proj-your-key-here"
ANTHROPIC_API_KEY="sk-ant-api03-your-key-here"
TAVILY_API_KEY="tvly-dev-your-key-here"
SERPER_API_KEY="xoM7QXTQZt5tMMmEGokLhi6w"
```

**Important**: Never commit the `.env` file to version control!

### Step 3: Run the Application

```bash
# Option 1: Using Streamlit directly
streamlit run sage_lens_enhanced.py

# Option 2: Using Python module
python -m streamlit run sage_lens_enhanced.py

# Option 3: With custom port
streamlit run sage_lens_enhanced.py --server.port 8502
```

### Step 4: Access the Application

Open your browser and navigate to:
- Default: `http://localhost:8501`
- Custom port: `http://localhost:YOUR_PORT`

---

## Streamlit Cloud Deployment

### Step 1: Prepare Your Repository

1. **Ensure your code is on GitHub**
   ```bash
   git add .
   git commit -m "Prepare for Streamlit Cloud deployment"
   git push origin main
   ```

2. **Verify file structure**
   - `sage_lens_enhanced.py` should be in the root
   - `requirements.txt` should be in the root
   - `.gitignore` should exclude `.env` files

### Step 2: Deploy to Streamlit Cloud

1. **Go to Streamlit Cloud**
   - Visit: https://share.streamlit.io/
   - Sign in with your GitHub account

2. **Create New App**
   - Click "New app"
   - Select your repository: `git-bonda108/sage-lens`
   - Set **Main file path**: `sage_lens_enhanced.py`
   - Set **Python version**: 3.9 or higher (recommended: 3.10+)
   - Click "Deploy"

### Step 3: Configure Secrets

1. **Go to App Settings**
   - In your app dashboard, click "Settings" (⚙️ icon)
   - Navigate to "Secrets" tab

2. **Add API Keys**
   Click "Edit secrets" and add:

   ```toml
   [secrets]
   OPENAI_API_KEY = "sk-proj-your-key-here"
   ANTHROPIC_API_KEY = "sk-ant-api03-your-key-here"
   TAVILY_API_KEY = "tvly-dev-your-key-here"
   SERPER_API_KEY = "xoM7QXTQZt5tMMmEGokLhi6w"
   ```

3. **Save and Restart**
   - Click "Save"
   - Wait for the app to automatically restart
   - Your app should now be live!

### Step 4: Access Your Deployed App

Your app will be available at:
```
https://YOUR-APP-NAME.streamlit.app
```

### Streamlit Cloud Configuration File

You can also create `.streamlit/config.toml` in your repository:

```toml
[server]
port = 8501
enableCORS = false
enableXsrfProtection = true

[browser]
gatherUsageStats = false
```

---

## Docker Deployment

### Step 1: Create Dockerfile

Create a `Dockerfile` in the project root:

```dockerfile
FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install OpenAI Agents SDK
RUN pip install --no-cache-dir openai-agents

# Copy application files
COPY sage_lens_enhanced.py .
COPY .streamlit .streamlit

# Expose port
EXPOSE 8501

# Health check
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Run Streamlit
CMD ["streamlit", "run", "sage_lens_enhanced.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### Step 2: Create .dockerignore

Create `.dockerignore`:

```
.env
__pycache__
*.pyc
*.pyo
*.pyd
.Python
venv/
env/
.git
.gitignore
*.md
```

### Step 3: Build and Run Docker Container

```bash
# Build the image
docker build -t sage-lens-enhanced .

# Run the container
docker run -d \
  -p 8501:8501 \
  -e OPENAI_API_KEY="your-key" \
  -e ANTHROPIC_API_KEY="your-key" \
  -e TAVILY_API_KEY="your-key" \
  -e SERPER_API_KEY="xoM7QXTQZt5tMMmEGokLhi6w" \
  --name sage-lens \
  sage-lens-enhanced

# Or use docker-compose (see below)
```

### Step 4: Docker Compose (Recommended)

Create `docker-compose.yml`:

```yaml
version: '3.8'

services:
  sage-lens:
    build: .
    ports:
      - "8501:8501"
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
      - TAVILY_API_KEY=${TAVILY_API_KEY}
      - SERPER_API_KEY=${SERPER_API_KEY}
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8501/_stcore/health"]
      interval: 30s
      timeout: 10s
      retries: 3
```

Run with:
```bash
docker-compose up -d
```

---

## Production Deployment

### Option 1: AWS EC2 / Google Cloud / Azure VM

1. **Launch a VM instance**
   - Ubuntu 20.04 or later
   - At least 2GB RAM, 1 CPU core

2. **Install Dependencies**
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip python3-venv git nginx
   ```

3. **Clone and Setup**
   ```bash
   git clone https://github.com/git-bonda108/sage-lens.git
   cd sage-lens
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   pip install openai-agents
   ```

4. **Configure Environment**
   ```bash
   nano .env
   # Add your API keys
   ```

5. **Run with systemd**
   Create `/etc/systemd/system/sage-lens.service`:

   ```ini
   [Unit]
   Description=Sage-Lens Enhanced Streamlit App
   After=network.target

   [Service]
   Type=simple
   User=ubuntu
   WorkingDirectory=/home/ubuntu/sage-lens
   Environment="PATH=/home/ubuntu/sage-lens/venv/bin"
   ExecStart=/home/ubuntu/sage-lens/venv/bin/streamlit run sage_lens_enhanced.py --server.port 8501 --server.address 0.0.0.0
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```

   Enable and start:
   ```bash
   sudo systemctl enable sage-lens
   sudo systemctl start sage-lens
   ```

6. **Configure Nginx Reverse Proxy**
   Create `/etc/nginx/sites-available/sage-lens`:

   ```nginx
   server {
       listen 80;
       server_name your-domain.com;

       location / {
           proxy_pass http://127.0.0.1:8501;
           proxy_http_version 1.1;
           proxy_set_header Upgrade $http_upgrade;
           proxy_set_header Connection "upgrade";
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           proxy_set_header X-Forwarded-Proto $scheme;
           proxy_read_timeout 86400;
       }
   }
   ```

   Enable:
   ```bash
   sudo ln -s /etc/nginx/sites-available/sage-lens /etc/nginx/sites-enabled/
   sudo nginx -t
   sudo systemctl restart nginx
   ```

### Option 2: Heroku

1. **Install Heroku CLI**
   ```bash
   # macOS
   brew tap heroku/brew && brew install heroku
   ```

2. **Create Procfile**
   ```
   web: streamlit run sage_lens_enhanced.py --server.port=$PORT --server.address=0.0.0.0
   ```

3. **Create runtime.txt**
   ```
   python-3.10.0
   ```

4. **Deploy**
   ```bash
   heroku login
   heroku create your-app-name
   heroku config:set OPENAI_API_KEY="your-key"
   heroku config:set ANTHROPIC_API_KEY="your-key"
   heroku config:set TAVILY_API_KEY="your-key"
   heroku config:set SERPER_API_KEY="xoM7QXTQZt5tMMmEGokLhi6w"
   git push heroku main
   ```

### Option 3: Railway

1. **Connect Repository**
   - Go to [Railway](https://railway.app/)
   - Connect your GitHub repository

2. **Configure Environment Variables**
   - Add all API keys in Railway dashboard
   - Set `PORT` environment variable (Railway provides this)

3. **Deploy**
   - Railway will automatically detect and deploy
   - Update `Procfile` if needed:
     ```
     web: streamlit run sage_lens_enhanced.py --server.port=$PORT --server.address=0.0.0.0
     ```

---

## Environment Variables Reference

| Variable | Required | Description | Example |
|----------|----------|-------------|---------|
| `OPENAI_API_KEY` | ✅ Yes | OpenAI API key | `sk-proj-...` |
| `ANTHROPIC_API_KEY` | ⚠️ Optional | Anthropic API key | `sk-ant-api03-...` |
| `TAVILY_API_KEY` | ⚠️ Optional | Tavily search API key | `tvly-dev-...` |
| `SERPER_API_KEY` | ⚠️ Optional | Serper Google search API key | `xoM7QXTQZt5tMMmEGokLhi6w` |

---

## Security Best Practices

1. **Never commit API keys**
   - Add `.env` to `.gitignore`
   - Use environment variables or secrets management

2. **Use HTTPS in production**
   - Configure SSL/TLS certificates
   - Use Let's Encrypt for free certificates

3. **Set up rate limiting**
   - Consider implementing rate limits
   - Monitor API usage

4. **Regular updates**
   - Keep dependencies updated
   - Monitor security advisories

5. **Access control**
   - Consider adding authentication
   - Use Streamlit's built-in authentication features

---

## Troubleshooting

### Issue: App won't start

**Solutions:**
- Check Python version: `python --version` (should be 3.9+)
- Verify dependencies: `pip install -r requirements.txt`
- Check port availability: `lsof -i :8501`
- Review logs for errors

### Issue: API key errors

**Solutions:**
- Verify keys are set correctly
- Check for extra spaces or quotes
- Ensure keys are active and have credits
- Test keys directly with API providers

### Issue: 403 Forbidden (Serper)

**Solutions:**
- Verify SERPER_API_KEY is correct
- Check API key format (no quotes needed)
- Ensure key has sufficient quota
- Verify Content-Type header is set

### Issue: Agent initialization fails

**Solutions:**
- Install OpenAI Agents SDK: `pip install openai-agents`
- App will fall back to standard mode automatically
- Check console for specific error messages

### Issue: Port already in use

**Solutions:**
- Use different port: `--server.port 8502`
- Kill existing process: `pkill -f streamlit`
- Check what's using the port: `lsof -i :8501`

---

## Monitoring and Maintenance

### Health Checks

Monitor your application:
- Streamlit Cloud: Built-in monitoring
- Docker: Health check endpoint
- Custom: Add monitoring endpoints

### Logs

View logs:
- **Local**: Check terminal output
- **Streamlit Cloud**: App logs in dashboard
- **Docker**: `docker logs sage-lens`
- **Systemd**: `journalctl -u sage-lens -f`

### Updates

To update the application:
1. Pull latest changes: `git pull`
2. Update dependencies: `pip install -r requirements.txt --upgrade`
3. Restart the application

---

## Support

For issues or questions:
1. Check the troubleshooting section
2. Review GitHub issues
3. Check API provider documentation
4. Verify environment variables

---

## Quick Reference Commands

```bash
# Local development
streamlit run sage_lens_enhanced.py

# With custom port
streamlit run sage_lens_enhanced.py --server.port 8502

# Docker
docker-compose up -d

# Systemd
sudo systemctl restart sage-lens

# Check logs
docker logs sage-lens
journalctl -u sage-lens -f
```

---

**Last Updated**: 2025-01-27
**Version**: 2.0.0 Enhanced

