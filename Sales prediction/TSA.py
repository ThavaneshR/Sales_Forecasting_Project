# -*- coding: utf-8 -*-
"""
Created on Sun May 26 12:28:03 2024

@author: Thavanesh
"""

import streamlit as st
import pickle
pickel_in=open("TSAmodel.pkl","rb")
model=pickle.load(pickel_in)
def predict_sales(date):
    prediction=model.predict(start='1972-09-01',end=date,dynamic=True)
    print(prediction[-1])
    return prediction
st.title("Sales Prediction")
in_date=st.text_input("Date",placeholder="Year-Month-Date  (from 1972-10-01)")
result=""
ans=""

if st.button("Predict"):
    result=predict_sales(in_date)
    ans=round(result[-1],2)
    st.success("The predicted Sale is {}".format(ans))

if st.button("Show Graph"):
    result=predict_sales(in_date)
    ans=round(result[-1],2)
    st.success("The predicted Sale is {}".format(ans))
    st.line_chart(predict_sales(in_date))



