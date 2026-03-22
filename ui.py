import streamlit as st
from app.vector_store import FAISSVectorStore
from app.rag_pipeline import run_rag

st.set_page_config(page_title="Local RAG Chat", layout="wide")

st.title("💬 Local RAG Assistant")

# load index once
@st.cache_resource
def load_store():
    store = FAISSVectorStore(dimension=384)
    store.load()
    return store

store = load_store()

query = st.text_input("Ask your data:")

if query:
    st.write("### 🤖 Answer")
    run_rag(query, store)
