"""
rag.py

Core Retrieval-Augmented Generation (RAG) pipeline logic.
Handles document retrieval and response synthesis.
"""

from typing import List
from embeddings.embedder import get_query_embedding
from processing.vector_store import retrieve_similar_documents
from processing.llm import generate_response


class RAGPipeline:
    def __init__(self, top_k: int = 3):
        self.top_k = top_k

    def retrieve(self, query: str) -> List[str]:
        """
        Retrieve top-k relevant documents based on semantic similarity.
        """
        query_embedding = get_query_embedding(query)
        documents = retrieve_similar_documents(query_embedding, top_k=self.top_k)
        return documents

    def build_context(self, documents: List[str]) -> str:
        """
        Combine retrieved documents into a single context string.
        """
        return "\n\n".join(documents)

    def generate_answer(self, query: str) -> str:
        """
        Full RAG flow: retrieve → build context → generate response.
        """
        documents = self.retrieve(query)
        context = self.build_context(documents)
        response = generate_response(query=query, context=context)
        return response