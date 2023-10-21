from bs4 import BeautifulSoup
import requests


response = requests.get("https://www.newegg.com/nvidia-geforce-rtx-4090/p/1FT-0004-00835")

response = response.text


soup = BeautifulSoup(response , "html.parser")

price = soup.find_all(["span"],string = "$")
print(price)


