import streamlit as st
from rag.query_rag import ask_question

st.title("Cloud Architecture RAG Assistant")

# Create input box
user_input = st.text_input("Ask a cloud architecture question:")

# Submit button
if st.button("Submit"):
    if user_input.strip() != "":
        answer = ask_question(user_input)
        st.write("### Answer:")
        st.write(answer)
    else:
        st.warning("Please enter a question.")
