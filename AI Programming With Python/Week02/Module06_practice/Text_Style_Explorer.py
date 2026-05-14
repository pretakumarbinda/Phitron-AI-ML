import streamlit as st
st.title("Text Style Explorer", anchor = False)
text = st.text_input("Enter your text: ")
if text=="":
    pass
else:
    st.divider()
    st.title(text)
    st.divider()
    st.header(text)
    st.divider()
    st.subheader(text)
    st.divider()
    st.text(text)

