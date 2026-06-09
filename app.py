import gradio as gr
from groq import Groq
import os
from retrieve import retrieve
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def ask(query):
    # 1. Retrieve relevant chunks
    retrieved_chunks = retrieve(query, top_k=4)
    
    # 2. Format the context and extract sources programmatically
    context = ""
    sources = set()
    for chunk in retrieved_chunks:
        context += f"Document: {chunk['metadata']['source']}\nText: {chunk['text']}\n\n"
        sources.add(chunk['metadata']['source'])
        
    # 3. Create the grounded system prompt
    system_prompt = """You are a helpful assistant for the 'Unofficial Guide to Quantum Computing Careers'. 
Your job is to answer user questions using ONLY the provided context.
If the context does not contain enough information to answer the question, you must explicitly state: 'I don't have enough information on that.'
Do not use your general knowledge to answer.
"""
    
    user_message = f"Context:\n{context}\n\nQuestion: {query}"
    
    # 4. Generate the response
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            temperature=0.0, # A low temperature prevents hallucinations
        )
        answer = response.choices[0].message.content
        return {"answer": answer, "sources": list(sources)}
    except Exception as e:
        return {"answer": f"An error occurred: {str(e)}", "sources": []}

def handle_query(question):
    result = ask(question)
    sources_text = "\n".join(f"• {s}" for s in result["sources"])
    return result["answer"], sources_text

# 5. Build the Gradio Interface
with gr.Blocks() as demo:
    gr.Markdown("# The Unofficial Guide to Quantum Computing Careers")
    gr.Markdown("Ask a question about the reality of working in quantum computing, salary bands, certifications, or courses!")
    
    inp = gr.Textbox(label="Your question", placeholder="e.g., Do I need a PhD to work at a quantum startup?")
    btn = gr.Button("Ask")
    answer = gr.Textbox(label="Answer", lines=8)
    sources = gr.Textbox(label="Retrieved from", lines=4)
    
    btn.click(handle_query, inputs=inp, outputs=[answer, sources])
    inp.submit(handle_query, inputs=inp, outputs=[answer, sources])

if __name__ == "__main__":
    demo.launch()