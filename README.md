# ☁️ AI Cloud Architecture RAG Assistant

🔗 **Live App:**  
https://ai-cloud-rag-pipeline-8he2klpk9j6yu3rarifrwk.streamlit.app/

---

# AI Cloud RAG Pipeline  
Retrieval-Augmented Generation (RAG) system with document ingestion, semantic search, and conversational memory.

---

## Overview

This project implements an end-to-end Retrieval-Augmented Generation (RAG) pipeline that allows users to upload documents and query them using a large language model.

The system combines:

- Document ingestion and preprocessing  
- Embedding-based semantic retrieval  
- Vector similarity search  
- Context-aware response generation  
- Conversational memory  
- Streamlit-based user interface  

The goal is to build a modular and scalable RAG architecture suitable for AI-powered document intelligence systems.

---

## Architecture

The pipeline follows a structured flow:

1. **Document Ingestion**  
   Uploaded PDFs are parsed and split into smaller text chunks.

2. **Embedding Generation**  
   Each chunk is converted into vector embeddings.

3. **Vector Storage & Retrieval**  
   Embeddings are stored in a vector database for similarity-based search.

4. **Query Processing (RAG Core)**  
   - User query is embedded  
   - Top-k similar document chunks are retrieved  
   - Retrieved chunks are combined into contextual input  

5. **Response Generation**  
   The language model generates a context-aware response.

6. **Conversational Memory**  
   Maintains prior interactions to enable multi-turn conversations.

---

## Project Structure

```
AI-cloud-Rag-pipeline/
│
├── api/                # API logic and RAG orchestration
├── ingestion/          # Document loading and preprocessing
├── embeddings/         # Embedding generation utilities
├── processing/         # Vector store + LLM interaction
├── rag/                # Core RAG query logic
│
├── data/               # Sample or uploaded documents
├── app.py              # Streamlit application entry point
├── requirements.txt    # Dependencies
├── Dockerfile          # AWS deployment configuration
└── README.md
```

---

## Core RAG Implementation

The core retrieval logic is structured through a `RAGPipeline` class responsible for:

- Query embedding
- Semantic retrieval
- Context construction
- LLM response generation

Example usage:

```python
from rag.rag import RAGPipeline

rag = RAGPipeline(top_k=3)
response = rag.generate_answer("What are the key findings?")
print(response)
```

---

## Features

- Modular pipeline design  
- Clean separation of ingestion, embedding, retrieval, and generation  
- Conversational memory support  
- Streamlit UI for interactive querying  
- Docker support for deployment  
- AWS-ready configuration  

---

## Installation

Clone the repository:

```
git clone https://github.com/your-username/AI-cloud-Rag-pipeline.git
cd AI-cloud-Rag-pipeline
```

Create a virtual environment:

```
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Run the Application

Start the Streamlit app:

```
streamlit run app.py
```

Upload a document and begin querying through the interface.

---

## Deployment

This project includes a Dockerfile for containerized deployment and is structured for cloud deployment environments such as AWS.

Build Docker image:

```
docker build -t rag-pipeline .
```

Run container:

```
docker run -p 8501:8501 rag-pipeline
```

---

## Future Improvements

- Add persistent vector database support  
- Improve streaming response handling  
- Add authentication and user session management  
- Optimize chunking and retrieval strategies  
- Integrate monitoring and logging  

---

## License

This project is for educational and research purposes.