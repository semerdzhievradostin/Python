import requests
from datetime import datetime
import credentialsconfig
import smtplib
import time
now = datetime.now()

# ------------------- ISS API to get latitude and longitude ----------------- #

api_response = requests.get(url="http://api.open-notify.org/iss-now.json")
api_response.raise_for_status()
data = api_response.json()

iss_longitude = float(data["iss_position"]["longitude"])
iss_latitude = float(data["iss_position"]["latitude"])

# ------------------- Set your Latitude and Longitude ---------------------------#
# ------------------  https://www.latlong.net/ --------------------------- #

my_latitude = 42.144920
my_longitude = 24.750320
your_city = ""

params = {
    "lat": my_latitude,
    "lng": my_longitude,
    "formatted": 0
}

sun_response = requests.get(url="https://api.sunrise-sunset.org/json", params=params)
sun_response.raise_for_status()
sun_info = sun_response.json()
sunrise = sun_info["results"]["sunrise"]
sunset = sun_info["results"]["sunset"]


# ------------------- Adjusting Sunset and Sunrise to integers ---------------------------#
# ------------------  Adding 3 hours because API only sends UTC --------------------------- #
# ------------------- Setting current hour and minute, also as integers ----------------- #

sunrise_time = (sunrise.split("T")[1].split(":")[0], sunrise.split("T")[1].split(":")[1])
sunrise_h_utc = int(sunrise_time[0])
sunrise_h_local = sunrise_h_utc + 3
sunrise_m = int(sunrise_time[1])

sunset_time = (sunset.split("T")[1].split(":")[0], sunset.split("T")[1].split(":")[1])
sunset_h_utc = int(sunset_time[0])
sunset_h_local = sunset_h_utc + 3
sunset_m = int(sunset_time[1])


local = str(now)
local_time = (local.split(" ")[1].split(":")[0], local.split(" ")[1].split(":")[1])
local_h = int(local_time[0])
local_m = int(local_time[1])


# ------------------- Check if International Space Station is overhead---------------------------#
def iss_overhead():
    if my_latitude - 5 <= iss_latitude <= my_latitude + 5 and my_longitude - 5 <= iss_longitude <= my_longitude + 5:
        return True


# ------------------- Check if it's dark---------------------------#
def is_dark():
    if local_h >= sunset_h_local and local_m >= sunset_m:
        return True


# ------------------- If it's dark and ISS is overhead ---------------------------#
# ------------------  Wait 60 sec and send an email  --------------------------- #
# ------------------- Email Configs are in credentialsconfig.py----------------- #
while True:
    if iss_overhead and is_dark:
        time.sleep(60)
        connection = smtplib.SMTP(host='smtp.gmail.com')
        connection.starttls()
        connection.login(credentialsconfig.my_email, credentialsconfig.password)
        connection.sendmail(credentialsconfig.my_email, credentialsconfig.receiver_email,
                            msg=f"Subject:ISS OVERHEAD\n\n " f"International Space Station is over the sky in {your_city}"
                            f"Look up")
        connection.close()
