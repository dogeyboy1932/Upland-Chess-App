import requests
import json


def CreateEscrowContainer():
    url = "https://api.sandbox.upland.me/developers-api/containers"

    payload = json.dumps({
      "expirationPeriodHours": 24,
      "userLimitByContainer": 2
    })

    headers = {
      'Content-Type': 'application/json',
      'Authorization': 'Basic MjMyOmVjMjFlZmZlLTYyZDktNDAzZi04MTc3LTEwODdjMWJlNmJjYw==',
      'Cookie': 'sticky-session-1=1699553168.246.2069.619172|aebf5e9dc298523c710b3cfe411c6704'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    data = response.json()

    print(data)

    return data['id']


# def run():
#     val = CreateEscrowContainer()
#
#     print(val)
#
#
# run()



# def create_escrow(upland_user_id, upland_access_token):
#     url = 'https://api.sandbox.upland.me/developers-api/containers'
#     headers = {
#         'Authorization': f'Bearer {upland_access_token}',
#         'UserId': upland_user_id,
#         'Content-Type': 'application/json'
#     }
#
#     payload = json.dumps({"userLimitByContainer": 2})
#
#     response = requests.post(url, headers=headers, data=payload)
#
#     data = response.json()
#
#     if response.status_code == 200:
#         escrow_id = data.get('appId')
#         print("AppID:", escrow_id)
#     else:
#         print(f'Request failed with status code {response.status_code}')
#         print("Response:", data)
#
#
# def run():
#     upland_access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiI0ODI5OGVhMC0yNDBhLTExZWUtOWMwNC1iMzcyMDk2MTViOGIiLCJhcHBJZCI6MjMyLCJ0b2tlbklkIjoiYTdkNmFiNTktZGIxZi00MDZjLWE2MGQtM2I4YThkMWU0ODY5IiwiaWF0IjoxNzAwMzI5MjQxfQ.G_6LVuSQCf4-ClpRa2jjMDekYMJVTHx22cVzjLUBWn0"
#     upland_user_id = "48298ea0-240a-11ee-9c04-b37209615b8b"
#
#     appID = "232"
#     access_token = "5e61f73b-da0c-4c9e-8d5e-7a028e03d7ae"
#
#     create_escrow(upland_user_id, upland_access_token)
#
#
# run()
