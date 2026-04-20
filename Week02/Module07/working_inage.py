import streamlit as st
from google import genai
import os
from dotenv import load_dotenv

from PIL import Image

load_dotenv()

my_api_key = os.getenv("GEMINI_API_KEY")

# initialize client
my_client = genai.Client(api_key=my_api_key)


images = st.file_uploader(
    "Upload the photoes of your note",
    type=['jpg','jpeg','png'],
    accept_multiple_files=True      # so this images are now in a list
)


if images:
    
    pil_images = []
    for img in images:
        pil_img = Image.open(img)
        pil_images.append(pil_img)
    
    prompt = """Summarize the texts from the pictures provided, in note format at maximum 100 words.
            Please use necessery markdown to differentiate different section and make the node visually attractive."""
    response = my_client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[images,prompt]
    )
    st.text(response.text)