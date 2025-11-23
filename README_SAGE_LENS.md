# 🔍 Sage-Lens: Agentic AI Research Engine

A powerful Streamlit-based research platform that leverages multiple AI providers (OpenAI GPT-4 and Anthropic Claude) to generate comprehensive documentation, curate web resources, and find relevant video guides for any research topic.

## ✨ Features

- **Multi-Provider AI Generation**: Uses both OpenAI GPT-4 Turbo and Anthropic Claude 3.5 Sonnet to generate comprehensive documentation
- **Intelligent Web Search**: Integrates Tavily and Google Serper APIs for curated web references
- **Video Discovery**: Automatically finds relevant YouTube videos related to your research topic
- **Version History**: Track and compare different versions of generated documentation
- **Real-time Metrics**: View processing time and AI engine used for each generation
- **Beautiful UI**: Modern, responsive interface with expandable sections and organized layouts

## 🚀 Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd SDLC
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements-sage-lens.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   OPENAI_API_KEY="sk-proj-..."
   ANTHROPIC_API_KEY="sk-ant-api03-..."
   TAVILY_API_KEY="tvly-dev-..."
   SERPER_API_KEY="xoM7QXTQZt5tMMmEGokLhi6w"
   ```

4. **Run the application**
   ```bash
   streamlit run sage-lens.py
   ```

5. **Access the app**
   Open your browser to `http://localhost:8501`

## 📋 Prerequisites

### Required API Keys

1. **OPENAI_API_KEY** (Required)
   - Get from: https://platform.openai.com/api-keys
   - Used for GPT-4 Turbo content generation

2. **ANTHROPIC_API_KEY** (Required)
   - Get from: https://console.anthropic.com/settings/keys
   - Used for Claude 3.5 Sonnet content generation

### Optional API Keys

3. **TAVILY_API_KEY** (Recommended)
   - Get from: https://tavily.com/
   - Used for intelligent web search

4. **SERPER_API_KEY** (Recommended)
   - Get from: https://serper.dev/
   - Used for Google search integration

## 🌐 Streamlit Cloud Deployment

### Step 1: Prepare Your Repository

1. Ensure `sage-lens.py` is in the repository root
2. Include `requirements-sage-lens.txt` with all dependencies
3. Verify `.gitignore` excludes `.env` files

### Step 2: Deploy to Streamlit Cloud

1. Go to https://share.streamlit.io/
2. Click **"New app"**
3. Connect your GitHub repository
4. Set **Main file path**: `sage-lens.py`
5. Set **Python version**: 3.9 or higher (recommended: 3.10+)

### Step 3: Configure Secrets

In Streamlit Cloud, go to **Settings → Secrets** and add:

```toml
[secrets]
OPENAI_API_KEY = "sk-proj-..."
ANTHROPIC_API_KEY = "sk-ant-api03-..."
TAVILY_API_KEY = "tvly-dev-..."
SERPER_API_KEY = "xoM7QXTQZt5tMMmEGokLhi6w"
```

**Minimum Required Secrets:**
```toml
[secrets]
OPENAI_API_KEY = "sk-proj-..."
ANTHROPIC_API_KEY = "sk-ant-api03-..."
```

### Step 4: Deploy

Click **"Deploy"** and wait for the app to build and launch.

## 📖 Usage Guide

### Basic Usage

1. **Enter Research Topic**: Type your research topic in the text area
   - Example: "Transformer Architecture Optimization"
   - Be specific for better results

2. **Generate Content**: Click the **"🚀 Generate"** button
   - The app will use both OpenAI and Anthropic to generate documentation
   - It will automatically search for web resources and videos

3. **Review Results**:
   - **Generated Documentation**: Main content in the left column
   - **Web References**: Curated links in the right sidebar
   - **Video Guides**: Relevant YouTube videos
   - **Generation Details**: Processing time and AI engine used

4. **Version History**: Access previous versions from the sidebar

### Advanced Features

