import streamlit as st
st.title("Image Gallery App")

images = st.file_uploader("Enter your image (max 03):", type=['jpg','jpeg','png'], accept_multiple_files=True)
if images:
    if len(images)>3:
        st.error("03 images only")
    else:
        if len(images)==3:
            st.success("Uploaded successfully")
        col = st.columns(3)
        for i, per_image in enumerate(images):
            with col[i]:
                st.image(per_image)
