from google import genai
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()   # loading .env file
my_api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=my_api_key)  # creating client object

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Tell me something about Bangladesh"
    )

print(response.text)

st.markdown(response.text)