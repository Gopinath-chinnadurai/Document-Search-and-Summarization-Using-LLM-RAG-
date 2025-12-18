import streamlit as st
import os
import numpy as np

from document_loader import load_txt, load_pdf
from chunker import chunk_text
from embeddings import get_embedding
from vector_store import VectorStore
from summarize import summarize_text
from rag_pipeline import answer_question
from config import TOP_K

st.set_page_config(page_title="RAG Document Search & Summarization")

st.title("RAG Document Search & Summarization")

mode = st.radio(
    "Choose Mode:",
    ["Upload & ask from your document","Ask from existing documents"]
)

# ---------------- MODE 1 ----------------
if mode == "Ask from existing documents":

    st.subheader(" Ask from existing knowledge base")
    st.caption(
        "Topics: Machine Learning, Deep Learning, NLP, LLMs, RAG, Transformers, "
        "Reinforcement Learning, Computer Vision, Recommendation Systems, Ethics in AI"
    )

    query = st.text_input("Type your question:")

    if query:
        all_text = ""
        for file in os.listdir("data"):
            all_text += load_txt(f"data/{file}")

        chunks = chunk_text(all_text)
        embeddings = [get_embedding(c) for c in chunks]

        store = VectorStore(len(embeddings[0]))
        store.add(np.array(embeddings).astype("float32"), chunks)

        answer = answer_question(query, store)

        st.subheader("Answer")
        st.write(answer)

# ---------------- MODE 2 ----------------
if mode == "Upload & ask from your document":

    st.subheader(" Upload PDF (Max 200 KB)")
    pdf = st.file_uploader("Upload your document", type=["pdf"])

    if pdf:
        text = load_pdf(pdf)

        chunks = chunk_text(text)
        embeddings = [get_embedding(c) for c in chunks]

        store = VectorStore(len(embeddings[0]))
        store.add(np.array(embeddings).astype("float32"), chunks)

        st.success("Document indexed successfully!")

        st.subheader("Document Summary")
        st.write(summarize_text(text, 5))

        question = st.text_input("Ask a question from this document:")

        if question:
            answer = answer_question(question, store)
            st.subheader("Answer")
            st.write(answer)