- **Multi-Provider Comparison**: The app generates content from both providers and selects the most comprehensive version
- **Automatic Deduplication**: Web search results are automatically deduplicated
- **Error Handling**: Graceful error messages if API keys are invalid or services are unavailable

## 🏗️ Architecture

### Components

1. **SageLensSystem Class**
   - Initializes API clients for OpenAI, Anthropic, Tavily, and Serper
   - Handles content generation from multiple providers
   - Manages web and video search

2. **Content Generation**
   - Parallel generation from OpenAI and Anthropic
   - Automatic selection of best content based on length/comprehensiveness
   - Error handling and fallback mechanisms

3. **Search Integration**
   - Tavily: AI-powered web search
   - Serper: Google search API
   - YouTube Search: Video discovery

## 🔧 Configuration

### Environment Variables

All configuration is done through environment variables in `.env` file:

```env
# Required
OPENAI_API_KEY="your-openai-key"
ANTHROPIC_API_KEY="your-anthropic-key"

# Optional
TAVILY_API_KEY="your-tavily-key"
SERPER_API_KEY="your-serper-key"
```

### Model Configuration

The app uses:
- **OpenAI**: `gpt-4-turbo` (temperature: 0.3)
- **Anthropic**: `claude-3-5-sonnet-20241022` (max_tokens: 4000)

## 🐛 Troubleshooting

### Issue: "Failed to generate content" error

**Solutions:**
- Verify API keys are correct in `.env` or Streamlit Secrets
- Check that API keys have sufficient credits/quota
- Ensure billing is active for both OpenAI and Anthropic accounts

### Issue: "Search error" messages

**Solutions:**
- Verify Tavily and Serper API keys are set (optional but recommended)
- Check API key permissions and quotas
- The app will continue to work even if search fails

### Issue: Authentication errors (401)

**Solutions:**
- Regenerate API keys in provider dashboards
- Ensure keys are copied correctly (no extra spaces or characters)
- Check that keys are active and not expired

### Issue: App not loading on Streamlit Cloud

**Solutions:**
- Verify `requirements-sage-lens.txt` includes all dependencies
- Check that Python version is 3.9+
- Review build logs for specific errors
- Ensure secrets are configured correctly

## 📊 API Usage & Costs

### Estimated Costs per Generation

- **OpenAI GPT-4 Turbo**: ~$0.01-0.03 per generation (depends on topic length)
- **Anthropic Claude 3.5 Sonnet**: ~$0.015-0.04 per generation
- **Tavily Search**: Free tier available, paid plans start at $99/month
- **Serper API**: Free tier: 2,500 searches/month, then $5/1,000 searches

### Cost Optimization Tips

1. Use specific, focused research topics to reduce token usage
2. Monitor API usage in provider dashboards
3. Consider using GPT-4o-mini for testing (cheaper alternative)
4. Set up usage alerts in provider accounts

## 🔐 Security Best Practices

1. **Never commit API keys** to the repository
2. **Use Streamlit Secrets** for production deployments
3. **Rotate API keys** regularly
4. **Monitor API usage** to detect unauthorized access
5. **Set up rate limiting** if needed
6. **Use environment variables** for local development

## 📝 License

This project is part of the SDLC Agentic AI Platform.

## 🤝 Contributing

Contributions are welcome! Please ensure:
- Code follows PEP 8 style guidelines
- All API keys are kept secure
- Tests are added for new features
- Documentation is updated

## 📞 Support

For issues or questions:
1. Check the troubleshooting section above
2. Review API provider documentation
3. Check Streamlit Cloud deployment logs
4. Verify environment variables are set correctly

## 🎯 Roadmap

- [ ] Add support for more LLM providers (Groq, DeepSeek)
- [ ] Implement caching for repeated queries
- [ ] Add export functionality (PDF, DOCX)
- [ ] Enhanced search result ranking
- [ ] Custom model selection per query
- [ ] Batch processing for multiple topics

---

**Built with ❤️ using Streamlit, OpenAI, and Anthropic**

