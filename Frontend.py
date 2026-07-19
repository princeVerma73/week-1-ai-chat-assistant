"""Streamlit interface for the AI Customer Support Assistant."""

import streamlit as st
from chat import generate_response


st.set_page_config(
    page_title="Nova Support | AI Customer Support",
    page_icon="🎧",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
        .block-container {max-width: 900px; padding-top: 2.5rem;}
        [data-testid="stSidebar"] {border-right: 1px solid #e7eaf0;}
        .support-hero {padding: 0.25rem 0 1.25rem;}
        .support-hero h1 {margin-bottom: 0.25rem;}
        .support-hero p {color: #566074; font-size: 1.05rem; margin: 0;}
    </style>
    """,
    unsafe_allow_html=True,
)

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.title("🎧 Nova Support")
    st.caption("AI-powered customer assistance")
    st.divider()
    st.subheader("What I can help with")
    st.markdown("- Orders and delivery\n- Refunds and payments\n- Accounts and general support")
    st.divider()
    st.caption("Powered by LangChain + Gemini 2.5 Flash")
    if st.button("🗑️ Clear chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

st.markdown(
    """
    <div class="support-hero">
      <h1>How can we help?</h1>
      <p>Describe your issue and receive clear, professional support in seconds.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

if not st.session_state.messages:
    st.info("Try: “Where is my order?” or “How do I request a refund?”", icon="💡")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_input := st.chat_input("Type your customer support question..."):
    user_message = {"role": "user","content": user_input}
    st.session_state.messages.append(user_message)

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Finding the best way to help..."):
            answer = generate_response(st.session_state.messages)
        st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})
