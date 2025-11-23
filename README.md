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

## 🚀 Quick Start

### Prerequisites

- Python 3.9+ (recommended: 3.10+)
- API keys for OpenAI and/or Anthropic
- Streamlit (for web interface)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd SDLC
   ```

2. **Install dependencies**
   ```bash
   # For Sage-Lens
   pip install -r requirements-sage-lens.txt
   
   # For SDLC Platform
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
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

