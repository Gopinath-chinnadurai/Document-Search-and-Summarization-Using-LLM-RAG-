from pypdf import PdfReader
from config import MAX_FILE_SIZE

def load_txt(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def load_pdf(file):
    if file.size > MAX_FILE_SIZE:
        raise ValueError("File size exceeds 200 KB")

    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text.strip()
