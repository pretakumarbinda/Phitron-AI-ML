import streamlit as st
from google import genai
import os
from dotenv import load_dotenv

st.title("Gemini Chatbot App", anchor = False)

question = st.text_input("What can I do for you? ")
button = st.button("Ask Gemini")
load_dotenv()
api_key = os.environ.get("GEMINI_API_CODE")
client = genai.Client(api_key=api_key)

if question=="":
    if button:
        st.error("Enter your question first")
else:
    if button:
        
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=question
        )
        st.write(response.text)
