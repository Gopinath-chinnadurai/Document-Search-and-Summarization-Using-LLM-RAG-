from ollama import embeddings
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class DocumentSearch:
    def __init__(self, documents, alpha=0.5):
        """
        documents: dict {filename: text}
        alpha: weight for embeddings similarity
        """
        self.alpha = alpha
        self.doc_names = []
        self.texts = []
        self.embeddings_list = []

        for name, text in documents.items():
            self.doc_names.append(name)
            self.texts.append(text)
            self.embeddings_list.append(self.get_vector(text))

        self.tfidf_vectorizer = TfidfVectorizer()
        self.tfidf_matrix = self.tfidf_vectorizer.fit_transform(self.texts)

        print("DocumentSearch initialized with embeddings + TF-IDF")

    def get_vector(self, text):
        response = embeddings("llama3", text)
        return np.array(response.embedding)

    def search(self, query, top_k=3):
        query_emb = self.get_vector(query)
        embedding_sims = [np.dot(query_emb, emb)/(np.linalg.norm(query_emb)*np.linalg.norm(emb)) for emb in self.embeddings_list]

        query_vec = self.tfidf_vectorizer.transform([query])
        tfidf_sims = cosine_similarity(query_vec, self.tfidf_matrix).flatten()

        final_scores = self.alpha * np.array(embedding_sims) + (1 - self.alpha) * np.array(tfidf_sims)
        top_idx = np.argsort(final_scores)[::-1][:top_k]

        top_docs = [(self.doc_names[i], final_scores[i]) for i in top_idx]
        return top_docs
