"""
Streamlit app for Simulated Telco customer churn dataset
Source data: https://www.kaggle.com/datasets/blastchar/telco-customer-churn/data
"""


import streamlit as st
import os
import pandas as pd
import numpy as np


# Main page formatting
st.title('Telco Customer Churn')

# Download button (requires kaggle login)
training_data = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'training_dataframe.csv'))

st.dataframe(training_data)