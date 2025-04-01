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
    """Input a customer's information and hit the predict button
    to identify if certain customers are at risk of leaving the company"""
)

# Form for churn prediction
with st.form('Churn Prediction Form'):
    st.header('Customer Information')

    # Selectbox Options
    phone_service = st.selectbox(label='Phone Service', 
                                options=('Yes', 'No'),
                                index=0,
                                placeholder='Select option...',
                                key='PhoneService')
    multiple_lines = st.selectbox(label='Multiple Phone Lines',
                                options=('No phone service', 'Yes', 'No'),
                                index=0,
                                placeholder='Select option...',
                                key='MultipleLines')
    internet_service = st.selectbox(label='Internet Service',
                                    options=('No', 'DSL', 'Fiber optic'),
                                    index=0,
                                    placeholder='Select option...',
                                    key='InternetService')
    contract = st.selectbox(label='Contract type',
                            options=('Month-to-month', 'One year', 'Two year'),
                            index=0,
                            placeholder='Select option...',
                            key='Contract')
    paperless_billing = st.selectbox(label='Paperless Billing',
                                    options=('Yes', 'No'),
                                    index=0,
                                    placeholder='Select option...',
                                    key='PaperlessBilling')
    payment_method = st.selectbox(label='Payment Method',
                                options=('Electronic check', 'Mailed check', 'Bank transfer', 'Credit card'),
                                index=0,
                                placeholder='Select option...',
                                key='PaymentMethod')
    # Numeric inputs
    tenure = st.number_input(label='Tenure',
                             min_value=1,
                             max_value=100,
                             value=None,
                             placeholder='Type a whole number...',
                             key='tenure')
    monthly_charges = st.number_input(label='Monthly Charges',
                                      min_value=0.0,
                                      max_value=None,
                                      value=None,
                                      format='%.2f',
                                      placeholder='Enter monthly charges...',
                                      key='MonthlyCharges')
    total_charges = st.number_input(label='Total Charges',
                                    min_value=0.0,
                                    max_value=None,
                                    value=None,
                                    format='%.2f',
                                    placeholder='Enter total charges...',
                                    key='TotalCharges')
    internet_services = st.number_input(label='Number of Internet Services',
                                        min_value=0,
                                        max_value=6,
                                        value=0,
                                        key='InternetServiceCount')

    submitted = st.form_submit_button("Predict")