import requests
from datetime import datetime



parameters = {
    "lat":28.394857,
    "lng":84.124008,
    "formatted":0,
}

response = requests.get("https://api.sunrise-sunset.org/json" , params=parameters)
response.raise_for_status()

data= response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])






time_now = datetime.now()
print(time_now)


