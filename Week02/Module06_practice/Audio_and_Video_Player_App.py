import streamlit as st
st.title("Audio & Video Player App")
audio = st.file_uploader("Upload your audio: ", type=['mp3','ogg'])
pressed = st.button("Play your audio")
if audio:
    if pressed:
        st.audio(audio)
else:
    if pressed:
        st.error("Upload a audio file first.")
st.divider()
video = st.file_uploader("Upload your video: ", type=['mp4','mkv'])
pressed_vid = st.button("Play your video")
if audio:
    if pressed_vid:
        st.video(video)
else:
    if pressed_vid:
        st.error("Upload a video file first.")

