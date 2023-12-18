from selenium import webdriver
from selenium.webdriver.common.by import By
import time



driver = webdriver.Chrome() 
driver.get("https://en.wikipedia.org/wiki/Main_Page")



text_box =  driver.find_element(By.CLASS_NAME ,"cdx-text-input__input")
text_box.send_keys("python")

time.sleep(5)
driver.quit()