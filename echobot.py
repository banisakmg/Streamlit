import streamlit as st

# Page configuration
st.set_page_config(
    page_title="✨ Echo AI Assistant",
    page_icon="🤖",
    layout="centered"
)

# Header
st.title("🤖 Echo AI Assistant")
st.markdown(
    """
    Welcome! I'm **Echo AI**, your friendly conversational companion.
    
    💬 Ask me anything and I'll echo it back with style!
    """
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("✨ Type your message here..."):

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Save user message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    # Fun assistant responses
    response = f"""
🚀 **You said:**

> {prompt}

🎉 Thanks for sharing! I heard you loud and clear.
"""

    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(response)

    # Save assistant response
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

# Sidebar
with st.sidebar:
    st.header("⚡ About Echo AI")
    st.write(
        """
        This demo showcases:
        - 💬 Interactive chat interface
        - 🧠 Conversation history
        - ✨ Modern chat layout
        - 🚀 Streamlit chat components
        """
    )

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

  
