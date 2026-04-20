import streamlit as st
from api_calling import note_generator, audio_transcription, quiz_generator
from PIL import Image

# Title section
st.title("Note Summary & Quiz Generator")
st.markdown("Upload upto 3 images to generate Note Summary and Quizes")
st.divider()


# Sidebar Section 
with st.sidebar:
    st.header("Controlls")
    
    # upload Images section
    images = st.file_uploader(
        "Upload the photoes of your note",
        type=['jpg','jpeg','png'],
        accept_multiple_files=True
    )
    
    pil_images = []
    for img in images:
        pil_img = Image.open(img)
        pil_images.append(pil_img)
    
    if pil_images:
        if len(pil_images)>3:
            st.error("Upload Maximum 3 Images")
        else:
            st.subheader("Your Images: ")
            col = st.columns(len(pil_images))
            for i, img in enumerate(pil_images):
                with col[i]:
                    st.image(img)
    
    
    # difficulty section
    selected_option = st.selectbox(
        "Enter the difficulty level of your quiz: ",
        ("Easy", "Medium", "Hard"),
        index=None
    )
    pressed = st.button("Click the button to initiate AI", type="primary")


# output section (body)
if pressed:
    if not images:
        st.error("No image uploaded! Please upload images.")
    if not selected_option:
        st.error("You must select the difficulty of your **Quizes**")

if images and selected_option:
    # about note:
    with st.container(border=True):
        st.subheader("Your note: ",anchor=None)
        with st.spinner("AI is writing notes for you: "):
            generated_note = note_generator(pil_images)
            st.markdown(generated_note)  # will use gemini api


    # Audio Transcript:
    with st.container(border=True):
        st.subheader("Listen the summary: ", anchor=None)
        
        with st.spinner("AI is creating audio for you: "):
            
            #clearing some markdowns for clear audio
            for ch in ["#", "*", "_", "-", "'"]:
                generated_note = generated_note.replace(ch, "")
            
            audio_transcript = audio_transcription(generated_note)
            st.audio(audio_transcript)
    
    # Quiz 
    with st.container(border=True):
        st.subheader(f"Quiz ({selected_option} level)", anchor=None)
        with st.spinner("AI is creating quizes for you: "):
            quizes = quiz_generator(pil_images,selected_option)
            st.markdown(quizes)
