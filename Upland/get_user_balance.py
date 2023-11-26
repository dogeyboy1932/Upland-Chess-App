import requests


def GetUserBalance(upland_access_token, upland_user_id):
    url = 'https://api.sandbox.upland.me/developers-api/user/balances'

    headers = {
        'Authorization': f'Bearer {upland_access_token}',
        'UserId': upland_user_id,
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data['availableUpx']

    else:
        print(f'Request failed with status code {response.status_code}')



# def run():
#     upland_access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiI0ODI5OGVhMC0yNDBhLTExZWUtOWMwNC1iMzcyMDk2MTViOGIiLCJhcHBJZCI6MjMyLCJ0b2tlbklkIjoiZGEwZDk4N2ItZjUyMi00YTVlLTliOGEtMmQzNDk5ZWZjODkwIiwiaWF0IjoxNzAwMDY2ODg0fQ.AHt_xck24NiQlAKAiNIrCH4ZRVkaYrWbzjplz8y6Yxk"
#     upland_user_id = "48298ea0-240a-11ee-9c04-b37209615b8b"
#
#     get_user_balance(upland_access_token, upland_user_id)
#
#
# run()