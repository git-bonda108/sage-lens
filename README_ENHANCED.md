# 🔬 Sage-Lens Enhanced: Agentic AI Research Engine

An advanced research platform powered by OpenAI Agents SDK, featuring multi-agent coordination, deep research capabilities, and an enhanced Streamlit interface.

## ✨ New Features

### 🤖 Agentic AI Capabilities
- **Multi-Agent System**: Three specialized agents working together
  - **Research Agent**: Conducts comprehensive research and synthesis
  - **Content Agent**: Creates polished, publication-ready content
  - **Analysis Agent**: Provides deep insights and strategic analysis
- **Intelligent Workflow**: Agents collaborate to produce superior research outputs
- **Fallback Mode**: Gracefully falls back to standard mode if Agents SDK is unavailable

### 🎨 Enhanced UI/UX
- **Modern Design**: Beautiful gradient styling and improved layout
- **Tabbed Interface**: Organized content display with tabs for Content, References, Analysis, and Metrics
- **Real-time Metrics**: Comprehensive performance tracking
- **Session Management**: Enhanced history tracking and version control
- **Responsive Layout**: Optimized for different screen sizes

### 📊 Additional Features
- **Deep Analysis Tab**: Advanced insights and strategic analysis
- **Enhanced Metrics**: Detailed performance and generation statistics
- **Better Error Handling**: User-friendly error messages with troubleshooting steps
- **Improved Search**: Enhanced web and video search with snippets
- **Version History**: Improved version comparison and loading

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- OpenAI API key (required)
- Optional: Anthropic API key, Tavily API key, Serper API key

### Installation

1. **Clone the repository** (if not already done)
   ```bash
   git clone https://github.com/git-bonda108/sage-lens.git
   cd sage-lens
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install OpenAI Agents SDK** (for agentic features)
   ```bash
   pip install openai-agents
   ```
   
   Note: The application will work without this, but agentic features will be disabled.

4. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=sk-proj-your-key-here
   ANTHROPIC_API_KEY=sk-ant-api03-your-key-here  # Optional
   TAVILY_API_KEY=tvly-dev-your-key-here  # Optional
   SERPER_API_KEY=your-serper-key-here  # Optional
   ```

5. **Run the application**
   ```bash
   python -m streamlit run sage_lens_enhanced.py
   ```
   
   Or using Streamlit directly:
   ```bash
   streamlit run sage_lens_enhanced.py
   ```

6. **Access the app**
   
   Open your browser to `http://localhost:8501`

## 📋 Features Comparison

### Original vs Enhanced

| Feature | Original | Enhanced |
|---------|----------|----------|
| AI Providers | OpenAI + Anthropic | OpenAI + Anthropic + Agents SDK |
| Research Method | Single-pass generation | Multi-agent collaborative research |
| UI Layout | Basic columns | Tabbed interface with modern design |
| Analysis | Basic content | Deep analysis with insights |
| Metrics | Basic | Comprehensive with detailed stats |
| Error Handling | Basic | Enhanced with troubleshooting |
| Version History | Basic | Improved with better UI |

## 🏗️ Architecture

### Agentic Workflow

1. **Research Phase**: Research Agent analyzes the topic and available resources
2. **Content Phase**: Content Agent transforms research into polished content
3. **Analysis Phase**: Analysis Agent provides strategic insights
4. **Integration**: All outputs are combined into a comprehensive result

### Components

- **SageLensAgenticSystem**: Main system class managing agents and tools
- **WebSearchTool**: Handles web search via Tavily and Serper
- **VideoSearchTool**: Handles YouTube video search
- **Agent Classes**: Research, Content, and Analysis agents
- **Streamlit UI**: Enhanced interface with tabs and modern design

## 🔧 Configuration

### Environment Variables

```env
# Required
OPENAI_API_KEY=your-openai-key

# Optional but recommended
ANTHROPIC_API_KEY=your-anthropic-key
TAVILY_API_KEY=your-tavily-key
SERPER_API_KEY=your-serper-key
```

### Agent Configuration

Agents are configured with specific instructions and models. You can modify these in the `_initialize_agents()` method:

- **Research Agent**: Uses GPT-4 Turbo, focused on comprehensive research
- **Content Agent**: Uses GPT-4 Turbo, focused on content quality
- **Analysis Agent**: Uses GPT-4 Turbo, focused on strategic insights

## 📊 Usage Guide

### Basic Usage

1. **Enter Research Topic**: Type your research topic in the text area
2. **Enable Agentic Mode**: Toggle "Use Agentic AI" in the sidebar (if SDK is installed)
3. **Generate**: Click the "🚀 Generate" button
4. **Review Results**: Explore the tabs for Content, References, Analysis, and Metrics

### Advanced Features

- **Version History**: Access previous research versions from the history section
- **Session Stats**: Monitor your usage in the sidebar
- **Clear History**: Reset session data when needed

## 🐛 Troubleshooting

### Issue: "OpenAI Agents SDK not installed"

**Solution**: Install the SDK:
```bash
pip install openai-agents
```

The application will work in standard mode without the SDK.

### Issue: Agent initialization fails

**Solution**: 
- Check that OpenAI API key is valid
- Verify openai-agents package is correctly installed
- Check console for specific error messages
- Application will automatically fall back to standard mode

### Issue: API errors

**Solutions**:
- Verify API keys are correct in `.env` file
- Check API key permissions and quotas
- Ensure billing is active for OpenAI account
- Review error messages for specific issues

## 📈 Performance

### Expected Latency

- **Standard Mode**: 5-15 seconds per query
- **Agentic Mode**: 15-30 seconds per query (more thorough)

### Cost Estimates

- **OpenAI GPT-4 Turbo**: ~$0.01-0.03 per generation
- **Anthropic Claude**: ~$0.015-0.04 per generation
- **Agentic Mode**: ~2-3x standard mode (uses multiple agent calls)

## 🔐 Security

- API keys are never exposed in the UI
- Environment variables are used for local development
- Streamlit Secrets for cloud deployment
- No sensitive data is logged

## 🚀 Deployment

### Streamlit Cloud

1. Push code to GitHub
2. Connect repository to Streamlit Cloud
3. Set main file: `sage_lens_enhanced.py`
4. Configure secrets in Streamlit Cloud settings
5. Deploy!

### Local Production

Use a process manager like `systemd` or `supervisor` to run the Streamlit app as a service.

## 📝 License

This project is part of the Sage-Lens research platform.

## 🤝 Contributing

Contributions welcome! Please ensure:
- Code follows PEP 8 style guidelines
- All API keys are kept secure
- Tests are added for new features
- Documentation is updated

## 📞 Support

For issues or questions:
1. Check the troubleshooting section
2. Review API provider documentation
3. Check GitHub issues
4. Verify environment variables

## 🎯 Roadmap

- [ ] Add more specialized agents (e.g., fact-checker, summarizer)
- [ ] Implement agent handoffs for complex workflows
- [ ] Add guardrails for content validation
- [ ] Export functionality (PDF, DOCX, Markdown)
- [ ] Caching for repeated queries
- [ ] Batch processing for multiple topics
- [ ] Real-time collaboration features

---

**Built with ❤️ using Streamlit, OpenAI Agents SDK, and advanced AI**

