from ollama import embeddings

def get_embedding(text):
    return embeddings(
        model="nomic-embed-text",
        prompt=text
    )["embedding"]
