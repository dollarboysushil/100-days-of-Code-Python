service = Service(executable_path=r"C:\Users\dolla\Documents\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://google.com")

print(f"An error occurred: {e}")
