import json

from FIXED_VARIABLES import conn


def GetUserProfile(upland_access_token):
    payload = ""
    headers = {
        'Authorization': f'Bearer {upland_access_token}',
    }

    conn.request("GET", "/developers-api/user/profile", payload, headers)
    response = conn.getresponse()
    data = json.loads(response.read().decode("utf-8"))

    if response.status == 200:
        return data
    else:
        print(f'Request failed with status code {response.status}')


def run():
    upland_access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiI0ODI5OGVhMC0yNDBhLTExZWUtOWMwNC1iMzcyMDk2MTViOGIiLCJhcHBJZCI6MjMyLCJ0b2tlbklkIjoiMGYxMzgzMjItODMxNC00NDdhLTk5MTktY2M4Mjk4OWFlYzkwIiwiaWF0IjoxNzEzMzY5NDE0fQ.AIueKuWTSSe1MjrrCeU-RGGbrr3v2rdoHHymgYqq4tU"
    upland_user_id = "48298ea0-240a-11ee-9c04-b37209615b8b"

    print(GetUserProfile(upland_access_token))


# run()


# OLD CODE:
# url = 'https://api.sandbox.upland.me/developers-api/user/profile'

# headers = {
#     'Authorization': f'Bearer {upland_access_token}',
#     'UserId': upland_user_id,
# }

# response = requests.get(url=url, headers=headers)

# if response.status_code == 200:
#     return response.json()
# else:
#     print(f'Request failed with status code {response.status_code}')
