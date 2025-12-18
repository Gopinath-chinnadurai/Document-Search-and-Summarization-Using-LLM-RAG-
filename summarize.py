from ollama import chat

def summarize_text(text, summary_length=3):
    """
    Summarize the given text in summary_length sentences using LLaMA 3
    """
    prompt = f"Summarize the following text in {summary_length} sentences:\n{text}"
    response = chat("llama3", messages=[{"role": "user", "content": prompt}])
    
    summary_text = response.message.content
    if summary_text.lower().startswith("here is a summary"):
        summary_text = summary_text.split(":", 1)[1].strip()
    
    return summary_text
