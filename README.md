# 🔬 Sage Lens - Multi Agent Orchestration Deep Research Agentic AI System

> **Research anything, anywhere using orchestrated multi-agent AI intelligence**

Sage Lens is an advanced agentic AI research platform that orchestrates multiple specialized agents to conduct comprehensive deep research across the web, synthesize information, and produce curated, publication-ready content.

## 🌟 Key Features

### 🤖 Multi-Agent Orchestration
- **Orchestrator Agent**: Coordinates the entire research workflow
- **Research Agent**: Conducts deep research and synthesis
- **Content Agent**: Refines and polishes content to publication standards
- **Analysis Agent**: Provides strategic insights and critical evaluation
- **Web Crawler Agents**: Simultaneously search multiple sources

### 🔍 Multi-Source Intelligence
- **Tavily AI Search**: Semantic web search with AI-powered ranking
- **Serper Google Search**: Comprehensive web coverage with knowledge graph
- **YouTube Search**: Video content discovery with popularity ranking
- **Parallel Processing**: All sources searched simultaneously

### 🧠 Multi-Provider AI
- **OpenAI GPT-4 Turbo**: Advanced reasoning and content generation
- **Anthropic Claude 3.5 Sonnet**: Alternative perspective and analysis
- **DeepSeek**: Additional insights and cost-effective generation
- **Intelligent Selection**: Automatically chooses best result

### 📊 Comprehensive Output
- **Research Documents**: Well-structured, comprehensive content
- **Curated References**: Web resources with snippets and links
- **Top Videos**: Ranked by popularity with view counts
- **Deep Analysis**: Strategic insights and implications
- **Performance Metrics**: Processing time and provider information

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- API Keys (see Configuration)

### Installation

```bash
# Clone repository
git clone https://github.com/git-bonda108/sage-lens.git
cd sage-lens

# Install dependencies
pip install -r requirements.txt

# Install OpenAI Agents SDK (optional but recommended)
pip install openai-agents
```

### Configuration

Create a `.env` file:

```env
OPENAI_API_KEY=your-openai-key
ANTHROPIC_API_KEY=your-anthropic-key
DEEPSEEK_API_KEY=your-deepseek-key
TAVILY_API_KEY=your-tavily-key
SERPER_API_KEY=your-serper-key
```

### Run

```bash
streamlit run sage_lens_enhanced.py
```

Access at `http://localhost:8501`

## 🔄 How It Works

### Orchestration Workflow

1. **Information Gathering**
   - Orchestrator receives research query
   - Web crawler agents search Tavily, Serper, and YouTube in parallel
   - All information collected simultaneously

2. **Content Generation**
   - Research Agent analyzes and synthesizes findings
   - Content Agent refines to publication quality
   - Multiple AI providers generate content in parallel

3. **Analysis & Refinement**
   - Analysis Agent provides deep insights
   - Identifies patterns, trends, and implications
   - Highlights critical considerations

4. **Curation & Presentation**
   - Resources deduplicated and ranked
   - Videos sorted by popularity
   - Comprehensive metrics provided

## 🎯 Agent Specializations

### Research Agent
- Conducts comprehensive research on any topic
- Synthesizes information from multiple sources
- Generates well-structured documentation
- Cites sources appropriately

### Content Agent
- Transforms research into polished content
- Ensures clarity and readability
- Maintains accuracy while improving presentation
- Creates publication-ready output

### Analysis Agent
- Analyzes research for key insights
- Identifies patterns and trends
- Provides critical evaluation
- Suggests implications and applications

## 📚 Use Cases

- **Academic Research**: Comprehensive literature reviews and analysis
- **Market Research**: Industry trends and competitive analysis
- **Technical Documentation**: In-depth technical guides and tutorials
- **Content Creation**: Research-backed articles and blog posts
- **Business Intelligence**: Strategic insights and recommendations

## 🛠️ Technology Stack

- **Framework**: Streamlit
- **AI SDK**: OpenAI Agents SDK
- **LLM Providers**: OpenAI, Anthropic, DeepSeek
- **Search APIs**: Tavily, Serper, YouTube
- **Language**: Python 3.9+

## 📖 Documentation

- **Workflow Tab**: Detailed explanation of the orchestration process
- **API Documentation**: See individual provider documentation
- **Deployment Guide**: See `DEPLOYMENT_INSTRUCTIONS.md`

## 🔐 Security

- API keys stored in environment variables
- Never commit `.env` files
- Secure API key handling
- No data persistence

## 🤝 Contributing

Contributions welcome! Please ensure:
- Code follows PEP 8 style guidelines
- All API keys are kept secure
- Tests are added for new features
- Documentation is updated

## 📝 License

This project is part of the Sage Lens research platform.

## 🔗 Links

- **GitHub**: https://github.com/git-bonda108/sage-lens
- **Issues**: https://github.com/git-bonda108/sage-lens/issues

## 🙏 Acknowledgments

Built with:
- OpenAI Agents SDK
- Streamlit
- Tavily AI
- Serper.dev
- Anthropic Claude
- DeepSeek

---

**Built with ❤️ for comprehensive research and knowledge discovery**
