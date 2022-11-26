import requests
from datetime import datetime

USERNAME = "legendaresss"
TOKEN = "kj34hg5kj2g34jh5"
today = datetime(year=2021, month=5, day=25)

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"
#
# graph_config = {
#     "id": "graph1",
#     "name": "Running Graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "sora",
# }
#
headers = {
    "X-USER-TOKEN": TOKEN,
}
#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)



pixel_post = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10.3",
}

response = requests.put(url=graph_endpoint, json=pixel_post, headers=headers)
print(response.text)
