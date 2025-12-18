from ollama import chat
from embeddings import get_embedding
from config import LLM_MODEL
import numpy as np

def answer_question(question, vector_store):
    query_vec = np.array(get_embedding(question))
    contexts = vector_store.search(query_vec)

    context_text = "\n\n".join(contexts)

    prompt = f"""
You are a RAG-based assistant.
Answer STRICTLY using the context below.
If the answer exists, answer clearly.
If not, say: "Answer not found in the provided document."

Context:
{context_text}

Question:
{question}
"""

    response = chat(
        model=LLM_MODEL,
        messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"]
