import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model/sales_model.pkl")

st.title("Smart Sales Forecast Dashboard")

st.write("Predict future sales based on month, quantity and price")

month = st.number_input("Month (1-12)",1 ,12, 6)
quantity = st.number_input("Quantity", 1, 50, 5)
price =  st.number_input("Price", 100, 100000, 20000)

if st.button("Predict Sales"):
    input_data = pd.DataFrame({'Month':[month], 'Quantity':[quantity], 'Price':[price]})
    
    prediction = model.predict(input_data)
    st.success(f"Predict Sales: Rs {int(prediction[0])}")