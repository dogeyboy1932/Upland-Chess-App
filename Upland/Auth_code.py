# import requests
import base64
from FIXED_VARIABLES import conn
import json


def Verify(credential):
    payload = ''
    headers = {
        'Authorization': f'Basic {credential}',
        'Cookie': 'sticky-session-1=1701556690.435.2069.742375|9a5cc3e4d08faea009d8e16f5c97bee9'
    }

    conn.request("POST", "/developers-api/auth/otp/init", payload, headers)
    response = conn.getresponse()

    if response.status == 200 or response.status == 201:
        data = json.loads(response.read().decode("utf-8"))
        code = data['code']

        return f"{code}"
    else:
        print(f'Request failed with status code {response.status}')


def run():
    app_id = "232"
    key = "ad331091-4762-4fe1-b40f-1d4ca0d02d9f"

    credential = base64.b64encode(f'{app_id}:{key}'.encode('utf-8')).decode('utf-8')

    Verify(credential)


# run()


# Old Code:
#
# def run():
#   app_id_ = app_id
#   secret_key_ = key
#
#   credential = base64.b64encode(f'{app_id_}:{secret_key_}'.encode('utf-8')).decode('utf-8')
#
#
# def verify(credential):
#
#   url = 'https://api.sandbox.upland.me/developers-api/auth/otp/init'
#
#   headers = {
#       'Authorization': f'Basic {credential}',
#   }
#
#   response = requests.post(url, headers=headers)
#
#   if response.status_code == 201 or response.status_code == 200:
#       data = response.json()
#       code = data['code']
#       print(f"{code}")
#
#   else:
#       # If the request was not successful, print the status code
#       print(f'request failed status code {response.status_code}')
#       # print(response.json())
