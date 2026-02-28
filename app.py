import streamlit as st
import numpy as np

st.title("Customer Subscription Prediction")

# Input fields
age = st.number_input("Enter Age", min_value=18, max_value=100)
purchase = st.number_input("Enter Purchase Amount", min_value=0)

# Prediction logic
if st.button("Predict"):
    if age > 30 and purchase > 500:
        st.success("Customer will Subscribe")
    else:
        st.error("Customer will NOT Subscribe")
