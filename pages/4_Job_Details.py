import streamlit as st
import utils.webscraper as ws

# Check if job details are available in session state
if 'job_details' not in st.session_state:
    st.error("No job details available.")
    st.stop()

job_details = st.session_state['job_details']

details = ws.detailed_jd(job_details["Job Link"])

# Display detailed information about the selected job
st.title(f"Job Details: {job_details['Job Title']}")

st.write(f"**Job Title:** {job_details['Job Title']}")
st.write(f"**Company Name:** {job_details['Company Name']}")
st.write(f"**Experience Required:** {job_details['Experience Required']}")
st.write(f"**Salary:** {job_details['Salary']}")
st.write(f"**Location:** {job_details['Location']}")
for key,val in details.items():
    st.write(f"**{key}:** {val}")