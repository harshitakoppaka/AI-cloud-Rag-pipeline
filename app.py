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

        # Loading spinner
        with st.spinner("Thinking..."):
            answer = ask_question(user_input)

        st.markdown("### Answer:")
        st.write(answer)

    else:
        st.warning("Please enter a question.")
