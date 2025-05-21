# memory.py

import streamlit as st

def initialize_memory():
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    if "indexed_files" not in st.session_state:
        st.session_state.indexed_files = []

def add_to_memory(role, message):
    st.session_state.chat_history.append((role, message))

def get_chat_history():
    return st.session_state.chat_history

def clear_memory():
    st.session_state.chat_history = []
    st.session_state.indexed_files = []

def add_indexed_files(filenames):
    st.session_state.indexed_files.extend(filenames)

def get_indexed_files():
    return list(set(st.session_state.indexed_files))
