import streamlit as st
from utils.resume import to_string

st.title("Upload Your Resume")

# File uploader for PDF
uploaded_file = st.file_uploader("Choose your resume (PDF format)", type=["pdf"])

if uploaded_file is not None:
    with st.spinner("Processing your resume... Please wait."):
        resume_text = to_string(uploaded_file)  # Process the PDF
        st.session_state['resume_text'] = resume_text  # Store the extracted text
    st.success("Resume uploaded successfully!")
    st.button("Analyze Resume", on_click=lambda: st.set_page_config("Job Analysis"))
