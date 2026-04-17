import streamlit as st
st.title("Personal Info Card App")
name = st.text_input("Enter Your Name: ")
age = st.number_input("Enter Your Age:",value=None,placeholder="Type your age")
profession = st.selectbox("Enter your Profession: ", options=['Student','Employee','Businessman','Freelancer'], index=None)
button = st.button("Confirm")
if button:
    if name == "" or age is None or profession is None:
        st.error("Please fill all fields.")
    else:
        st.success("All fields are filled.")
        st.write("your name is: ",name)
        st.write("Your age is: ",age)
        st.write("Your profession is: ",profession)
