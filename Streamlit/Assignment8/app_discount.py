import streamlit as st

product_price = st.number_input("Enter Product Price in Rs : ")
discount_percentage = st.slider("Select a discount percentage % " ,  1 , 50)
if st.button("Calculate The discounted Price !") :
    final_price = product_price - (product_price * discount_percentage / 100)
    prices = {
        "Before" : [product_price],
        "After" : [final_price]
    }
    st.success(f" Origal Price  : {product_price } \n Discount : {discount_percentage} \n Final Price : {final_price}" )
    
    st.table(prices)