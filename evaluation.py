from document_loader import load_txt
from chunker import chunk_text
from embeddings import get_embedding
from vector_store import VectorStore
from rag_pipeline import answer_question
import numpy as np
import os

def evaluate():
    corpus = ""
    for file in os.listdir("data"):
        corpus += load_txt(f"data/{file}")

    chunks = chunk_text(corpus)
    embeddings = [get_embedding(c) for c in chunks]

    store = VectorStore(len(embeddings[0]))
    store.add(np.array(embeddings), chunks)

    queries = [
        "What is machine learning?",
        "Explain NLP",
        "What is RAG?"
    ]

    for q in queries:
        print(f"\nQ: {q}")
        print("A:", answer_question(q, store))

if __name__ == "__main__":
    evaluate()
