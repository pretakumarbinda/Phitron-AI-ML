from google import genai
import os
from dotenv import load_dotenv
import io
from gtts import gTTS
import streamlit as st


load_dotenv()

my_api_key = os.getenv("GEMINI_API_KEY")

# initialize client
my_client = genai.Client(api_key=my_api_key)




# note generator
def note_generator(images):
    prompt = """Summarize the texts from the pictures provided, in note format at maximum 100 words.
            Please use necessery markdown to differentiate different section and make the node visually attractive."""
    response = my_client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[images,prompt]
    )
    return response.text

def audio_transcription(text):
    speech = gTTS(text, lang='en', slow=False)
    audio_buffer = io.BytesIO()     # creating a space in RAM to avoid direct saving
    speech.write_to_fp(audio_buffer)
    return audio_buffer

def quiz_generator(image, difficulty):
    prompt = f"Generate 3 quizes based on the {difficulty}. make sure to add markdown to differentiate the option. after the quizes, add the corerct answers."
    response = my_client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[image,prompt]
    )
    return response.text