import streamlit as st
from chat import generate_response

st.set_page_config(
    page_title="AI Chat Assistant",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.title("🤖 AI Chat Assistant")
st.markdown(
    """
    Welcome to your **Gemini-powered AI Chat Assistant**.
    Ask any question and get intelligent responses powered by Google's Gemini model.
    """
)
with st.sidebar:
    st.title("📌 Project Info")
    st.write("### About")
    st.write(
        """
        **Model:** Gemini 2.5 Flash

        **Backend:** Google GenAI SDK

        **Frontend:** Streamlit

        **Developer:** Prince Verma
        """
    )
        # Clear Chat Button
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()



# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages=[]

for message in st.session_state.messages: # Display old messages
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input=st.chat_input("Ask me anything...") # user input

#Process User Input
if user_input: 
    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    st.session_state.messages.append(  # Store user message
        {
            "role":"user",
            "content":user_input
        })

    # Generate AI response
    with st.spinner("🤖Thinking..."):
        response = generate_response(st.session_state.messages)

    # Store assistant response
    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":response
        })
    
    # Display AI response
    with st.chat_message("assistant"):
        st.markdown(response)