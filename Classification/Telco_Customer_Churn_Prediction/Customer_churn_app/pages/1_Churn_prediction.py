"""Page for inputting customer data that model uses to predict churn"""

import streamlit as st
import pickle
import os
import xgboost

# Required first code in separate pages
st.set_page_config(page_title='Customer Churn Predictor', 
                   page_icon='❓')

# Load-in model
@st.cache_resource
def churn_prediction_model():
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    model_dir = os.path.join(parent_dir, '..', 'model', 'Telco_customer_churn_model.pkl')
    with open(model_dir, 'rb') as file:
        model = pickle.load(file)
    return model


model = churn_prediction_model()

# Page layout
st.markdown('# Customer Churn Predictor')
st.sidebar.header('Churn Predictor')
st.write(
    """Input a customer's information and hit the **predic** button
    to identify if certain customers are at risk of leaving the company"""
)