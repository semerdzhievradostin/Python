import requests

# ------------------- If you wish to change the questions go to https://opentdb.com/api_config.php ---------- #
# ------------------- And choose of your liking, then paste the API below ----------------------------------- #

api_request = requests.get("https://opentdb.com/api.php?amount=50&difficulty=medium&type=boolean")
api_request.raise_for_status()
data = api_request.json()

question_data = data["results"]

