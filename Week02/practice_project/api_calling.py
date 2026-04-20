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

def hints_generator(Uploaded_image):
    prompt = """You are a coding debugging assistant.
    I will upload a screenshot of an error message, terminal output, IDE screen, or code snippet.
    Your job is to:
    * Carefully read the screenshot
    * Identify the actual error
    * Explain the likely cause in simple language
    * Give only hints and guidance, not the full corrected code immediately
    * Help me think through the issue step by step
    * Mention which line or part of the code is likely causing the problem
    * Suggest what concepts I should check (syntax, indentation, variable names, imports, arguments, object types, package versions, etc.)
    * If there are multiple possible causes, list them from most likely to least likely
    * If needed, ask me for the missing code around the error
    * Do not rewrite the whole program unless I specifically ask
    * Focus on teaching debugging and problem-solving skills
    * Explain beginner-friendly reasoning for why the error happened
    * If the screenshot contains Python code, assume I am still learning Python and explain in simple terms
    At the end of your response, always include:
    1. What the error means
    2. Where to check
    3. What to try next
    4. A small hint instead of the final answer
    """
    response = my_client.models.generate_content(model="gemini-3-flash-preview", contents=[Uploaded_image,prompt])
    return response.text

def solution_generator(Uploaded_image):
    prompt = """You are an expert programming debugger.
    I will upload a screenshot containing a coding error or terminal output or IDE message or traceback or compiler/runtime error ar mixture of them.
    Your task is to:
    1. Read all visible code, error messages, warnings, line numbers, and terminal output carefully from the uploaded images.
    2. Identify the exact cause of the error.
    3. Explain the problem in simple language.
    4. Show which line is causing the issue.
    5. Provide the corrected code snippet.
    6. If there are multiple possible causes, list them in order of likelihood.
    7. Mention whether the issue is due to syntax, logic, library import, version mismatch, indentation, environment, file path, API usage, variable naming, or dependency issues.
    8. If the screenshot is unclear or incomplete, clearly mention what additional screenshot or code is needed.
    9. Keep the answer structured like this:
    - Error Type
    - Cause
    - Problematic Line
    - Fixed Code
    - Extra Notes
    10. Do not only explain the error — always provide a corrected version of the code.
    Assume the user is a beginner and explain step by step in an easy way.
    """
    response = my_client.models.generate_content(model="gemini-3-flash-preview", contents=[Uploaded_image,prompt])
    return response.text

