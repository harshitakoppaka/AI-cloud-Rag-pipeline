import faiss
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer

# Load data
df = pd.read_csv("data/sample_flights.csv")

# Load vector index
index = faiss.read_index("data/vector.index")

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

def ask_question(question, top_k=3):
    query_vector = model.encode([question])
    distances, indices = index.search(np.array(query_vector), top_k)

    print(f"\nQuestion: {question}\n")
    print("Top results:\n")

    for i in indices[0]:
        row = df.iloc[i]
        print(
            f"Flight {row['flight_id']} delayed by {row['delay_minutes']} minutes "
            f"due to {row['delay_reason']}"
        )

if __name__ == "__main__":
    question = "Why were flights delayed?"
    ask_question(question)
