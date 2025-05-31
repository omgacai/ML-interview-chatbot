import chromadb
from chromadb.config import Settings
from src.config import TOP_K

# Setup ChromaDB client
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection("rag")


def add_to_vectorstore(docs, embeddings):
    for i, (doc, emb) in enumerate(zip(docs, embeddings)):
        collection.add(
            documents=[doc["content"]],
            metadatas=[doc["meta"]],
            ids=[f"doc_{i}"],
            embeddings=[emb]
        )

def retrieve_relevant_docs(query_embedding):
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=TOP_K
    )
    return results["documents"][0]  # Return top_k documents
