# Document Search and Summarization Using LLM (RAG)

### Project Overview

This project implements a **Document Search and Summarization System** using a **Retrieval-Augmented Generation (RAG)** approach.
Generate concise summaries using a **Large Language Model (LLaMA 3 via Ollama)**.

<img width="990" height="569" alt="RAG_Doc_Summarize_UI" src="https://github.com/user-attachments/assets/d50be2bb-449e-4117-9d84-84bc0a07a862" />

**The system allows users to:**

- Upload their own document (PDF ≤ 200 KB) and:

      Get an automatic summary

      Ask context-aware questions from the uploaded document

- Ask questions from a preloaded knowledge base (AI-related documents)

    Supported topics are Machine Learning, Deep Learning, Natural Language Processing (NLP), Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), Transformers, Reinforcement Learning, Computer Vision, Recommendation Systems, Ethics in AI

## The project uses:

- Vector embeddings

- FAISS vector database

- Large Language Model (LLaMA 3 via Ollama)

- Streamlit for UI

**This design ensures grounded answers, reduced hallucinations, and scalable retrieval.**

## End-to-End Workflow

    Documents (TXT / PDF)
        ↓
    Text Chunking
        ↓
    Embedding Generation
        ↓
    FAISS Vector Store
        ↓
    Similarity Search (Top-K)
        ↓
    LLM Prompt with ONLY Retrieved Context
        ↓
    Final Answer / Summary

## Objectives

- Efficiently search across a document corpus

- Retrieve the most relevant text using semantic similarity

- Generate accurate summaries using an LLM

- Support document upload + question answering

- Provide a simple, interactive UI

- Demonstrate a real-world RAG pipeline

## Installation & Setup

**1. Prerequisites**

- Python 3.10+
   
- Ollama installed
    https://ollama.com

 **Pull required models:**
    
     ollama pull llama3
    
     ollama pull nomic-embed-text 

**2. Clone the Repository**

     git clone https://github.com/Gopinath-chinnadurai/Document-Search-and-Summarization-Using-LLM-RAG-.git

     cd Document-Search-and-Summarization-Using-LLM-RAG-

**3. Install Dependencies**

     pip install -r requirements.txt

**4. Running the Application**

     streamlit run app.py

**The app will open automatically in your browser:**

## Application Features

**Mode 1: Upload & Ask from Your Document**

- Upload PDF (≤ 200 KB)

- Automatic document summarization

- Ask follow-up questions based on uploaded content

- Conversational and context-aware

**Example:**

     Upload: Resume.pdf
     Summary shown
     Question: What is the education background?
     Answer: Bachelor of Science in Computer Science...

**Mode 2: Ask from Existing Knowledge Base**

- Ask questions related to the 10 AI topics

**Uses:**

    Chunking

    Vector embeddings

    FAISS similarity search

    LLM answer generation

*Answers are grounded in the stored documents*

**Example:**

    Question: What is NLP?
    Answer: Natural Language Processing (NLP) is a field of AI that enables machines to understand and generate human language...  

## Why This Is a RAG System?

**This project strictly follows the RAG pipeline:**

**1. Retrieve**

- Documents are chunked and stored as vectors in FAISS

- Relevant chunks are retrieved using semantic similarity

**2. Augment**

- Retrieved text is injected into the LLM prompt as context

**3. Generate**

- LLM generates answers only from retrieved context

- If information is missing, it responds:

         Not found in the document

**This approach:**

- Reduces hallucinations

- Improves factual accuracy

- Works with private documents
    
## Scalability & Efficiency

- FAISS enables fast similarity search

- Easily extendable to thousands of documents

- Chunk-based indexing

- Local LLM inference via Ollama (no API cost)

- Modular and production-friendly code

## Deployment Note

Streamlit Cloud does not support Ollama
This project must be run locally or on a VM/server with Ollama installed.

## Conclusion

**This project demonstrates:**

- Practical use of LLMs

- Strong Information Retrieval fundamentals

- Real-world RAG architecture

- Clean, modular Python code

- Interactive and intuitive UI

## Author

**Gopinath Chinnadurai**

**GitHub:**
     
     https://github.com/Gopinath-chinnadurai
