import streamlit as st
import boto3
import uuid
import pandas as pd
from botocore.exceptions import NoCredentialsError, ClientError
from datetime import datetime

# Set page config and dark green theme
st.set_page_config(
    page_title="BudgetBuilder Upload",
    page_icon="💰",
    layout="centered",
    initial_sidebar_state="collapsed"
)

#######################
# Custom CSS Styling
st.markdown("""
    <style>
        body {
            background-color: #eaf4ec;
            font-family: 'Segoe UI', sans-serif;
        }
        .title {
            font-size: 3em;
            font-weight: bold;
            color: #1e5631;
            text-align: center;
            margin-top: 0.5em;
        }
        .subtitle {
            font-size: 1.2em;
            text-align: center;
            margin-bottom: 1em;
            color: #4f775c;
        }
        .footer {
            margin-top: 3em;
            font-size: 0.9em;
            color: #6c8f76;
            text-align: center;
        }
        .logo {
            text-align: center;
            font-size: 2em;
            font-weight: 800;
            color: #1e5631;
            margin-top: 1em;
        }
        .stButton>button {
            background-color: #4f775c;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 0.5em 1.5em;
        }
        .stButton>button:hover {
            background-color: #3d5f4b;
        }
        [data-testid="stSidebarNav"] {
            display: none !important;
        }
    </style>
""", unsafe_allow_html=True)

#######################
# AWS configs
BUCKET_NAME = 'ds4300-finalproject-transaction'
AWS_REGION = 'us-east-2'

#######################
# Sidebar Navigation Replacement
with st.sidebar:
    st.title("📂 Navigation")
    st.page_link("home.py", label="Upload CSV", icon="📤")
    st.page_link("pages/email.py", label="Send Emails", icon="📬")
    st.page_link("pages/analysis.py", label="Advanced Analysis", icon="📊")

#######################
# Header & Branding
st.markdown('<div class="logo">Send Outreach Emails</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Smart Transactions Start Here</div>', unsafe_allow_html=True)

#######################
# Upload Page Content inside card


#######################
# Footer / Contributors
st.markdown("""
    <div class="footer">
        Created by Michael Maaseide, Sam Baldwin, Alex Tu, and Jeffrey Krapf<br>
        Northeastern University · TransactionTracker
        
    </div>
""", unsafe_allow_html=True)
