import faiss
import pickle
import numpy as np
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

INDEX_PATH = "data/vector.index"
CHUNKS_PATH = "data/chunks.pkl"

from embeddings.generate_embeddings import create_faiss_index

def load_index():
    # If index doesn't exist, create it
    if not os.path.exists(INDEX_PATH) or not os.path.exists(CHUNKS_PATH):
        print("Index not found. Creating embeddings...")
        create_faiss_index()

    index = faiss.read_index(INDEX_PATH)
    with open(CHUNKS_PATH, "rb") as f:
        chunks = pickle.load(f)

    return index, chunks


def embed_query(query):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=query
    )
    return np.array(response.data[0].embedding).astype("float32")

def ask_question(question, top_k=3):
    index, chunks = load_index()

    query_vector = embed_query(question).reshape(1, -1)
    distances, indices = index.search(query_vector, top_k)

    retrieved_chunks = [chunks[i] for i in indices[0]]
    context = "\n\n".join(retrieved_chunks)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a cloud architecture assistant. Answer only from the provided context."},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {question}"}
        ]
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    question = input("Ask your cloud architecture question: ")
    answer = ask_question(question)
    print("\nAnswer:\n")
    print(answer)
