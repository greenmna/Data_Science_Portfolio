"""
Streamlit app for Simulated Telco customer churn dataset
Source data: https://www.kaggle.com/datasets/blastchar/telco-customer-churn/data
"""


import streamlit as st
import pandas as pd
import numpy as np


# Main page formatting
st.title('Telco Customer Churn')

# Download button (requires kaggle login)
raw_data = pd.read_csv('https://github.com/greenmna/Data_Science_Portfolio/blob/main/Classification/Telco_Customer_Churn_Prediction/WA_Fn-UseC_-Telco-Customer-Churn.csv')
training_data = pd.read_csv('https://github.com/greenmna/Data_Science_Portfolio/blob/main/Classification/Telco_Customer_Churn_Prediction/Customer_churn_app/training_dataframe.csv')

st.dataframe(training_data)