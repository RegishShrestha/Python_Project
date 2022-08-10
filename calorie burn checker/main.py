
import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime
import os
GENDER = 'male'
WEIGHT_KG = 70
HEIGHT_CM = 14
AGE = 20

# hide this using os

# APP_ID="449fdf7d"
# API_KEY="b784f925cc03c07e88548bc8a1090bcf"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

tokken=os.environ.get("token")
sheet_endpoint=f"https://api.sheety.co/{tokken}/myWorkouts/sheet1"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": os.environ.get("APP_ID"),
    "x-app-key": os.environ.get("API_KEY"),
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "sheet1": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

# sheet_response = requests.post(sheet_endpoint, json=sheet_inputs,auth=(
#     "shresthapython",
#     "1234abcd()"
# ))

bearer_headers = {"Authorization": f'Bearer {os.environ.get("bearerpass")}'}

sheet_response = requests.post(sheet_endpoint, json=sheet_inputs,headers=bearer_headers)
print(sheet_response.text)


