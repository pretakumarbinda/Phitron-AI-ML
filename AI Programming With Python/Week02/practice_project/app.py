import streamlit as st
from PIL import Image
from api_calling import hints_generator, solution_generator


st.title("**AI Code Debugger App**",anchor=False, text_alignment="center")
st.markdown("Upload upto 3 images to debug your error.")
st.divider()

# Image Upload Section
images = st.file_uploader("Upload your screenshot here: ", type=['jpg','png','jpeg'], accept_multiple_files=True)
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


selected_option = st.selectbox("What do you want from AI? ",["Hints","Solution with code"], index=None)
button_pressed = st.button("Debug Code",type="primary")

# output section
if button_pressed:
    if len(pil_images)<1:
        st.error("You must upload at least one image!")
    elif not selected_option:
        st.error("You must select one option!")

if button_pressed and images and selected_option:
    with st.container(border=True):
        st.subheader("Your Solution: ", anchor=False)
        with st.spinner("AI is solving your issue..."):
            if selected_option == "Hints":
                output_generated = hints_generator(pil_images)
                st.markdown(output_generated)
            else:
                output_generated = solution_generator(pil_images)
                st.markdown(output_generated)
