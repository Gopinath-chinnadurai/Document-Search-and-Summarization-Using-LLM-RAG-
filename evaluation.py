from preprocess import load_and_clean_data
from search import DocumentSearch
from summarize import summarize_text
from rouge_score import rouge_scorer

documents = load_and_clean_data()

search_engine = DocumentSearch(documents, alpha=0.5)

test_set = {
    "What is machine learning?": "machine_learning.txt",
    "Explain reinforcement learning.": "reinforcement_learning.txt",
    "What is deep learning?": "deep_learning.txt",
    "What is NLP?": "nlp.txt"
}

correct = 0
for query, expected_doc in test_set.items():
    results = search_engine.search(query, top_k=3)
    top_docs = [doc for doc, _ in results]
    if expected_doc in top_docs:
        correct += 1

accuracy = correct / len(test_set) * 100
print(f"Search Accuracy: {accuracy:.2f}%")

scorer = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)
for query, expected_doc in test_set.items():
    summary = summarize_text(documents[expected_doc], summary_length=3)
    reference = documents[expected_doc]
    scores = scorer.score(reference, summary)
    print(f"\nDocument: {expected_doc}")
    print(f"ROUGE-1: {scores['rouge1'].fmeasure:.3f}, ROUGE-L: {scores['rougeL'].fmeasure:.3f}")
    print(f"Summary: {summary}")
