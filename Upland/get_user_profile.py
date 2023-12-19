from FIXED_VARIABLES import conn
import json


def GetUserProfile(upland_access_token, upland_user_id):
    payload = ""
    headers = {
        'Authorization': f'Bearer {upland_access_token}',
    }

    conn.request("GET", "/developers-api/user/profile", payload, headers)
    response = conn.getresponse()
    data = json.loads(response.read().decode("utf-8"))

    if response.status == 200:
        # print(data)
        return data
    else:
        print(f'Request failed with status code {response.status}')


def run():
    upland_access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiI0ODI5OGVhMC0yNDBhLTExZWUtOWMwNC1iMzcyMDk2MTViOGIiLCJhcHBJZCI6MjMyLCJ0b2tlbklkIjoiZWY2MWEwY2MtMjgyMC00Y2FhLTkwODktOGZhMTdkY2EzMTY2IiwiaWF0IjoxNzAxNTUzMzY5fQ.0zKCRi2lxIsftkN_XdrB-tg_bY6hDLkltd3LRXDlNno"
    upland_user_id = "48298ea0-240a-11ee-9c04-b37209615b8b"

    GetUserProfile(upland_access_token, upland_user_id)


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
