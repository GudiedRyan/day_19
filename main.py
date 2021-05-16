import requests
from datetime import datetime
from config import email


MY_LAT = 40.7934
MY_LONG = -77.8600

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
def check_distance():
    lat_dist = MY_LAT - iss_latitude
    lng_dist = MY_LONG - iss_longitude
    if abs(lat_dist) <= 5 and abs(lng_dist) <= 5:
        return True
    else:
        return False

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


time_now = datetime.now()
now = time_now.hour

def check_night():
    if sunrise < now < sunset:
        return False
    else:
        return True


def run():
    if check_distance() and check_night():
        email()

run()