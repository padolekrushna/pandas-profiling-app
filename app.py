import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# App title
st.title("Excel File Profiling App")

# File uploader
uploaded_file = st.file_uploader("Upload an Excel file for Profiling", type=["xlsx"])

if uploaded_file:
    # Read the uploaded file into a DataFrame
    df = pd.read_excel(uploaded_file)
    st.write("## Preview of the Uploaded Dataset")
    st.dataframe(df)

    # Generate and display profile report
    st.write("## Dataset Profiling Report")
    profile = ProfileReport(df, title="Dataset Profiling Report", explorative=True)
    st_profile_report(profile)

    # Save the report to a file
    with open("dataset_profile_report.html", "wb") as f:
        profile.to_file(f)
    st.write("### Download the Profile Report")
    st.download_button(
        label="Download Report",
        data=open("dataset_profile_report.html", "rb"),
        file_name="dataset_profile_report.html",
        mime="text/html",
    )
