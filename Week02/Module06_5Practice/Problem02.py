import streamlit as st
from google import genai
import os
from dotenv import load_dotenv
st.title("Professional Sentence Improver", anchor=False)
load_dotenv()
user_input= st.text_input("Enter the sentance: ")
button = st.button("Improve Sentence")
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
prompt = f"Improve this sentence professionally: {user_input}"
if user_input=="":
    if button:
        st.error("Enter your question first")
else:
    if button:
        
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt,

        )
        st.write(response.text)