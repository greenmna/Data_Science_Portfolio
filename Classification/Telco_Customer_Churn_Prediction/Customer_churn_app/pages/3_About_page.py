"""Page detailing information about the project, including the premise, descriptions of data, and why it was done"""

import streamlit as st

st.set_page_config(
    page_title='About',
    page_icon='ℹ️'
)

st.write(
"""
# Telco Customer Churn Prediction
*For the original source, visit https://www.kaggle.com/datasets/blastchar/telco-customer-churn/data*          
""")

st.markdown(
"""
## Project Scenario
This project involves a simulated Telecommunications company
wanting to understand why customers are leaving. This project
serves as a valuable case study for real-world problems, as companies
that provide a service adhere to what are known as the four Rs:
**Relationship, Referrals, Retention, Recovery**.

Because it generally costs more (both in time and capital) to acquire
new customers versus keeping old ones, service companies seek to ensure
that customers stick around.

In this project, we play the role of a data scientist with 2 main goals:
1. Identify factors that may be contributing to customer churn
2. Design a predictive model that can be used to flag potential "flight risks"
(i.e. customers that are likely to leave)

This web app was built to simulate an in-house application for employees at Telco
to use for identifying customers who may leave the company.

### Visualize the process
**To see more on the rationale for choices made during data preprocessing and model development, 
visit my [Jupyter Notebook][1].**

[1]: <https://github.com/greenmna/Data_Science_Portfolio/blob/main/Classification/Telco_Customer_Churn_Prediction/telco_customer-churn-prediction.ipynb> "Jupyter Notebook"
"""
)