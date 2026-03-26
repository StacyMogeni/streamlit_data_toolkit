import streamlit as st

st.title("My First Streamlit App")

st.write("Hello, this is my first app!")

name = st.text_input("Enter your name:")

if name:
    st.write(f"Welcome, {name}!")  