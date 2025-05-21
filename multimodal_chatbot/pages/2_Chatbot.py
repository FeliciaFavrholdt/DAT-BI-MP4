import streamlit as st
from utils import *

st.set_page_config(page_title="Chatbot", layout="wide")
st.title("Chatbot")
st.markdown("---")

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "indexed_files" not in st.session_state:
    st.session_state.indexed_files = []

# Chat input
user_question = st.text_input("Ask me anything", key="question_input")

# Upload grid layout
col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)

def track_and_store(file_list, parser):
    names = handle_multiple_files(file_list, parser)
    st.session_state.indexed_files.extend(names)
    return names

# Upload sections
with col1:
    st.markdown("**Upload Image**")
    files = st.file_uploader("Upload image(s)", type=["jpg", "jpeg", "png"], accept_multiple_files=True, label_visibility="collapsed")
    if files:
        names = track_and_store(files, parse_image)
        st.success(f"Indexed: {', '.join(names)}")

with col2:
    st.markdown("**Upload CSV**")
    files = st.file_uploader("Upload CSV(s)", type=["csv"], accept_multiple_files=True, label_visibility="collapsed")
    if files:
        names = track_and_store(files, parse_csv)
        st.success(f"Indexed: {', '.join(names)}")

with col3:
    st.markdown("**Upload PDF**")
    files = st.file_uploader("Upload PDF(s)", type=["pdf"], accept_multiple_files=True, label_visibility="collapsed")
    if files:
        names = track_and_store(files, parse_pdf)
        st.success(f"Indexed: {', '.join(names)}")

with col4:
    st.markdown("**Upload Text/DOCX**")
    files = st.file_uploader("Upload Text", type=["txt", "docx"], accept_multiple_files=True, label_visibility="collapsed")
    if files:
        names = track_and_store(files, parse_file)
        st.success(f"Indexed: {', '.join(names)}")

with col5:
    st.markdown("**Upload Other File**")
    files = st.file_uploader("Upload Other", type=["md", "rtf"], accept_multiple_files=True, label_visibility="collapsed")
    if files:
        names = track_and_store(files, parse_file)
        st.success(f"Indexed: {', '.join(names)}")

with col6:
    st.markdown("**Analyze Webpage**")
    url = st.text_input("Enter URL")
    if url:
        content = parse_webpage(url)
        if content.strip():
            chunks = split_text(content)
            store_chunks(chunks)
            st.session_state.indexed_files.append(url)
            st.success("Webpage content indexed.")

# Output section
st.markdown("## Output")

if user_question:
    st.chat_message("user").write(user_question)
    docs = retrieve_chunks(user_question)
    answer = answer_question(user_question, docs)
    st.chat_message("assistant").write(answer)
    st.session_state.chat_history.append(("user", user_question))
    st.session_state.chat_history.append(("assistant", answer))

# Display chat history
for role, msg in st.session_state.chat_history:
    st.chat_message(role).write(msg)

# Download chat history
if st.session_state.chat_history:
    chat_text = "\n\n".join(f"{role.upper()}: {msg}" for role, msg in st.session_state.chat_history)
    st.download_button("Download Chat History", data=chat_text, file_name="chat_history.txt")

# Display indexed files
if st.session_state.indexed_files:
    st.markdown("### Indexed Files / Sources")
    for name in set(st.session_state.indexed_files):
        st.write(f"- {name}")
