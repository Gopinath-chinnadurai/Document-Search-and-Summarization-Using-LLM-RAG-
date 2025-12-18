from ollama import chat
from config import LLM_MODEL

def summarize_text(text, sentences=4):
    prompt = f"""
Summarize the following text in {sentences} concise sentences:

{text}
"""
    response = chat(
        model=LLM_MODEL,
        messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"]
