# AI Cloud RAG Pipeline – Cloud Architecture Knowledge Assistant

This project implements a **Retrieval-Augmented Generation (RAG)** system that enables intelligent querying of **cloud architecture documentation** using **FAISS vector search** and **OpenAI GPT**.

It demonstrates how embeddings and semantic retrieval can be integrated into a cloud-style pipeline to build a context-aware knowledge assistant for system design and architecture documents.

---

## Project Overview

The system allows users to place cloud architecture documents (PDF or TXT) into the `data/` folder and ask natural language questions such as:

- How does auto-scaling work in this architecture?
- What services are used for high availability?
- What security mechanisms are implemented?
- How is fault tolerance handled?

The pipeline retrieves the most relevant document sections and generates grounded answers using GPT.

---

## Architecture Flow

1. **Document Ingestion**  
   Load cloud architecture PDFs or text files from the `data/` directory.

2. **Chunking**  
   Split documents into smaller chunks to improve retrieval accuracy.

3. **Embedding Generation**  
   Generate embeddings for each chunk using OpenAI (`text-embedding-3-small`).

4. **Vector Storage (FAISS)**  
   Store embeddings in a FAISS index for fast similarity search.

5. **Query Retrieval**  
   Embed the user’s question, retrieve the top-k most relevant chunks from FAISS.

6. **Answer Generation (GPT)**  
   Provide retrieved context to GPT (`gpt-4o-mini`) to generate a grounded response.

---

## Tech Stack

- Python  
- OpenAI Embeddings (`text-embedding-3-small`)  
- OpenAI GPT (`gpt-4o-mini`)  
- FAISS (vector similarity search)  
- PyPDF2 (PDF ingestion)  
- NumPy  

---

## Setup

### 1) Install dependencies

```bash
pip install -r requirements.txt
