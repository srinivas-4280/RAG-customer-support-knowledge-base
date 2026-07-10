import streamlit as st
from sentence_transformers import SentenceTransformer
from langchain_community.vectorstores import FAISS

st.set_page_config(
    page_title="FAST RAG App",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for UI improvement
st.markdown(
    """
<style>
    .main-header {
        text-align: center;
        color: #1E3A8A;
        font-weight: bold;
        padding-top: 1rem;
        padding-bottom: 0.5rem;
    }
    .sub-header {
        text-align: center;
        color: #6B7280;
        margin-bottom: 2rem;
        font-size: 1.1rem;
    }
    .result-card {
        background-color: #f8fafc;
        border-left: 5px solid #3b82f6;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 15px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    }
    /* Dark mode support for the card */
    @media (prefers-color-scheme: dark) {
        .result-card {
            background-color: #1e293b;
            color: #e2e8f0;
            border-left: 5px solid #60a5fa;
        }
        .main-header {
            color: #60a5fa;
        }
        .sub-header {
            color: #94a3b8;
        }
    }
</style>
""",
    unsafe_allow_html=True,
)

# Sidebar for Help and Information
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712010.png", width=80)
    st.title("💡 How to use")
    st.info(
        "Welcome to the **Customer Support Knowledge Base**! \n\n"
        "1. **Type your question** in the search bar.\n"
        "2. **Wait a second** for the AI to retrieve the most relevant answers.\n"
        "3. **Read the top matches** carefully to resolve your query."
    )
    st.divider()
    st.subheader("Example Questions:")
    st.markdown(
        """
    - *How do I reset my password?*
    - *What is the refund policy?*
    - *How can I track my order?*
    """
    )
    st.divider()
    st.caption("Powered by FAST RAG and Sentence Transformers ⚡")

# Main Page UI
st.markdown(
    '<h1 class="main-header">⚡ Customer Support Knowledge Base</h1>',
    unsafe_allow_html=True,
)
st.markdown(
    '<p class="sub-header">Instantly find answers from our support documentation using AI-powered search.</p>',
    unsafe_allow_html=True,
)


# 1. Load local embedding model (NO HF download)
@st.cache_resource
def load_embedder():
    return SentenceTransformer("all-MiniLM-L6-v2")


embedder = load_embedder()


# 2. Embedding wrapper (MAKES IT CALLABLE)
class EmbeddingWrapper:
    def __call__(self, text):
        # when FAISS calls embedding_function(text)
        return embedder.encode([text], convert_to_numpy=True)[0]

    def embed_documents(self, texts):
        return embedder.encode(texts, convert_to_numpy=True)

    def embed_query(self, text):
        return embedder.encode([text], convert_to_numpy=True)[0]


embedding_fn = EmbeddingWrapper()


# 3. Load FAISS DB
@st.cache_resource
def load_faiss():
    return FAISS.load_local(
        "models/vector_store",
        embeddings=embedding_fn,
        allow_dangerous_deserialization=True,
    )


vector_store = load_faiss()

st.divider()

# 4. UI Input
col1, col2, col3 = st.columns([1, 6, 1])
with col2:
    query = st.text_input(
        "Ask a question from the documents:",
        placeholder="E.g., How do I contact billing support?",
        help="Type any question related to customer support.",
    )

# 5. Search
if query:
    with st.spinner("🤖 Searching through the knowledge base..."):
        results = vector_store.similarity_search(query, k=3)

    st.subheader("📌 Top Answers:")
    if results:
        for i, res in enumerate(results, start=1):
            st.markdown(
                f"""
            <div class="result-card">
                <strong style="color: #3b82f6;">Result {i}</strong><br><br>
                {res.page_content}
            </div>
            """,
                unsafe_allow_html=True,
            )
    else:
        st.warning("No relevant answers found. Please try rephrasing your question.")
else:
    # Empty state UI
    st.markdown(
        "<div style='text-align: center; color: gray; margin-top: 40px;'>"
        "<h4>Search above to get instant answers. 🚀</h4>"
        "</div>",
        unsafe_allow_html=True,
    )
