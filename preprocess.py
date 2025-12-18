import os

def load_and_clean_data(data_dir="data"):
    """
    Load all .txt files from data_dir and clean them.
    Include file title in the text for better search accuracy.
    """
    documents = {}
    for file_name in os.listdir(data_dir):
        if file_name.endswith(".txt"):
            with open(os.path.join(data_dir, file_name), "r", encoding="utf-8") as f:
                text = f.read().replace("\n", " ").strip()
                title = file_name.replace("_", " ").replace(".txt","")
                documents[file_name] = f"{title}. {text}"
    return documents
