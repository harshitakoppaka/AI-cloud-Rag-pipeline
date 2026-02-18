import streamlit as st
import os
from rag.query_rag import ask_question
from embeddings.generate_embeddings import create_faiss_index

st.set_page_config(
    page_title="Cloud Architecture RAG Assistant",
    page_icon="☁️",
    layout="centered"
)

st.title("Cloud Architecture RAG Assistant")

# -------- PDF Upload Section --------

uploaded_file = st.file_uploader("Upload a PDF document", type=["pdf"])

if uploaded_file is not None:

    os.makedirs("data", exist_ok=True)

    # Save uploaded file
    file_path = "data/uploaded.pdf"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success("PDF uploaded successfully.")

    # Remove old index if exists
    if os.path.exists("data/vector.index"):
        os.remove("data/vector.index")
    if os.path.exists("data/chunks.pkl"):
        os.remove("data/chunks.pkl")

    with st.spinner("Processing and indexing document..."):
        create_faiss_index()

    st.success("Document indexed successfully.")

# -------- Chat Memory --------

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -------- Chat Input --------

if prompt := st.chat_input("Ask a question about your document..."):

    # Store user message
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate answer
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            answer, retrieved_chunks = ask_question(
                prompt,
                chat_history=st.session_state.messages
            )

        st.markdown(answer)

    # Store assistant response
    st.session_state.messages.append({"role": "assistant", "content": answer})
