from bs4 import BeautifulSoup
import pandas as pd
import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
import math
import time
from pyvirtualdisplay import Display
start_time = time.perf_counter ()

   
display = Display(visible=0, size=(800, 600))
display.start()


# Set up the driver (change path to the location of your own driver executable)
#driver = webdriver.Chrome('path/to/chromedriver')
pathurl="/home/ajay/chromedriver_linux64/chromedriver"


# In[40]:


driver = webdriver.Chrome(executable_path=pathurl)

# Navigate to LeetCode login page
driver.implicitly_wait(10) 
driver.get('https://leetcode.com/accounts/login/')

# Fill in username and password
username=input("Enter your leetcode username: ")
password=getpass.getpass('Password:')
username_field = driver.find_element_by_xpath('//input[@name="login"]')
username_field.send_keys(username)

password_field = driver.find_element_by_xpath('//input[@name="password"]')
password_field.send_keys(password)

# Submit the form
password_field.send_keys(Keys.RETURN)

try:
    element = WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.ID, "initial-loading"))
    )
except:
    print("Timed out waiting for page to load")
  
driver.get("https://leetcode.com/api/problems/algorithms/")
text=driver.page_source
text=text.strip().replace('<html>','')
text=text.replace('<head>','')
text=text.replace('</head>','')
text=text.replace('<body>','')
text=text.replace('</body>','')
text=text.replace('</html>','')
text_json=json.loads(text)
no_of_problems=text_json["num_solved"]
texttemp=[]
for i in range(len(text_json["stat_status_pairs"])):
    textarr=[]
    textarr.append(text_json["stat_status_pairs"][i]["stat"]["question_id"])
    textarr.append(text_json["stat_status_pairs"][i]["stat"]["question__title"])
    textarr.append(text_json["stat_status_pairs"][i]["difficulty"]["level"])
    textarr.append(text_json["stat_status_pairs"][i]['status'])
    texttemp.append(textarr)
df=pd.DataFrame(texttemp)   
df.columns=["question_id","title","difficulty","submission_status"]
df.to_csv("tryingoutleetcodefinal.csv",index=False)
