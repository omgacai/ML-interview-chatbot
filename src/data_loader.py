from bs4 import BeautifulSoup
import os
import fitz  # PyMuPDF
from src.config import CORPUS_PATH

def split_text(text, chunk_size=1000, overlap=100):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)
    return chunks

def load_documents(corpus_path):
    all_chunks = []

    for fname in os.listdir(corpus_path):
        fpath = os.path.join(corpus_path, fname)

        if fname.endswith(".pdf"):
            doc = fitz.open(fpath)
            full_text = "\n".join(page.get_text() for page in doc)
            chunks = split_text(full_text)
            for chunk in chunks:
                all_chunks.append({"content": chunk, "meta": {"name": fname}})

        elif fname.endswith(".html"):
            with open(fpath, "r", encoding="utf-8") as f:
                soup = BeautifulSoup(f, "html.parser")
                full_text = soup.get_text(separator="\n")
                chunks = split_text(full_text)
                for chunk in chunks:
                    all_chunks.append({"content": chunk, "meta": {"name": fname}})

    return all_chunks
