import os
import glob
import random
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Define the path to the documents folder
DOCS_DIR = "documents"

def load_documents(directory):
    """Loads all markdown files from the specified directory."""
    documents = []
    filepaths = glob.glob(os.path.join(directory, "*.md"))
    
    for filepath in filepaths:
        with open(filepath, 'r', encoding='utf-8') as file:
            text = file.read()
            # Our documents are already clean markdown, so we don't need heavy HTML stripping here
            documents.append({
                "text": text,
                "metadata": {"source": os.path.basename(filepath)}
            })
    return documents

def chunk_documents(documents, chunk_size=512, chunk_overlap=64):
    """Splits documents into smaller chunks using RecursiveCharacterTextSplitter."""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", " ", ""] # Try to split on paragraphs first, then lines, etc.
    )
    
    chunks = []
    for doc in documents:
        # Split the text
        splits = text_splitter.split_text(doc["text"])
        
        # Reattach metadata to each chunk
        for split in splits:
            chunks.append({
                "text": split,
                "metadata": doc["metadata"]
            })
            
    return chunks

if __name__ == "__main__":
    print(f"Loading documents from '{DOCS_DIR}'...")
    raw_docs = load_documents(DOCS_DIR)
    print(f"Loaded {len(raw_docs)} documents.")
    
    print("\nChunking documents...")
    all_chunks = chunk_documents(raw_docs)
    print(f"Total chunks created: {len(all_chunks)}")
    
    print("\n--- Inspecting 5 Random Sample Chunks ---\n")
    sample_size = min(5, len(all_chunks))
    sample_chunks = random.sample(all_chunks, sample_size)
    
    for i, chunk in enumerate(sample_chunks):
        print(f"Chunk {i+1} | Source: {chunk['metadata']['source']} | Length: {len(chunk['text'])} chars")
        print("-" * 60)
        print(chunk['text'])
        print("-" * 60 + "\n")