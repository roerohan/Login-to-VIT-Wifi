from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import base64


username = "" #enter your username in a string
password = "" #enter your password in a string


driver = webdriver.Chrome()
driver.get("http://phc.prontonetworks.com/cgi-bin/authlogout")
driver.get("http://phc.prontonetworks.com/cgi-bin/authlogin?URI=http://172.16.160.1/")
driver.find_element_by_name("userId").send_keys(username)
driver.find_element_by_name("password").send_keys(password)
element = driver.find_element_by_class_name("loginbutton")
element.click()
driver.quit()
