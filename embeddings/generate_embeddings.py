import faiss
import numpy as np
import os
import pickle
from openai import OpenAI
from dotenv import load_dotenv
from ingestion.ingest_data import load_documents
from processing.chunk_text import chunk_text

# Load environment variables
load_dotenv()

# Debug: Check if API key is loading
print("API KEY LOADED:", os.getenv("OPENAI_API_KEY"))

# Initialize OpenAI client
client = OpenAI()

INDEX_PATH = "data/vector.index"
CHUNKS_PATH = "data/chunks.pkl"

def create_faiss_index():

    print("Loading documents...")
    documents = load_documents()
    print(f"Loaded {len(documents)} documents successfully.")

    print("Chunking documents...")
    all_chunks = []
    for doc in documents:
        chunks = chunk_text(doc)
        all_chunks.extend(chunks)

    print(f"Total chunks created: {len(all_chunks)}")

    print("Generating embeddings...")
    embeddings = []

    for chunk in all_chunks:
        response = client.embeddings.create(
            model="text-embedding-3-small",
            input=chunk
        )
        embeddings.append(response.data[0].embedding)

    embeddings = np.array(embeddings).astype("float32")

    print("Building FAISS index...")
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    print("Saving index and chunks...")
    faiss.write_index(index, INDEX_PATH)

    with open(CHUNKS_PATH, "wb") as f:
        pickle.dump(all_chunks, f)

    print("FAISS index created successfully.")

if __name__ == "__main__":
    create_faiss_index()
