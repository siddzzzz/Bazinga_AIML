import streamlit as st
import pandas as pd
import time  # Simulate delay for web scraping
import utils.webscraper as ws


# Check if the ideal job is in session state
if 'ideal_job' not in st.session_state:
    st.error("Please complete the job analysis first.")
    st.stop()

ideal_job = st.session_state['ideal_job']

# Cached data-fetching function
@st.cache_data
def fetch_job_postings(ideal_job):
    """Fetch job postings based on the ideal job."""
    time.sleep(10)  # Simulate scraping delay
    # Replace this with actual scraping/loading logic
    return ws.find_listings(ideal_job)

# Fetch data (uses cache if data is already fetched)
with st.spinner("Fetching job postings... This might take up to 20 seconds."):
    df = fetch_job_postings(ideal_job)

# Display each job posting in a box
for idx, row in df.iterrows():
    with st.expander(f"**{row['Job Title']}** - {row['Company Name']}"):
        st.write(f"**Experience Required:** {row['Experience Required']}")
        st.write(f"**Salary:** {row['Salary']}")
        st.write(f"**Location:** {row['Location']}")
        st.write(f"**Job Description:** {row['Job Description']}")
        st.write(f"**Posting Date:** {row['Posting Date']}")
        if st.button(f"View More Details - {row['Job Title']}", key=f"job_{idx}"):
            st.session_state['job_details'] = row.to_dict()
            st.session_state['current_page'] = "Job Details"  # Set the page to Job Details
            st.rerun()  # Trigger a re-run to switch pages
