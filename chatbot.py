import streamlit as st
#from src.config import CORPUS_PATH
from src.data_loader import load_documents
from src.embedder import embed_text
from src.retriever import add_to_vectorstore, retrieve_relevant_docs
from src.generator import generate_answer

# Run once on startup
@st.cache_resource
def setup_pipeline():
    docs = load_documents("corpus/")
    texts = [doc["content"] for doc in docs]
    embeddings = embed_text(texts)
    add_to_vectorstore(docs, embeddings)
    return docs

# Initial load
with st.spinner("📄 Loading and embedding documents..."):
    setup_pipeline()

# Title
st.title("💬 AI/ML Interview Chatbot")

# Chat history session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat input box
query = st.chat_input("Ask me anything about AI/ML interviews...")

# Process query
if query:
    query_embedding = embed_text([query])[0]
    context_docs = retrieve_relevant_docs(query_embedding)
    answer = generate_answer(query, context_docs)

    # Save chat history
    st.session_state.chat_history.append({"role": "user", "text": query})
    st.session_state.chat_history.append({"role": "bot", "text": answer})

# Display conversation
for chat in st.session_state.chat_history:
    if chat["role"] == "user":
        with st.chat_message("user"):
            st.markdown(chat["text"])
    else:
        with st.chat_message("assistant"):
            st.markdown(chat["text"])

# Optionally show retrieved context
if query:
    with st.expander("📂 Retrieved Chunks"):
        for i, doc in enumerate(context_docs):
            st.markdown(f"**Chunk {i+1}**\n\n{doc[:500]}{'...' if len(doc) > 500 else ''}")
