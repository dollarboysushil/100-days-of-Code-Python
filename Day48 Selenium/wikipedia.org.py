from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


chrome_options = Options()


service = Service(executable_path=r"C:\Users\dolla\Documents\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")



article_num = driver.find_element(By.CSS_SELECTOR,"#articlecount a")

print(article_num.text)