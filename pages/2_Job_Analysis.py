import streamlit as st
from utils.JobCategory import Job


st.title("Resume Analysis")

if 'resume_text' not in st.session_state:
    st.error("Please upload your resume first.")
    st.stop()

resume_text = st.session_state['resume_text']
st.write("### Uploaded Resume:")
st.text_area("Resume Content", resume_text, height=200)

# Add a spinner while predicting the ideal job
with st.spinner("Analyzing your resume... Please wait."):
    ideal_job = Job(resume_text) 

# Store the ideal job in session state
st.session_state['ideal_job'] = ideal_job

st.write(f"### Your ideal job according to the analysis is: **{ideal_job}**")

st.button("Find Ideal Jobs", on_click=lambda: st.set_page_config("Job Postings"))
