import requests
from datetime import datetime
MYLAT= 27.700769
MYLONG=85.300140

parameters={
    "lat":MYLAT,
    "log":MYLONG,
    "formatted":0,
}

response=requests.get("https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()

data=response.json()

# print(data)

sunrise=data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset=data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)
time_now=datetime.now()
print(time_now.hour)