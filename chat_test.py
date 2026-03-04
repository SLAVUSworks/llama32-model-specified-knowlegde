import chromadb
import ollama

DB_PATH = r"D:\Projects2\llama32-specified-knowledge\chroma_db"

client = chromadb.PersistentClient(
    path=DB_PATH,
    tenant="default_tenant",
    database="default_database"
)

print("Available collections:")
for col in client.list_collections():
    print("-", col.name, "| count:", col.count())

collection = client.get_collection("worldwitches")

print("Total docs in worldwitches:", collection.count())

while True:
    query = input("\nTanya: ")

    query_embed = ollama.embeddings(
        model="nomic-embed-text",
        prompt=query
    )["embedding"]

    results = collection.query(
        query_embeddings=[query_embed],
        n_results=5
    )

    if not results["documents"] or not results["documents"][0]:
        print("No results found.")
        continue

    context = "\n".join(results["documents"][0])

    prompt = f"""
Answer the questions using the information below.
If it's partially relevant, keep your answers contextual.

Konteks:
{context}

Pertanyaan: {query}
Jawaban:
"""

    response = ollama.chat(
        model="llama3.2:3b",
        messages=[{"role": "user", "content": prompt}]
    )

    print("\nJawaban:\n", response["message"]["content"])