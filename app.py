import streamlit as st
st.title("Hello,Streamlit")
st.write("This is my first Streamlit App.")

name=st.text_input("What's your name?")
st.write(f"Hello, {name} !")
