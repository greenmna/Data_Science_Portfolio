"""Page for inputting customer data that model uses to predict churn"""

import streamlit as st
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
import pickle
import os

# Required first code in separate pages
st.set_page_config(page_title='Customer Churn Predictor', 
                   page_icon='❓')

# Declare parent directory and read in training data
parent_dir = os.path.dirname(os.path.abspath(__file__))

# Load-in data and model
@st.cache_resource
def churn_prediction_model():
    model_dir = os.path.join(parent_dir, '..', 'model', 'Telco_customer_churn_model.pkl')
    with open(model_dir, 'rb') as file:
        model = pickle.load(file)
    return model

# Create same scaler and transformer used to encode categorical data and scale numeric data
@st.cache_data
def transformer_and_scaler():
    training_data = pd.read_csv(os.path.join(parent_dir, '..', 'data', 'training_dataframe.csv'))
    X = training_data.iloc[:, :-1].values
    y = training_data.iloc[:, -1].values

    ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0, 1, 2, 3, 4, 5])], remainder='passthrough')
    le = LabelEncoder()
    X = np.array(ct.fit_transform(X))
    y = le.fit_transform(y)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    sc = StandardScaler()
    X_train[:, 17:] = sc.fit_transform(X_train[:, 17:])
    
    return {'transformer':ct, 'scaler':sc}


model = churn_prediction_model()
data_manipulators = transformer_and_scaler()
transformer = data_manipulators['transformer']
scaler = data_manipulators['scaler']

# Page layout
st.markdown('# Customer Churn Predictor')
st.sidebar.header('Churn Predictor')
st.write(
    """Input a customer's information and hit the predict button
    to identify if certain customers are at risk of leaving the company."""
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
    internet_service_type = st.selectbox(label='Internet Service',
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

# Logic for processing customer data with model
if submitted:
    input_vals = [[phone_service, multiple_lines, internet_service_type,
                     contract, paperless_billing, payment_method, tenure,
                     monthly_charges, total_charges, internet_services]]
    # Check for missing values before completing prediction
    if None in input_vals[0]:
        st.write('You are missing 1 or more required inputs in this form, please check that all boxes have a value')
    else:
        model_inputs = transformer.transform(input_vals)
        model_inputs[:, 17:] = scaler.transform(model_inputs[:, 17:])

        result = model.predict(model_inputs)
        result_container = st.container()

        with result_container:
            if result == 0:
                st.markdown("""
                <div style='text-align: center; font-size: 32px;'>
                    <b>Flight risk 🚨</b>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div style='text-align: center; font-size: 32px;'>
                    <b>Safe ✅</b>
                </div>
                """, unsafe_allow_html=True)