import streamlit as st
from preprocess import load_and_clean_data
from search import DocumentSearch
from summarize import summarize_text

st.title("Document Search & Summarization System")

st.caption(
    "Covers Machine Learning, Deep Learning, NLP, LLMs, RAG, "
    "Transformers, Reinforcement Learning, Computer Vision, "
    "Recommendation Systems, and Ethics in AI."
)

documents = load_and_clean_data()
search_engine = DocumentSearch(documents, alpha=0.5)

suggested_queries = [
    "What is machine learning?",
    "Explain deep learning",
    "What is NLP?",
    "What are Large Language Models?",
    "Explain reinforcement learning",
    "What is RAG?",
    "What are transformers?",
    "Ethics in AI examples"
]

st.subheader("Query Input")

custom_query = st.text_input("type your own query:")

selected_suggestion = st.selectbox(
    "Choose a suggested query:",
    [""] + suggested_queries
)

query = custom_query if custom_query else selected_suggestion

summary_option = st.selectbox(
    "Summary length:",
    ["Short", "Medium", "Long"]
)

summary_length_map = {
    "Short": 2,
    "Medium": 4,
    "Long": 6
}
summary_length = summary_length_map[summary_option]

if st.button(" Search"):

    if not query:
        st.warning("Please enter or select a query.")
    else:
        results = search_engine.search(query, top_k=3)

        st.subheader("Results")

        for doc_name, score in results:
            st.markdown(f"###  {doc_name}")
            st.markdown("**Summary:**")

            summary = summarize_text(documents[doc_name], summary_length)
            st.write(summary)

            st.markdown("---")
