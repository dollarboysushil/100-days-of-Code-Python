from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Create ChromeOptions object
chrome_options = Options()

# Add any options you need (e.g., for headless mode)
# chrome_options.add_argument("--headless")


service = Service(executable_path=r"C:\Users\dolla\Documents\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https:python.org")

names =driver.find_elements(By.CSS_SELECTOR,'.event-widget li a')
for name in names:
    
    print(name.text)


