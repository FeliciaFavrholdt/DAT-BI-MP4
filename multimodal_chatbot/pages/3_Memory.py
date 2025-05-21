import streamlit as st
import sys
import os

# Let Python find memory.py from parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from memory import initialize_memory, get_chat_history, get_indexed_files, clear_memory
from utils import reset_vector_store

# Set up page
st.set_page_config(page_title="Memory Overview", layout="wide")
st.title("Memory Overview")
st.markdown("---")

# Initialize memory state
initialize_memory()

# Reset button
if st.button("Reset Memory"):
    reset_vector_store()
    clear_memory()
    st.success("Memory, chat, and file tracking cleared.")

# Indexed files section
st.subheader("Indexed Files")
files = get_indexed_files()
if files:
    for name in files:
        st.write(f"- {name}")
    files_txt = "\n".join(files)
    st.download_button("Download Indexed Files", data=files_txt, file_name="indexed_files.txt")
else:
    st.info("No files indexed.")

# Chat history section
st.subheader("Chat History")
history = get_chat_history()
if history:
    for role, msg in history:
        st.markdown(f"**{role.capitalize()}**: {msg}")
    chat_txt = "\n\n".join(f"{role.upper()}: {msg}" for role, msg in history)
    st.download_button("Download Chat History", data=chat_txt, file_name="chat_history.txt")
else:
    st.info("No chat history available.")
