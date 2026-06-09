import chromadb
from sentence_transformers import SentenceTransformer
from ingest import load_documents, chunk_documents, DOCS_DIR

# 1. Initialize the embedding model but keep it on CPU for simplicity in this example as my local old gpu is not compatible with the model
print("Loading embedding model...")
model = SentenceTransformer("all-MiniLM-L6-v2", device="cpu")

# 2. Initialize ChromaDB
print("Initializing ChromaDB...")
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection_name = "unofficial_guide"

# We delete the collection if it exists to start fresh on each run for testing
try:
    chroma_client.delete_collection(name=collection_name)
except Exception:
    pass

collection = chroma_client.create_collection(
    name=collection_name,
    metadata={"hnsw:space": "cosine"}
)

# 3. Load and chunk documents
print("Loading and chunking documents...")
raw_docs = load_documents(DOCS_DIR)
chunks = chunk_documents(raw_docs)

# 4. Embed and store chunks
print(f"Embedding and storing {len(chunks)} chunks...")
documents = [chunk["text"] for chunk in chunks]
metadatas = [chunk["metadata"] for chunk in chunks]
ids = [f"chunk_{i}" for i in range(len(chunks))]
embeddings = model.encode(documents).tolist()

collection.add(
    documents=documents,
    embeddings=embeddings,
    metadatas=metadatas,
    ids=ids
)
print("Chunks successfully stored in ChromaDB.")

# 5. Retrieval Function
def retrieve(query, top_k=4):
    """Retrieves the top_k most relevant chunks for a given query."""
    query_embedding = model.encode(query).tolist()
    
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )
    
    retrieved_chunks = []
    for i in range(len(results['ids'][0])):
        retrieved_chunks.append({
            "id": results['ids'][0][i],
            "text": results['documents'][0][i],
            "metadata": results['metadatas'][0][i],
            "distance": results['distances'][0][i]
        })
        
    return retrieved_chunks

if __name__ == "__main__":
    # Test Retrieval with Evaluation Questions
    test_queries = [
        "According to Blind reviews, what is the expected base salary range for a mid-level SWE at IBM Quantum?",
        "What version of Qiskit should I study for the IBM Qiskit Developer Certification?",
        "If I don't have a PhD, what specific roles should I target at a quantum company according to QubitWrangler?"
    ]
    
    print("\n--- Testing Retrieval ---")
    for query in test_queries:
        print(f"\nQuery: '{query}'")
        results = retrieve(query)
        for i, res in enumerate(results):
            print(f"  Result {i+1} | Source: {res['metadata']['source']} | Distance: {res['distance']:.4f}")
            print(f"  Text: {res['text'][:150]}...\n")