import streamlit as st 
import pandas as pd

st.title("Hello , GenAi")

st.write("hello world")
st.header("This is  header")
st.subheader("this subheader")
st.text("this is text")
name = st.text_input("Enter your name :")
st.write(name)

##  Button , checkboxex  , slider

level = st.slider("this is slider : " ,)
st.write(f"The level you selected if : {level}")

if st.button("click me!") : 
    st.write("button clicked")

if not st.checkbox("checkbox") : 
    st.write("you checked")


# file upload 

file = st.file_uploader("upload a file ; "  ,type =['csv' , 'txt'])

if file is not None : 
    df = pd.read_csv(file)
    st.dataframe(df)
