import streamlit as st
from rag.query_rag import ask_question

# Page configuration
st.set_page_config(
    page_title="Cloud Architecture RAG Assistant",
    page_icon="☁️",
    layout="centered"
)

st.title("Cloud Architecture RAG Assistant")

st.write("Ask a cloud architecture question:")

# User input
user_input = st.text_input(
    "Enter your question:",
    placeholder="What services support high availability in AWS?"
)

# Submit button
if st.button("Submit"):

    if user_input.strip():

        with st.spinner("Thinking..."):
            answer, retrieved_chunks = ask_question(user_input)

        st.markdown("### Answer:")
        st.write(answer)

        st.markdown("---")
        st.markdown("### Retrieved Context")

        for i, chunk in enumerate(retrieved_chunks, 1):
            st.markdown(f"**Chunk {i}:**")
            st.write(chunk)

    else:
        st.warning("Please enter a question.")
