import streamlit as st
from groq import Groq

# Initialize Groq client
client = Groq(
    api_key="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"
)

# Function to get chat response
def get_chat_response(user_message):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_message,
            }
        ],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content

# Initialize session state for conversation history
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Function to handle message submission
def submit_message():
    user_message = st.session_state.user_input
    if user_message:
        # Add user message to conversation history
        st.session_state.messages.append({"role": "user", "content": user_message})
        
        # Get response from the Groq API
        response = get_chat_response(user_message)
        
        # Add bot response to conversation history
        st.session_state.messages.append({"role": "bot", "content": response})
        
        # Clear the input box
        st.session_state.user_input = ""

# Streamlit app interface
st.title("Groq Chatbot Interface")

# Display conversation history
for i, message in enumerate(st.session_state.messages):
    if message['role'] == 'user':
        st.text_area("You:", message['content'], key=f"user_{i}", height=100)
    else:
        st.text_area("Chatbot:", message['content'], key=f"bot_{i}", height=100)

# Text input for user message
st.text_input("You:", key="user_input", on_change=submit_message)
