import time

import requests
from datetime import datetime
import smtplib

my_email="barbarika2004@gmail.com"
password="szpn vnxq eppl uyxj"

# response=requests.get(url="http://api.open-notify.org/iss-now.json")
# # if response.status_code==400:
# #     raise Exception("Bad")
# # elif response.status_code==404:
# #     raise  Exception("not rigght")
# response.raise_for_status()# to raise exception itself
# data=response.json()
#
# iss_position=(longitude,latitude)

my_lat=12.971599
my_long=12.971599
def iss_overhead():
    response=requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data=response.json()
    iss_longitude=float(data["iss_position"]["longitude"])
    iss_latitude=float(data["iss_position"]["latitude"])
    if my_lat-5  <=iss_latitude<=my_lat+5 and my_long-5<=iss_longitude<=my_long+5:
        return  True

def is_night():
    parameters = {
        "lat": my_lat,
        "lng": my_long,
        "formatted": 0,
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise=int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset=int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now=datetime.now().hour
    if time_now>=sunrise or time_now<=sunset:
        return True
while True:
    time.sleep(60)
    if iss_overhead() and is_night():
        connection=smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(my_email,password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg="Subject:Look up to sky\n\n the iss is above in sky."
        )


