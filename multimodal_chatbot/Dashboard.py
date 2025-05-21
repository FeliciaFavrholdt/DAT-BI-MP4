import streamlit as st

st.set_page_config(page_title="Dashboard | Group 4 Chatbot", layout="wide")
st.title("Group 4 Chatbot Multimodal")

st.markdown("Welcome to Dashboard. This page summarizes your current session.")

st.markdown("---")

# ========== Indexed Files Section ==========

if "indexed_files" in st.session_state and st.session_state.indexed_files:
    st.subheader("Indexed Files")
    for name in set(st.session_state.indexed_files):
        st.write(f"- {name}")
else:
    st.info("No files have been indexed yet.")

# ========== Chat Summary Section ==========

if "chat_history" in st.session_state and st.session_state.chat_history:
    st.subheader("Recent Questions")
    user_questions = [msg for role, msg in st.session_state.chat_history if role == "user"]
    if user_questions:
        for q in user_questions[-5:]:
            st.markdown(f"- {q}")
    else:
        st.info("No questions asked yet.")
else:
    st.info("No chat activity in this session.")

# ========== Navigation Section ==========

st.markdown("---")
st.subheader("Navigation")
col1, col2 = st.columns(2)

with col1:
    st.page_link("pages/2_Chatbot.py", label="Open Chatbot")

with col2:
    st.page_link("pages/1_About.py", label="About the Project")
