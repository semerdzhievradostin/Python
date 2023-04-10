from datetime import datetime
import requests


#https://pixe.la/
TOKEN = "TYPE at least 8 symbols for token"
USER = "YOURUSERNAME"
GRAPH_ID = "graph ID"


pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

pixela_registration = requests.post(pixela_endpoint, json=user_params)

graph_params = {
    "id": "giti1",
    "name": "GitLike",
    "unit": "commit",
    "type": "int",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

graph_endpoint = f"{pixela_endpoint}/{USER}/graphs"
gr = requests.post(graph_endpoint, json=graph_params, headers=headers)
print(gr.text)


today = datetime.now()
commits = input("How many commits today?\n")
graph_add = {
    "date": today.strftime("%Y%m%d"),
    "quantity": commits,
}



graph_post = f"{pixela_endpoint}/{USER}/graphs/{GRAPH_ID}"
gr_add = requests.post(graph_post, json=graph_add, headers=headers)
print(gr_add.text)


#https://pixe.la/