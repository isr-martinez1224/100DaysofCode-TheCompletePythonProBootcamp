import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv("../../variables.env")

USERNAME = os.getenv("PIXELA_USER")
TOKEN = os.getenv("PIXELA_TOKEN")

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

post_endpoint = f"{graph_endpoint}/graph1"

today = datetime(year=2026, month=3, day=26)

post_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "15",
}

# response = requests.post(url=post_endpoint, json=post_config, headers=headers)
# print(response.text)

#print(today.strftime("%Y%m%d"))



update_endpoint = f"{post_endpoint}/20260326"

update_config = {
    "quantity": "8.7",
}

# response = requests.put(url=update_endpoint, json=update_config, headers=headers)
# print(response.text)


delete_endpoint = f"{update_endpoint}"

delete_config = {

}

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)