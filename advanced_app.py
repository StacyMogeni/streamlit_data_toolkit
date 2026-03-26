import streamlit as st
import pandas as pd

# Sidebar Navigation
st.sidebar.title("📚 Navigation")
page = st.sidebar.radio("Go to", ["Home", "Learn", "Data App"])

# Home Page
if page == "Home":
    st.title("🚀 Streamlit Starter Kit")
    st.write("Welcome! This app demonstrates basic Streamlit features.")

# Learn Page
elif page == "Learn":
    st.title("📖 Streamlit Basics")

    st.markdown("""
    ### What is Streamlit?
    Streamlit is a Python library used to build interactive web apps for data science.

    ### Key Features:
    - Simple and beginner-friendly  
    - No front-end development required  
    - Fast app deployment  
    """)

# Data App Page
elif page == "Data App":
    st.title("📊 Data Explorer")

    file = st.file_uploader("Upload a CSV file")

    if file is not None:
        df = pd.read_csv(file)
    else:
        st.warning("Please upload a CSV file to continue.")
        st.stop()  

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.write("Dataset Shape:", df.shape)

    st.subheader("Summary Statistics")
    st.write(df.describe())

    column = st.selectbox("Select a column to visualize", df.columns)

    if column:
        st.subheader(f"Bar Chart of {column}")
        st.bar_chart(df[column])        