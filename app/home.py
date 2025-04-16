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
    initial_sidebar_state="expanded"
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
# Sidebar Navigation 
with st.sidebar:
    st.title("📂 Navigation")
    st.page_link("home.py", label="Upload CSV", icon="📤")
    st.page_link("pages/email.py", label="Send Emails", icon="📬")
    st.page_link("pages/analysis.py", label="Advanced Analysis", icon="📊")

#######################
# Header & Branding
st.markdown('<div class="logo">💰 TransactionTracker</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Smart Tracking Starts Here</div>', unsafe_allow_html=True)

#######################
# Page content
with st.container():
    st.markdown("### 📁 Upload Your Transaction CSV")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    submit = st.button("Submit File")

    if submit and uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.subheader("Preview of Uploaded File:")
            st.dataframe(df.head())

            # Generate readable filename
            timestamp = datetime.now().strftime("%H%M%S")
            s3_key = f"uploads/transaction_{timestamp}.csv"

            s3 = boto3.client('s3', region_name=AWS_REGION)
            with st.spinner("Uploading to S3..."):
                s3.upload_fileobj(uploaded_file, BUCKET_NAME, s3_key)

            st.success(f"✅ File `{uploaded_file.name}` uploaded successfully to S3 as `{s3_key}`")

        except pd.errors.ParserError:
            st.error("❌ Error: The uploaded file is not a valid CSV.")
        except NoCredentialsError:
            st.error("❌ AWS credentials not found. Please check your environment or IAM configuration.")
        except ClientError as e:
            st.error(f"❌ AWS Client Error: {e.response['Error']['Message']}")
        except Exception as e:
            st.error(f"❌ Unexpected Error: {e}")
    elif submit and uploaded_file is None:
        st.warning("⚠️ Please select a file before submitting.")

#######################
# Footer / Contributors
st.markdown("""
    <div class="footer">
        Created by Michael Maaseide, Sam Baldwin, Alex Tu, and Jeffrey Krapf<br>
        Northeastern University · DS4300 Final Project
    </div>
""", unsafe_allow_html=True)