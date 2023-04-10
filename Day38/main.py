import credentials
import requests
from datetime import datetime
GENDER = "MALE"
WEIGHT = "85"
HEIGHT = "183"
AGE = "24"


currentDateAndTime = datetime.now()
currentTime = currentDateAndTime.strftime("%H:%M:%S")
currentDate = currentDateAndTime.strftime("%d/%m/%Y")


sheet_url = f"https://api.sheety.co/{credentials.sheet_key}/{credentials.sheet_project}/{credentials.sheet_name}"
nutri_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise = input("Tell me what exercise you did?\n")
headers = {
    "x-app-id": credentials.nutri_id,
    "x-app-key": credentials.nutri_key,
    "x-remote-user-id": credentials.nutri_user,
}
parameters = {
    "query": exercise,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}


response = requests.post(url=nutri_endpoint, json=parameters, headers=headers)
response.raise_for_status()
result = response.json()
exercises = result["exercises"][0]
user_exercise = exercises["name"].title()
exercise_duration_min = exercises["duration_min"]
calories_burned = exercises["nf_calories"]

post_body = {
    "workout": {
        "Date": currentDate,
        "Time": currentTime,
        "Exercise": user_exercise,
        "Duration": exercise_duration_min,
        "Calories": calories_burned,
    }
}
