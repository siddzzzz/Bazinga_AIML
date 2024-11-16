import streamlit as st
import pandas as pd

# Load job postings from a CSV file
df = pd.read_csv("data/job_postings.csv")

st.title("Job Postings")

# Display each job posting in a box
for idx, row in df.iterrows():
    with st.expander(f"**{row['Job Title']}** - {row['Company Name']}"):
        st.write(f"**Experience Required:** {row['Experience Required']}")
        st.write(f"**Salary:** {row['Salary']}")
        st.write(f"**Location:** {row['Location']}")
        st.write(f"**Posting Date:** {row['Posting Date']}")
        if st.button(f"View More Details - {row['Job Title']}", key=f"job_{idx}"):
            st.session_state['job_details'] = row.to_dict()
            st.experimental_set_page_config("Job Details")
