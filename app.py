import streamlit as st
from rag.query_rag import ask_question

st.set_page_config(
    page_title="Cloud Architecture RAG Assistant",
    page_icon="☁️",
    layout="centered"
)

st.title("Cloud Architecture RAG Assistant")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input box
if prompt := st.chat_input("Ask a cloud architecture question..."):

    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            answer, retrieved_chunks = ask_question(prompt)

        st.markdown(answer)

    # Save assistant message
    st.session_state.messages.append({"role": "assistant", "content": answer})
