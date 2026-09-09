import streamlit as st 

sales ={
    "January" : 1200 , 
    "February" : 1500 , 
    "March" : 900 , 
    "April" : 2000
}
st.title("Simple Sales Dashboard")
st.write("This Dashboard shows monthly sales")

month = st.selectbox("Select a Month" , ["January  " , "February" , "March" , "April"])

st.metric("Sales " , sales[month.strip()])

st.bar_chart(list(sales.values()))

