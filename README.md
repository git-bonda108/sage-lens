<<<<<<< HEAD
# SDLC Agentic AI Platform

A comprehensive Software Development Life Cycle (SDLC) platform powered by agentic AI, featuring multiple specialized agents for requirements, design, build, integration testing, UAT, and cutover phases.

## 🎯 Projects

### 1. Sage-Lens: AI Research Engine 🔍
**Location**: `sage-lens.py`

A powerful research platform that leverages multiple AI providers to generate comprehensive documentation, curate web resources, and find relevant video guides.

**Quick Start**:
```bash
streamlit run sage-lens.py
```

**Documentation**: See [README_SAGE_LENS.md](README_SAGE_LENS.md)

### 2. SDLC Agentic AI Manager
**Location**: `main_sdlc_agentic_ai.py`, `mcp_sdlc_app.py`

Complete SDLC orchestration platform with specialized agents for each phase.

**Documentation**: See [STREAMLIT_CLOUD_DEPLOYMENT.md](STREAMLIT_CLOUD_DEPLOYMENT.md)
=======
# 🔍 Sage-Lens: Agentic AI Research Engine

**Sage-Lens** is an intelligent, multi-provider AI research platform that generates comprehensive documentation on any topic by leveraging multiple AI models, web search, and video content discovery.

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.32+-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 🌟 Features

### 🤖 Multi-Provider AI Generation
- **OpenAI GPT-4 Turbo**: Fast, reliable content generation
- **Anthropic Claude-3.5 Sonnet**: Advanced reasoning and comprehensive documentation
- **Automatic Best Selection**: Chooses the most comprehensive output

### 🔎 Intelligent Research Capabilities
- **Dual Web Search**: 
  - Tavily API for AI-powered research
  - Google Serper for comprehensive web results
- **Video Discovery**: YouTube search integration for tutorial and guide content
- **Curated References**: Automatically gathers relevant web and video resources

### 📊 Advanced Features
- **Version History**: Track multiple document versions from different AI providers
- **Performance Metrics**: Real-time latency and provider information
- **Session Management**: Maintains research history across sessions
- **Responsive UI**: Clean, modern interface optimized for research workflows
>>>>>>> 63912e8072886598f077c55b6ced6c1ab0884b69

## 🚀 Quick Start

### Prerequisites

<<<<<<< HEAD
- Python 3.9+ (recommended: 3.10+)
- API keys for OpenAI and/or Anthropic
- Streamlit (for web interface)
=======
- Python 3.9 or higher
- API keys for:
  - OpenAI (required)
  - Anthropic (required)
  - Tavily (required)
  - Google Serper (required)
>>>>>>> 63912e8072886598f077c55b6ced6c1ab0884b69

### Installation

1. **Clone the repository**
   ```bash
<<<<<<< HEAD
   git clone <your-repo-url>
   cd SDLC
=======
   git clone https://github.com/git-bonda108/sage-lens.git
   cd sage-lens
>>>>>>> 63912e8072886598f077c55b6ced6c1ab0884b69
   ```

2. **Install dependencies**
   ```bash
<<<<<<< HEAD
   # For Sage-Lens
   pip install -r requirements-sage-lens.txt
   
   # For SDLC Platform
=======
>>>>>>> 63912e8072886598f077c55b6ced6c1ab0884b69
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
<<<<<<< HEAD
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

4. **Run applications**
   ```bash
   # Sage-Lens
   streamlit run sage-lens.py
   
   # SDLC Platform
   streamlit run main_sdlc_agentic_ai.py
   ```

## 📚 Documentation

- **[Sage-Lens Documentation](README_SAGE_LENS.md)** - Complete guide for the AI Research Engine
- **[Deployment Guide](DEPLOYMENT_GUIDE.md)** - Step-by-step Streamlit Cloud deployment
- **[Streamlit Cloud Deployment](STREAMLIT_CLOUD_DEPLOYMENT.md)** - SDLC Platform deployment guide
- **[API Keys Reference](API_KEYS_QUICK_REFERENCE.md)** - Quick reference for required API keys

## 🔑 API Keys Required

### Sage-Lens
- `OPENAI_API_KEY` (Required)
- `ANTHROPIC_API_KEY` (Required)
- `TAVILY_API_KEY` (Optional)
- `SERPER_API_KEY` (Optional)

### SDLC Platform
- `OPENAI_API_KEY` (Required)
- `ANTHROPIC_API_KEY` (Optional)
- `GROK_API_KEY` (Optional)
- `DEEPSEEK_API_KEY` (Optional)

See [API_KEYS_QUICK_REFERENCE.md](API_KEYS_QUICK_REFERENCE.md) for details.

## 🌐 Deployment

### Streamlit Cloud

Both applications can be deployed to Streamlit Cloud:

1. Push code to GitHub
2. Connect repository to Streamlit Cloud
3. Configure secrets (API keys)
4. Deploy!

See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for detailed instructions.

## 🏗️ Architecture

### Sage-Lens
- Multi-provider AI content generation
- Intelligent web search integration
- Video discovery
- Version history tracking

### SDLC Platform
- Agentic AI orchestration
- Phase-specific agents
- Document processing
- Memory and vector storage
- Integration with JIRA, GitHub, Abacus

## 📝 License

This project is part of the SDLC Agentic AI Platform.

## 🤝 Contributing

Contributions are welcome! Please ensure:
- Code follows PEP 8 style guidelines
- All API keys are kept secure (never commit)
- Tests are added for new features
- Documentation is updated

## 📞 Support

For issues or questions:
1. Check the relevant documentation
2. Review troubleshooting sections
3. Check API provider documentation
4. Verify environment variables

---

**Built with ❤️ using Streamlit, OpenAI, Anthropic, and AutoGen**
=======
   
   Create a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=sk-...
   ANTHROPIC_API_KEY=sk-ant-...
   TAVILY_API_KEY=tvly-...
   SERPER_API_KEY=...
   ```

