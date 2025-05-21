import streamlit as st
import sys
import os

# Let Python find memory.py from parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from memory import initialize_memory, get_chat_history, get_indexed_files

st.set_page_config(page_title="Memory Overview", layout="wide")
st.title("Memory Overview")

initialize_memory()

st.subheader("Indexed Files")
files = get_indexed_files()
if files:
    for name in files:
        st.write(f"- {name}")
else:
    st.info("No files indexed.")

st.subheader("Chat History")
history = get_chat_history()
if history:
    for role, msg in history:
        st.markdown(f"**{role.capitalize()}**: {msg}")
else:
    st.info("No chat history available.")
