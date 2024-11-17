import utils.webscraper as ws
import pandas as pd
import utils.gemeni as gemeni
df = ws.detailed_jd("https://www.naukri.com/job-listings-ml-engineer-macmillan-publishers-india-pvt-ltd-chennai-bengaluru-2-to-4-years-131124015288")

response = gemeni.get_gemini_response("Tell me about what is resume")
print(response)