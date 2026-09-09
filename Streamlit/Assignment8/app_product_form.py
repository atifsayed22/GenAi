import streamlit as st 

name = st.sidebar.text_input("Enter Product name : ")
category = st.sidebar.selectbox("Enter Category : " , ["Electronics" , "Clothing" , "Accessories"])
price = st.sidebar.number_input("Enter price : ")

info = {
    "name " : name , 
    "category" : category , 
    "price" : price 
}

if st.sidebar.button("Add Product +") : 
    st.sidebar.success("Product added Successfully")
    st.sidebar.table(info)
