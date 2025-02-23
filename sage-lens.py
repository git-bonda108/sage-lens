import os
import time
import requests
import streamlit as st
from openai import OpenAI
from tavily import TavilyClient
from youtube_search import YoutubeSearch
from dotenv import load_dotenv
import anthropic

load_dotenv()


class SageLensSystem:
    def __init__(self):
        try:
            self.llms = {
                "openai": OpenAI(api_key=os.getenv("OPENAI_API_KEY")),
                "anthropic": anthropic.Anthropic(
                    api_key=os.getenv("ANTHROPIC_API_KEY")
                )
            }
            self.tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
            self.serper_config = {
                "url": "https://google.serper.dev/search",
                "headers": {"X-API-KEY": os.getenv("SERPER_API_KEY")},
                "timeout": 10
            }
        except Exception as e:
            st.error(f"Initialization failed: {str(e)}")
            raise

    def _search_web(self, query: str) -> list:
        all_results = []
        try:
            # Tavily Search
            tavily_results = self.tavily.search(query=query, max_results=5)
            all_results.extend([
                {"title": r.get("title", "Untitled"), "url": r["url"]}
                for r in tavily_results.get("results", []) if "url" in r
            ])

            # Google Serper
            response = requests.post(**self.serper_config, json={"q": query, "num": 5})
            serper_results = response.json()
            all_results.extend([
                {"title": r.get("title", "Untitled"), "url": r["link"]}
                for r in serper_results.get("organic", []) if "link" in r
            ])

            # Deduplicate
            seen = set()
            return [x for x in all_results if not (x["url"] in seen or seen.add(x["url"]))][:10]
        except Exception as e:
            st.error(f"Search error: {str(e)}")
            return []

    def _search_videos(self, query: str) -> list:
        try:
            results = YoutubeSearch(query, max_results=10).to_dict()
            return [{
                "title": r.get("title", "Untitled Video"),
                "url": f"https://youtube.com/watch?v={r['id']}",
                "views": r.get("views", "N/A")
            } for r in results if 'id' in r][:5]
        except Exception as e:
            st.error(f"Video search error: {str(e)}")
            return []

    def _generate_content(self, provider: str, prompt: str) -> dict:
        try:
            start_time = time.time()
            if provider == "anthropic":
                response = self.llms[provider].messages.create(
                    model="claude-3-5-sonnet-20241022",
                    max_tokens=4000,
                    messages=[
                        {"role": "user", "content": f"Generate comprehensive documentation about: {prompt}"}]
                )
                return {
                    "content": response.content[0].text,
                    "provider": "Claude-3.5-Sonnet",
                    "latency": time.time() - start_time
                }
            else:
                response = self.llms["openai"].chat.completions.create(
                    model="gpt-4-turbo",
                    messages=[{"role": "user", "content": f"Create detailed documentation about: {prompt}"}],
                    temperature=0.3
                )
                return {
                    "content": response.choices[0].message.content,
                    "provider": "OpenAI-GPT4",
                    "latency": time.time() - start_time
                }
        except Exception as e:
            st.error(f"{provider} error: {str(e)}")
            return None

    def process_query(self, topic: str) -> dict:
        result = {"content": "", "references": {"web": [], "videos": []}}
        try:
            versions = []
            for provider in ["openai", "anthropic"]:
                if content := self._generate_content(provider, topic):
                    versions.append(content)
            if versions:
                result["content"] = max(versions, key=lambda x: len(x["content"]))
                result["references"]["web"] = self._search_web(topic)
                result["references"]["videos"] = self._search_videos(topic)
        except Exception as e:
            st.error(f"Processing error: {str(e)}")
        return result


def main():
    st.set_page_config(
        page_title="Sage-Lens",
        layout="wide",
        page_icon="🔍",
        initial_sidebar_state="expanded"
    )

    # Custom styling
    st.markdown("""
        <style>
        .main {background-color: #f9f9f9;}
        .stTextArea textarea {min-height: 150px; border-radius: 10px;}
        .stButton>button {border-radius: 8px; padding: 10px 24px;}
        .stExpander {border: 1px solid #e0e0e0; border-radius: 8px;}
        </style>
    """, unsafe_allow_html=True)

    # Header section
    st.title("🔍 Sage-Lens: Agentic AI Research Engine")
    st.markdown("### Your AI-Powered Research Companion")
    st.write("---")

    # Initialize session state
    if 'history' not in st.session_state:
        st.session_state.history = []
    if 'current_result' not in st.session_state:
        st.session_state.current_result = None

    # Main input section
    with st.container():
        input_col, btn_col = st.columns([5, 1])
        with input_col:
            topic = st.text_area(
                "📝 Enter Research Topic:",
                placeholder="e.g., Transformer Architecture Optimization",
                help="Describe your topic in detail"
            )
        with btn_col:
            st.write("")
            st.write("")
            if st.button("🚀 Generate", use_container_width=True):
                if topic.strip():
                    with st.spinner("🔬 Agentic AI processors analyzing..."):
                        st.session_state.current_result = SageLensSystem().process_query(topic)
                        if st.session_state.current_result["content"]:
                            st.session_state.history.append(st.session_state.current_result)
                            st.rerun()

    # Results display
    if st.session_state.current_result:
        result = st.session_state.current_result

        # Main content columns
        doc_col, ref_col = st.columns([3, 1])

        with doc_col:
            # Documentation display
            with st.expander("📄 Generated Documentation", expanded=True):
                st.markdown(result["content"]["content"], unsafe_allow_html=True)

            # Generation metrics
            with st.expander("⚙️ Generation Details"):
                cols = st.columns(2)
                cols[0].metric("Processing Time", f"{result['content']['latency']:.2f}s")
                cols[1].metric("AI Engine", result['content']['provider'])
                st.caption("Powered by Claude-3.5-Sonnet and GPT-4 Turbo")

        with ref_col:
            # Reference materials
            with st.container(border=True):
                st.subheader("🔗 Curated Resources")

                # Web results
                with st.expander("🌐 Web References", expanded=True):
                    if result["references"]["web"]:
                        for i, item in enumerate(result["references"]["web"][:5], 1):
                            st.markdown(f"{i}. [{item['title']}]({item['url']})")
                    else:
                        st.info("No web resources found")

                # Video results
                with st.expander("🎥 Video Guides"):
                    if result["references"]["videos"]:
                        for vid in result["references"]["videos"][:3]:
                            st.markdown(f"▶️ [{vid['title']}]({vid['url']})")
                            st.caption(f"Views: {vid.get('views', 'N/A')}")
                    else:
                        st.info("No video guides found")

            # Version history
            with st.expander("🕰 Document Versions"):
                if len(st.session_state.history) > 1:
                    for i, rev in enumerate(st.session_state.history):
                        cols = st.columns([1, 3])
                        cols[0].button(
                            f"v{i + 1}",
                            key=f"load_{i}",
                            on_click=lambda r=rev: st.session_state.update(current_result=r),
                            help=f"Load version {i + 1}"
                        )
                        cols[1].caption(f"{rev['content']['provider']} | {rev['content']['latency']:.1f}s")
                else:
                    st.info("No previous versions")


if __name__ == "__main__":
    main()
