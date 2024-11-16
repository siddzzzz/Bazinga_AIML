import utils.webscraper as ws
import pandas as pd
df = ws.detailed_jd("https://www.naukri.com/job-listings-ml-engineer-macmillan-publishers-india-pvt-ltd-chennai-bengaluru-2-to-4-years-131124015288")

print(df)