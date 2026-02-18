import faiss
import numpy as np
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI()

def retrieve(query, index, chunks, top_k=3):
    # Generate embedding for query
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=query
    )

    query_vector = np.array([response.data[0].embedding]).astype("float32")

    # Search FAISS index
    distances, indices = index.search(query_vector, top_k)

    # Return matching chunks
    retrieved_chunks = [chunks[i] for i in indices[0]]
    return retrieved_chunks
