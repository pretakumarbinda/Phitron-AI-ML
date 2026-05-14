import streamlit as st

st.title(":world_map: My first streamlit web app", anchor=False)
st.write("Hello World")

# for creating header:
st.header("Content 01", divider=True)
st.subheader("Content 1 Subheader")
st.write("Hello World")

# for markdown code
st.markdown(":red[**Hello** *World*]")
st.markdown(":green[Hello World]")

st.markdown(":red-background[:green[Hello World]] :world_map:")

a=10
b=20
st.write(a,b)