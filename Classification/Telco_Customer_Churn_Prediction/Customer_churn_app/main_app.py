"""
Streamlit app for Simulated Telco customer churn dataset
Source data: https://www.kaggle.com/datasets/blastchar/telco-customer-churn/data
"""


import streamlit as st
import os
from io import BytesIO
import pandas as pd
import numpy as np

# Functions

@st.cache_data
def load_datasets():
    raw_data = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'WA_Fn-UseC_-Telco-Customer-Churn.csv'))
    training_data = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'training_dataframe.csv'))
    
    return {'Raw data': raw_data, 'Training data':training_data}


# Initialize session_state for selectboxes
if 'data_type' not in st.session_state:
    st.session_state.data_type = None
if 'file_format' not in st.session_state:
    st.session_state.file_format = None

# Main page formatting
st.title('Telco Customer Churn')

# Container for buttons to exist in


# Select box for dataset to download
dataset_option = st.selectbox('Download Dataset', ('Raw data', 'Training data'), 
                         index=0,
                         placeholder='Select data...',
                         key='dataset_select')

if dataset_option:
    datasets = load_datasets()
    selected_data = datasets[dataset_option]

    # Dataset format select box
    dataset_format = st.selectbox(
        'Select file format',
        options = ('CSV', 'Excel', 'TSV', 'JSON'),
        index=0,
        key='format_select'
    )

    # Set outputs based on format chosen
    if dataset_format:
        output = BytesIO()

        if dataset_format == 'CSV':
            data = selected_data.to_csv(index=False).encode('utf-8')
            mime_type = 'text/csv'
            file_ext = 'csv'
        elif dataset_format == 'TSV':
            data = selected_data.to_csv(sep='\t', index=False).encode('utf-8')
            mime_type = 'text/tab-separated-values'
            file_ext = 'tsv'
        elif dataset_format == 'JSON':
            data = selected_data.to_json(indent=2).encode('utf-8')
            mime_type = 'application/json'
            file_ext = 'json'
        elif dataset_format == 'Excel':
            with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                selected_data.to_excel(writer, index=False, sheet_name='Data')
            data = output.getvalue()
            mime_type = 'application/vnd.openxmlformats-officedocument.spreadsheet.sheet'
            file_ext = 'xlsx'

        # Create download button
        st.download_button(
            label=f'Download {dataset_option} as {dataset_format}',
            data=data,
            file_name=f'{dataset_option.lower().replace(' ', '_')}.{file_ext}',
            mime=mime_type
        )

        # Preview file to be downloaded
        with st.expander("Preview Data"):
            st.dataframe(selected_data.head())