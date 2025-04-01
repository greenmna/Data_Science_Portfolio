"""Page for inputting customer data that model uses to predict churn"""

import streamlit as st

st.set_page_config(page_title='Customer Churn Predictor', 
                   page_icon='❓')

# Page layout
st.markdown('# Customer Churn Predictor')
st.sidebar.header('Churn Predictor')
st.write(
    """Input a customer's information and hit the **predic** button
    to identify if certain customers are at risk of leaving the company"""
)