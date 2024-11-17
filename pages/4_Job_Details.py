import streamlit as st
import utils.webscraper as ws
import utils.gemeni as gem

if 'job_details' not in st.session_state:
    st.error("No job details available.")
    st.stop()

job_details = st.session_state['job_details']

details = ws.detailed_jd(job_details["Job Link"])
for key,val in details.items():
    info = f"**{key}:** {val}"
    formatted_info = gem.get_gemini_response(f"Format the text - {info}")
resume_text = st.session_state['resume_text']
# Check if job details are available in session state
if formatted_info is None:
    score =  gem.get_gemini_response(f"This is my resume{resume_text}, score on similarity with the job description - {details}, just output the score")
else:
    score =  gem.get_gemini_response(f"This is my resume{resume_text}, score on similarity with the job description - {formatted_info}, just output the score")

# Display detailed information about the selected job
st.title(f"Job Details: {job_details['Job Title']}")
st.title(f"**Relevance Score is:** {score}")
st.write(f"**Job Title:** {job_details['Job Title']}")
st.write(f"**Company Name:** {job_details['Company Name']}")
st.write(f"**Experience Required:** {job_details['Experience Required']}")
st.write(f"**Salary:** {job_details['Salary']}")
st.write(f"**Location:** {job_details['Location']}")
st.write(f"{formatted_info}")
str_gap = gem.get_gemini_response(f"This is my resume {resume_text}, this is the job description {formatted_info}, Tell me in points what are the stregths and gaps in the resume, and another point on how i should inprove them")
st.write(f"{str_gap}")