4. **Run the application**
   ```bash
   streamlit run sage-lens.py
   ```

5. **Access the app**
   
   Open your browser to `http://localhost:8501`

## 📋 API Keys Required

### Essential API Keys

| API Key | Purpose | Where to Get | Required |
|---------|---------|--------------|----------|
| `OPENAI_API_KEY` | GPT-4 Turbo content generation | [OpenAI Platform](https://platform.openai.com/api-keys) | ✅ Yes |
| `ANTHROPIC_API_KEY` | Claude-3.5 Sonnet content generation | [Anthropic Console](https://console.anthropic.com/settings/keys) | ✅ Yes |
| `TAVILY_API_KEY` | AI-powered web research | [Tavily](https://tavily.com) | ✅ Yes |
| `SERPER_API_KEY` | Google search results | [Serper.dev](https://serper.dev) | ✅ Yes |

### Getting Your API Keys

1. **OpenAI API Key**
   - Visit https://platform.openai.com/api-keys
   - Sign up or log in
   - Create a new API key
   - Copy the key (starts with `sk-`)

2. **Anthropic API Key**
   - Visit https://console.anthropic.com/settings/keys
   - Sign up or log in
   - Create a new API key
   - Copy the key (starts with `sk-ant-`)

3. **Tavily API Key**
   - Visit https://tavily.com
   - Sign up for an account
   - Navigate to API keys section
   - Create and copy your API key

4. **Serper API Key**
   - Visit https://serper.dev
   - Sign up for an account
   - Get your API key from the dashboard
   - Copy the key

## 🎯 Usage

### Basic Workflow

1. **Enter Research Topic**
   - Type your research topic in the text area
   - Be specific for better results (e.g., "Transformer Architecture Optimization" vs "AI")

2. **Generate Documentation**
   - Click the "🚀 Generate" button
   - Wait for AI processing (typically 5-15 seconds)

3. **Review Results**
   - **Main Documentation**: Comprehensive content generated by AI
   - **Web References**: Curated links to relevant articles and resources
   - **Video Guides**: YouTube tutorials and explanations
   - **Generation Metrics**: Performance and provider information

4. **Version Management**
   - Compare different versions from OpenAI and Anthropic
   - Load previous versions using the version history panel

### Example Topics

- "Machine Learning Model Optimization Techniques"
- "React Hooks Best Practices"
- "Cloud Architecture Patterns for Microservices"
- "Data Science Pipeline Automation"
- "API Security Best Practices"

## 🏗️ Architecture

### System Components

```
┌─────────────────────────────────────────────────┐
│           Streamlit UI Layer                    │
│  (User Input, Results Display, History)        │
└─────────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────────┐
│           SageLensSystem                         │
│  ┌──────────────┐  ┌──────────────┐            │
│  │ AI Providers │  │  Web Search   │            │
│  │ - OpenAI     │  │ - Tavily      │            │
│  │ - Anthropic  │  │ - Serper      │            │
│  └──────────────┘  └──────────────┘            │
│  ┌──────────────┐                               │
│  │ Video Search │                               │
│  │ - YouTube    │                               │
│  └──────────────┘                               │
└─────────────────────────────────────────────────┘
```

### Key Classes

- **`SageLensSystem`**: Main orchestration class
  - Manages AI provider connections
  - Coordinates web and video searches
  - Generates and processes content

### Data Flow

1. User inputs research topic
2. System queries both OpenAI and Anthropic in parallel
3. Web search (Tavily + Serper) runs concurrently
4. YouTube search executes
5. Results are aggregated and displayed
6. Best content version is selected automatically

## 🌐 Streamlit Cloud Deployment

### Prerequisites

- GitHub repository with the code
- Streamlit Cloud account (free tier available)
- All API keys ready

### Deployment Steps

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Prepare for Streamlit Cloud deployment"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Go to https://share.streamlit.io
   - Click "New app"
   - Connect your GitHub repository
   - Select branch: `main`
   - Main file path: `sage-lens.py`

3. **Configure Secrets**
   
   In Streamlit Cloud, go to **Settings → Secrets** and add:
   ```toml
   [secrets]
   OPENAI_API_KEY = "sk-..."
   ANTHROPIC_API_KEY = "sk-ant-..."
   TAVILY_API_KEY = "tvly-..."
   SERPER_API_KEY = "..."
   ```

4. **Deploy**
   - Click "Deploy"
   - Wait for build to complete
   - Access your live app!

### Streamlit Cloud Configuration

The app includes `.streamlit/config.toml` for optimal Cloud deployment:
- Headless server mode
- CORS and XSRF protection
- Optimized theme settings
- Fast reruns enabled

## 🧪 Development

### Local Development Setup

1. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run in development mode**
   ```bash
   streamlit run sage-lens.py --server.headless true
   ```

### Project Structure

```
sage-lens/
├── sage-lens.py          # Main application file
├── requirements.txt      # Python dependencies
├── README.md            # This file
├── .streamlit/
│   └── config.toml      # Streamlit configuration
├── .devcontainer/
│   └── devcontainer.json # VS Code dev container config
└── .env                 # Environment variables (not in git)
```

## 🔧 Configuration

### Environment Variables

All configuration is done via environment variables:

```env
# Required
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
TAVILY_API_KEY=tvly-...
SERPER_API_KEY=...

# Optional (with defaults)
# No optional variables currently
```

### Customization

You can modify the following in `sage-lens.py`:

- **AI Models**: Change models in `_generate_content()` method
  - OpenAI: Currently `gpt-4-turbo`
  - Anthropic: Currently `claude-3-5-sonnet-20241022`

- **Search Results**: Adjust `max_results` parameters
  - Web search: Currently 5 results per provider
  - Video search: Currently 5 results

- **UI Styling**: Modify the CSS in the `main()` function

## 📊 Performance

### Typical Response Times

- **AI Generation**: 5-15 seconds (depending on provider)
- **Web Search**: 2-5 seconds
- **Video Search**: 1-3 seconds
- **Total Processing**: 8-23 seconds

### Optimization Tips

1. **Use specific topics**: More specific queries yield faster, better results
2. **Monitor API usage**: Track your API consumption to avoid rate limits
3. **Cache results**: The app maintains session state for quick access

## 🐛 Troubleshooting

### Common Issues

**Issue**: "Initialization failed" error
- **Solution**: Check that all API keys are set correctly in `.env`

**Issue**: "Search error" messages
- **Solution**: Verify Tavily and Serper API keys are valid and have credits

**Issue**: Slow response times
- **Solution**: Check your internet connection and API provider status

**Issue**: Empty results
- **Solution**: Try a more specific query or check API rate limits

### Debug Mode

To enable debug logging, add this at the top of `sage-lens.py`:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **OpenAI** for GPT-4 Turbo
- **Anthropic** for Claude-3.5 Sonnet
- **Tavily** for AI-powered search
- **Serper** for Google search API
- **Streamlit** for the amazing framework

## 📧 Support

For issues, questions, or contributions:
- Open an issue on [GitHub](https://github.com/git-bonda108/sage-lens/issues)
- Check existing documentation
- Review the code comments for implementation details

## 🗺️ Roadmap

- [ ] Add more AI providers (Gemini, Grok, etc.)
- [ ] Implement result caching
- [ ] Add export functionality (PDF, Markdown)
- [ ] Support for custom prompts
- [ ] Multi-language support
- [ ] Advanced filtering and search options
- [ ] Integration with academic databases
- [ ] Citation management

---

**Made with ❤️ using Streamlit and AI**
>>>>>>> 63912e8072886598f077c55b6ced6c1ab0884b69

