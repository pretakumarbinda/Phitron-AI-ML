import streamlit as st

a = st.number_input("Enter 1st number: ",placeholder="a",value=None)
b = st.number_input("Enter 2nd number: ",placeholder="b",value=None)
box = st.selectbox("Select operation", options=['+','-','*','/'],index=None)
pressed = st.button("Confirm")

if pressed:
    if b==0 and box=="/":
        st.error("cann't devide by zero")
    elif box=="+":
        st.write(a+b)
    elif box=="-":
        st.write(a-b)
    elif box=="*":
        st.write(a*b)
    elif box=="/":
        st.write(a/b)
    else:
        st.error("Select a option first.")