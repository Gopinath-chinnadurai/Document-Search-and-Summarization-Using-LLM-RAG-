# Document Search and Summarization Using LLM (RAG)

### Project Overview

This project implements a Document Search and Summarization System using a Retrieval-Augmented Generation (RAG) approach.
It allows users to uploads the document(200KB) and search across a corpus of AI-related documents and generate concise summaries using a Large Language Model (LLaMA 3 via Ollama).

<img width="990" height="569" alt="RAG_Doc_Summarize_UI" src="https://github.com/user-attachments/assets/d50be2bb-449e-4117-9d84-84bc0a07a862" />


The system combines:

- Traditional Information Retrieval (TF-IDF)

- Vector-based semantic search (LLM embeddings)

- LLM-powered summarization

- Interactive Streamlit UI

## Objectives

- Efficiently search a large text corpus

- Retrieve the most relevant documents for a user query

- Generate coherent summaries of retrieved documents

-  Allow users to control summary length

- Provide a clean and user-friendly interface

## Supported Topics

The corpus contains documents related to:

1.  Machine Learning

2. Deep Learning

3. Natural Language Processing (NLP)

4. Large Language Models (LLMs)

5. Retrieval-Augmented Generation (RAG)

6. Transformers

7. Reinforcement Learning

8. Computer Vision

9. Recommendation Systems

10. Ethics in AI

## Installation & Setup

*1. Prerequisites*

- Python 3.10+

- Ollama installed
https://ollama.com

- ollama pull llama3

*2. Clone the Repository*

- git clone https://github.com/Gopinath-chinnadurai/Document-Search-and-Summarization-Using-LLM-RAG-.git

- cd Document-Search-and-Summarization-Using-LLM-RAG-

*3. Install Dependencies*

- pip install -r requirements.txt

*4. requirements.txt*

- streamlit
- ollama
- numpy
- scikit-learn

*5. Running the Application*

- streamlit run app.py

**The app will open automatically in your browser:**


## Application Features

**Query Input**

- Type your own query OR

- Select from suggested queries (auto-suggestions)

*Search*

Hybrid document search using:

- TF-IDF (keyword relevance)

- LLM embeddings (semantic similarity)

*Summarization*

- Summaries generated using LLaMA 3

- Adjustable summary length[Short, Medium, Long]

*Results Display*

- Top-N relevant documents

- Similarity score displayed

- Expandable summaries

- Pagination support

## Evaluation

Run Evaluation Script

- python evaluation.py

## Evaluation Includes:

- Search accuracy (document relevance)

- Summary quality

- Manual + automated analysis readiness (ROUGE-compatible)

## Why This Is RAG?

This project strictly follows the RAG pipeline:

*1. Retrieve*

- Relevant documents are retrieved from an external corpus using TF-IDF + embeddings

*2. Augment*

- Retrieved documents are passed as context to the LLM

*3. Generate*

- The LLM generates grounded summaries based on retrieved content

*This reduces hallucinations and improves factual accuracy.*

## Scalability & Efficiency

- Easily extendable to thousands of documents

- Embeddings can be stored in FAISS / Vector Databases

- Modular design for future enhancements

- Local LLM inference using Ollama for efficiency

## Conclusion

*This project demonstrates:*

- Practical use of Large Language Models

- Strong Information Retrieval fundamentals

- Real-world RAG system design

- Clean, modular codebase

Interactive and user-friendly UI

*Fully satisfies the Interview Assignment requirements*

## Author

*Gopinath Chinnadurai*

*GitHub:*

https://github.com/Gopinath-chinnadurai
