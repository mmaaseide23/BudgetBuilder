#######################
# Import libraries
import streamlit as st
import boto3
import pandas as pd
from botocore.exceptions import NoCredentialsError, ClientError
from datetime import datetime


#######################
# AWS configs
BUCKET_NAME = 'ds4300-finalproject-transaction'
AWS_REGION = 'us-east-2' 

st.title("📊 Company Transaction Upload Portal")

st.write("""
Upload your CSV file containing transaction data. 
The file will be stored securely in an S3 bucket for processing.
""")


#######################
# File upload and S3 upload
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    try:
        # Preview file
        df = pd.read_csv(uploaded_file)
        st.subheader("Preview:")
        st.dataframe(df.head())

        timestamp = datetime.now().strftime("%H%M%S")
        s3_key = f"transaction_{timestamp}.csv"

        # Upload to S3
        s3 = boto3.client('s3', region_name=AWS_REGION)
        with st.spinner("Uploading to S3..."):
            s3.upload_fileobj(uploaded_file, BUCKET_NAME, s3_key)

        st.success(f"✅ File successfully uploaded to S3 as: `{s3_key}`")

    except pd.errors.ParserError:
        st.error("❌ Error: The uploaded file is not a valid CSV.")
    except NoCredentialsError:
        st.error("❌ AWS credentials not found. Please check your environment or IAM configuration.")
    except ClientError as e:
        st.error(f"❌ AWS Client Error: {e.response['Error']['Message']}")
    except Exception as e:
        st.error(f"❌ Unexpected Error: {e}")
