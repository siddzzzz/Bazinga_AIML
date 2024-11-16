from bs4 import BeautifulSoup
import os
import pandas as pd
job_details = {
            "Job Title": [],
            "Job Link": [],
            "Company Name": [],
            "Experience Required": [],
            "Salary": [],
            "Location": [],
            "Job Description": [],
            "Posting Date": []
        }

for file in os.listdir("data"):
    try:
        with open(f"data/{file}") as f:
            html_doc = f.read()
        soup = BeautifulSoup(html_doc,"html.parser")
        title_element = soup.find('a', class_='title')
        job_title = title_element.get_text(strip=True) if title_element else None
        job_details["Job Title"].append(job_title)

        job_link = title_element['href'] if title_element and 'href' in title_element.attrs else None
        job_details["Job Link"].append(job_link)
        
        # Extract the company name
        company_element = soup.find('a', class_='comp-name')
        company_name = company_element.get_text(strip=True) if company_element else None
        job_details["Company Name"].append(company_name)

        # Extract the experience required
        experience_element = soup.find('span', class_='expwdth')
        experience = experience_element.get_text(strip=True) if experience_element else None
        job_details["Experience Required"].append(experience)
        # Extract the salary range
        salary_element = soup.find('span', class_='sal')
        salary = salary_element.get_text(strip=True) if salary_element else None
        job_details["Salary"].append(salary)

        # Extract the location
        location_element = soup.find('span', class_='locWdth')
        location = location_element.get_text(strip=True) if location_element else None
        job_details["Location"].append(location)

        # Extract the job description
        description_element = soup.find('span', class_='job-desc')
        job_description = description_element.get_text(strip=True) if description_element else None
        job_details["Job Description"].append(job_description)

        # Extract the posting date
        posting_date_element = soup.find('span', class_='job-post-day')
        posting_date = posting_date_element.get_text(strip=True) if posting_date_element else None
        job_details["Posting Date"].append(posting_date)

    except Exception as e:
        print(e)

#print(soup.prettify())
df = pd.DataFrame(data = job_details)
df.to_csv("Data.csv")