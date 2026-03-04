import chromadb
import os
import ollama
import re
from tqdm import tqdm

DB_PATH = r"D:\Projects2\llama32-specified-knowledge\chroma_db"

def clean_text(text):
    text = re.sub(r"\[\[.*?\|(.*?)\]\]", r"\1", text)

    text = re.sub(r"\[\[(.*?)\]\]", r"\1", text)

    text = re.sub(r"<.*?>", " ", text)

    text = re.sub(r"\s+", " ", text)

    return text.strip()

client = chromadb.PersistentClient(
    path=DB_PATH,
    tenant="default_tenant",
    database="default_database"
)

try:
    client.delete_collection("worldwitches")
except:
    pass

collection = client.create_collection("worldwitches")

folder_path = "wiki_text"

def embed(text):
    return ollama.embeddings(
        model="nomic-embed-text",
        prompt=text
    )["embedding"]

doc_id = 0
files = os.listdir(folder_path)

print(f"Found {len(files)} files.")

for filename in tqdm(files, desc="Indexing files"):
    with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as f:
        content = clean_text(f.read())

    if len(content) < 50:
        continue

    chunks = [content[i:i+800] for i in range(0, len(content), 800)]

    for chunk in chunks:
        collection.add(
            documents=[f"TITLE: {filename}\n\n{chunk}"],
            embeddings=[embed(chunk)],
            ids=[str(doc_id)],
            metadatas=[{"source": filename}]
        )
        doc_id += 1

print("\nIndexing Done.")
print("Total documents in DB:", collection.count())