import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
import tempfile

# App title
st.title("Excel File Profiling App")

# File uploader
uploaded_file = st.file_uploader("Upload an Excel file for Profiling", type=["xlsx"])

if uploaded_file:
    # Read the uploaded file into a DataFrame
    df = pd.read_excel(uploaded_file)
    st.write("## Preview of the Uploaded Dataset")
    st.dataframe(df)

    # Generate profile report
    st.write("## Dataset Profiling Report")
    profile = ProfileReport(df, title="Dataset Profiling Report", explorative=True)

    # Save the profile report to a temporary HTML file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as tmp_file:
        profile.to_file(tmp_file.name)
        tmp_file_path = tmp_file.name

    # Create a download button for the report
    with open(tmp_file_path, "rb") as f:
        st.download_button(
            label="Download Profile Report",
            data=f,
            file_name="dataset_profile_report.html",
            mime="text/html",
        )
