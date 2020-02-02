from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import base64
from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv(verbose=True)

env_path = Path('.') / '.env'

load_dotenv(dotenv_path=env_path)

def getenv(var_name):
    return os.getenv(var_name)

username = getenv("USERNAME")
password = getenv("PASSWORD")

driver = webdriver.Chrome()
driver.get("http://phc.prontonetworks.com/cgi-bin/authlogout")
driver.get("http://phc.prontonetworks.com/cgi-bin/authlogin?URI=http://172.16.160.1/")
driver.find_element_by_name("userId").send_keys(username)
driver.find_element_by_name("password").send_keys(password)
element = driver.find_element_by_class_name("loginbutton")
element.click()
driver.quit()
