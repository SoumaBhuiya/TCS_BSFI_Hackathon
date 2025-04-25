

import streamlit as st
from utils import ask_gemini, load_knowledge_base  # Make sure both functions are imported

# Set up the page configuration for Streamlit
st.set_page_config(page_title="Insurance Chatbot", layout="centered")

# Custom CSS for Dark Theme Colors and Styling
st.markdown(
    """
    <style>
        .stApp {
            background-color: #1e1e2f;  /* Dark background color */
            color: #3d6fbd;  /* White text for readability */
        }
        .stTitle {
            color: #ffffff;  /* White for the title */
        }
        .stTextInput input {
            background-color: #fff;  /* Darker background for text input */
            border-color: #6e7f94;  /* Light blue-gray border for text input */
            color: #6e7f94;  /* White text inside the input box */
        }
        .stTextInput input:focus {
            border-color: #4a6f91;  /* Blue border on focus */
        }
        .stMarkdown {
            color: #ffffff;  /* White color for markdown text */
        }
        .stButton {
            text:#6e7f94;
            background-color: #1e1e2f;  /* Dark button color matching background */
            color: #6e7f94;  /* White text on buttons */
            border: 2px solid transparent;  /* Transparent border */
            transition: all 0.3s ease;  /* Smooth transition for hover effect */
        }
        .stButton: {
           
            color: #3d6fbd;  /* Change text color to #3d6fbd on hover */
            
        }
      
        .stWarning {
            background-color: #ffb84d;  /* Light orange for warning messages */
            color: #333333;  /* Dark text for warning */
        }
        .stTextInput label {
            color: #ffffff;  /* White color for labels */
        }
        .stSlider {
            background-color: #3a3a4a;  /* Darker slider background */
            color: #ffffff;  /* White color for slider text */
        }
        .stRadio {
            background-color: #3a3a4a;  /* Dark background for radio buttons */
            color: #ffffff;  /* White for radio buttons */
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and introductory text
st.title("Insurance Policy Assistant 🤖")
st.markdown("Ask anything about our insurance plans, coverage, premiums, or claims!")

# Load the knowledge base from the PDF (data.pdf)
if "context" not in st.session_state:
    st.session_state.context = load_knowledge_base(pdf_path="data.pdf")  # Use PDF

# Initialize conversation history if not already done
if "conversation" not in st.session_state:
    st.session_state.conversation = []

# Input from the user
user_input = st.text_input("You:", placeholder="What does life insurance cover?")

# Add a Submit button to submit the question
submit_button = st.button("Submit", help="Click to submit your question")

# If the submit button is clicked and there is user input
if submit_button and user_input:
    # Add user input to the conversation history
    st.session_state.conversation.append(f"You: {user_input}")
    
    with st.spinner("Thinking..."):
        reply = ask_gemini(user_input, st.session_state.context)
        
        # Add bot's response to the conversation history
        st.session_state.conversation.append(f"Bot: {reply}")
    
    # Display the conversation history
    for message in st.session_state.conversation:
        if message.startswith("You:"):
            st.markdown(f"<p style='color: #ffffff;'><b>{message}</b></p>", unsafe_allow_html=True)
        else:
            st.markdown(f"<p style='color: #6e7f94;'><b>{message}</b></p>", unsafe_allow_html=True)

# If the user asks for an agent
if user_input and "agent" in user_input.lower():
    st.warning("It seems you need help from a human agent. We'll connect you shortly.")
    st.button("Connect to Agent", help="Click here to connect to a human agent.")
