import streamlit as st
st.title("Input your files", anchor = False)
st.divider()

#from storage
st.image("picture/hogworts.png")

#from online
st.image("https://static.vecteezy.com/system/resources/thumbnails/057/068/323/small/single-fresh-red-strawberry-on-table-green-background-food-fruit-sweet-macro-juicy-plant-image-photo.jpg")
st.divider()

image = st.file_uploader("Enter your file", type=["png", 'jpeg', 'jpg'],accept_multiple_files=True)
print(type(image))
if image:
    # to create column
    col = st.columns(len(image))  # creating column object
    for i,per_image in enumerate(image):
        with col[i]:
            st.image(per_image)
            


# for showing audio

#from directory/storage
st.audio("audio/harry_potter.mp3")

#user audio input:
audio_file = st.file_uploader("Enter your audio: ",type=['mp3','ogg','flac'])
if audio_file:
    st.audio(audio_file)
    
## video adding:
st.title("Enter video file:",anchor=False)
st.divider()
video_file = st.file_uploader("Enter your video",type=['mp4','mkv'])

button = st.button("Click to upload: ")
if button:
    if video_file:
        st.video(video_file)
        st.success("Your file is uploaded successfully")
    else:
        st.error("You must upload a file")