import streamlit as st

st.title("input your info", anchor=False)
st.divider()

name = st.text_input("Enter your name:")
st.write("Your name is: ", name)

st.divider()

age = st.number_input("Enter your age: ", value=None, placeholder="type your age")
st.write("Your age is: ", age)

print(name)

password = st.text_input("Enter your name:", type="password")


st.divider()

pressed = st.button("enter to confirm", type="primary")
if pressed:
    st.write("your pass is:",password)
    
selected = st.selectbox("Choose your profession",("student","employee", "businessmen"),index=None, accept_new_options=True)
st.write("you selected: ", selected)
