import requests
from datetime import datetime
import smtplib
import time

PASSWORD = "cqoaeyrmeskagpyi"

MY_LAT = 29.767954
MY_LONG = -95.366821



#Your position is within +5 or -5 degrees of the ISS position.
def iss_near_me():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print(f"Latitude: {iss_latitude}, Longitude: {iss_longitude}")

    if (iss_latitude - 5.0) <= MY_LAT <= (iss_latitude + 5.0) and (iss_longitude - 5.0) <= MY_LONG <= (iss_longitude + 5.0):
        print("ISS is near your position! Look up!")
        return True
    else:
        print("ISS is not near your coordinates")
        return False

def send_email():
    my_email = "martinez.2400.i@gmail.com"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()  # secures our connection to the servers MOST IMPORTANT
        connection.login(user=my_email, password=PASSWORD)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg=f"Subject:ISS Visible!\n\nThe ISS is visible in your area, look up!")
    connection.close()

def night():
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

    time_now = datetime.now().hour
    print(time_now)
    print(f"Sunrise: {sunrise}, Sunset: {sunset}")

    if sunset <= time_now or time_now <= sunrise:
        print("It is dark enough to see ISS")
        return True
    else:
        print("It is not dark to see ISS")
        return False



#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.




while True:
    if iss_near_me() and night():
        send_email()
    time.sleep(60)