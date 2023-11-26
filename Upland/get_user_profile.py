import requests


def GetUserProfile(upland_access_token, upland_user_id):
    url = 'https://api.sandbox.upland.me/developers-api/user/profile'

    headers = {
        'Authorization': f'Bearer {upland_access_token}',
        'UserId': upland_user_id,
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f'Request failed with status code {response.status_code}')


# def run():
#     upland_access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiI0ODI5OGVhMC0yNDBhLTExZWUtOWMwNC1iMzcyMDk2MTViOGIiLCJhcHBJZCI6MjMyLCJ0b2tlbklkIjoiMjcyMTA5MTQtZTUwZS00OTA5LTg4MjItMjQ1ZDEwZGM3YjA3IiwiaWF0IjoxNzAwMzIxMjI1fQ.3GsbdV72G3tjdwkzwqEMWhJg0xpTCRe9DUHnazbcyrU"
#     upland_user_id = "48298ea0-240a-11ee-9c04-b37209615b8b"
#
#     get_user_profile(upland_access_token, upland_user_id)
#
#


# run()