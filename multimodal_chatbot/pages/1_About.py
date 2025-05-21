import streamlit as st

st.set_page_config(page_title="About", layout="wide")

st.title("About the Application")
st.markdown("---")

st.markdown("""
### Created by Alberte & Felicia  
**CPH Business Academy – Lyngby**

This application is developed as part of **Mini Project 4** for the *Business Intelligence & Data Science* course.

""")

st.markdown("""
## Project Overview

This is a **multimodal chatbot application** that allows users to upload and analyze various types of files using a local language model with Retrieval-Augmented Generation (RAG).

You can upload and ask questions about:

- PDF documents  
- Image files  
- CSV data  
- Text documents (`.txt`, `.docx`)  
- Web page content (via URL)

All data is processed **locally** — nothing is sent to external APIs.

---
""")

st.markdown("""
## How It Works

1. Upload one or more files or enter a URL.
2. The system extracts text or image content.
3. It stores the data as vectors in memory.
4. Ask a question — the app retrieves the most relevant content and generates a response using a local LLM (like `phi` or `llava`).
""")

st.markdown("""
## Technologies Used

- **Streamlit** – Web UI  
- **LangChain** – Chunking, vector search, and prompt chaining  
- **Ollama** – Local LLMs (`phi`, `llava`)  
- **Unstructured** – Multimodal file parsing (text + image)  
- **InMemoryVectorStore** – Fast, temporary vector storage  

---
""")

st.caption("Built with dedication for MP4 | Business Intelligence & Data Science | CPHBusiness")
