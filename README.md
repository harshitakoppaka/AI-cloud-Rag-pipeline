# AI-Enabled Cloud Data Pipeline with RAG

This project demonstrates an end-to-end **AI-enabled cloud-style data pipeline** that uses **Retrieval-Augmented Generation (RAG)** to answer natural language questions from structured data.

The goal of this project is to show how data engineering pipelines can be combined with modern AI techniques such as embeddings and vector search.

---

##  What This Project Does

1. Ingests structured flight delay data
2. Generates vector embeddings from the data
3. Stores embeddings in a FAISS vector index
4. Retrieves relevant records based on a natural language query
5. Answers questions like:
   - *Why were flights delayed?*
   - *Which flights had the longest delays?*

---

##  Project Architecture


