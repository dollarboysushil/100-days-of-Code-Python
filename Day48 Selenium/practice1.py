import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('https://secure-retreat-92358.herokuapp.com/')



fname = driver.find_element(By.NAME,"fName")
fname.send_keys("Sushil")


sname = driver.find_element(By.NAME,'lName')
sname.send_keys("Poudel")

email = driver.find_element(By.NAME ,"email")
email.send_keys("email@email.com")

btn = driver.find_element(By.CLASS_NAME,"btn")
btn.click()

time.sleep(10)

