from selenium import webdriver
from selenium.webdriver.common.by import By
import time



driver = webdriver.Chrome() 
driver.get("https://en.wikipedia.org/wiki/Main_Page")

#button.click()

text_box =  driver.find_element(By.NAME ,"search")
text_box.send_keys("python")

time.sleep(5)
driver.quit()