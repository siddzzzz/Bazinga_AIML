from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
#https://www.naukri.com/ml-engineer-jobs?k=ml%20engineer&nignbevent_src=jobsearchDeskGNB
def find_listings(category):
    query = category.split()
    query1 = "-".join(query)
    query2 = "%20".join(query)
    url = f"https://www.naukri.com/{query1}-jobs?k={query2}&nignbevent_src=jobsearchDeskGNB"
    driver = webdriver.Chrome()

    driver.get(url)
    elem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "srp-jobtuple-wrapper"))
    )

    elems = driver.find_elements(By.CLASS_NAME, "srp-jobtuple-wrapper")
    html_list = []
    for elem in elems:
        d = elem.get_attribute("outerHTML")
        html_list.append(d)
    
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

    for item in html_list:
        try:
            html_doc = item
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
    df = pd.DataFrame(data=job_details)
    driver.close()
    return df



def detailed_jd(url):
    driver = webdriver.Chrome()

    driver.get(url)
    elem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "styles_job-desc-container__txpYf"))
    )

    elems = driver.find_elements(By.CLASS_NAME, "styles_job-desc-container__txpYf")
    html_list = []
    for elem in elems:
        d = elem.get_attribute("outerHTML")
        html_list.append(d)

    for item in html_list:
        soup = BeautifulSoup(item, 'html.parser')

        # Initialize a dictionary to store the headings and their content
        job_details = {}

        # Find all sections with headings and content
        sections = soup.find_all(['h2', 'p', 'ul', 'div'], recursive=True)

        current_heading = None

        # Extract the headings and their content
        for section in sections:
            if section.name == 'h2':  # Detect headings
                current_heading = section.text.strip()
                job_details[current_heading] = []
            elif current_heading:
                # Store content under the current heading
                if section.name in ['p', 'ul']:
                    job_details[current_heading].append(section.get_text(strip=True))

        # Clean up dictionary
        job_details = {k: ' '.join(v).strip() for k, v in job_details.items() if v}

    driver.close()
    return job_details
