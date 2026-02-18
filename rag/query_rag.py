import os
import faiss
import pickle
import numpy as np
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client (reads OPENAI_API_KEY from environment)
client = OpenAI()

# Paths
INDEX_PATH = "data/vector.index"
CHUNKS_PATH = "data/chunks.pkl"

# Import embedding creator
from embeddings.generate_embeddings import create_faiss_index


def load_index():
    """
    Load FAISS index and chunks.
    If they don't exist (like on first Streamlit Cloud run),
    automatically create them.
    """

    # Create index if missing
    if not os.path.exists(INDEX_PATH) or not os.path.exists(CHUNKS_PATH):
        print("Index not found. Creating embeddings...")
        create_faiss_index()

    index = faiss.read_index(INDEX_PATH)

    with open(CHUNKS_PATH, "rb") as f:
        chunks = pickle.load(f)

    return index, chunks


def embed_query(query):
    """
    Generate embedding for user query.
    """
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=query
    )

    return np.array(response.data[0].embedding).astype("float32")


def ask_question(question, top_k=3):
    """
    Retrieve relevant chunks and generate final answer.
    """

    index, chunks = load_index()

    # Embed query
    query_vector = embed_query(question).reshape(1, -1)

    # Search FAISS
    distances, indices = index.search(query_vector, top_k)

    retrieved_chunks = [chunks[i] for i in indices[0]]
    context = "\n\n".join(retrieved_chunks)

    # Generate final answer
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a cloud architecture assistant. Answer only using the provided context."
            },
            {
                "role": "user",
                "content": f"Context:\n{context}\n\nQuestion: {question}"
            }
        ]
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    question = input("Ask your cloud architecture question: ")
    answer = ask_question(question)
    print("\nAnswer:\n")
    print(answer)
