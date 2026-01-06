import pandas as pd
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from pathlib import Path

def generate_embeddings():
    # Load processed data
    data_path = Path("data/sample_flights.csv")
    df = pd.read_csv(data_path)

    # Create text (same as processing step)
    texts = df.apply(
        lambda row: f"Flight {row.flight_id} by {row.airline} was delayed due to {row.delay_reason} for {row.delay_minutes} minutes.",
        axis=1
    ).tolist()

    # Load embedding model
    model = SentenceTransformer("all-MiniLM-L6-v2")

    # Generate embeddings
    embeddings = model.encode(texts)

    # Create FAISS index
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))

    # Save index
    faiss.write_index(index, "data/vector.index")

    print("✅ Embeddings generated and FAISS index saved")
    print(f"Total vectors: {index.ntotal}")

if __name__ == "__main__":
    generate_embeddings()
