from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


file = 0
driver = webdriver.Chrome()

driver.get(f"https://www.naukri.com/ml-engineer-jobs?k=ml%20engineer")
# Wait for the element to appear (up to 10 seconds)
elem = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "srp-jobtuple-wrapper"))
)

elems = driver.find_elements(By.CLASS_NAME, "srp-jobtuple-wrapper")
print(  f"{len(elems)} items found")
for elem in elems:
    d = elem.get_attribute("outerHTML")
    with open(f"data/ml_{file}.html","w") as f:
        f.write(d)
        file += 1
        
    
#print(elem.get_attribute("outerHTML"))
#print(elem.text)
time.sleep(2)
driver.close()

