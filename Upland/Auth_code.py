import requests
import base64


def verify(app_id, key):
    app_id_ = app_id
    secret_key_ = key

    credential = base64.b64encode(f'{app_id_}:{secret_key_}'.encode('utf-8')).decode('utf-8')

    url = 'https://api.sandbox.upland.me/developers-api/auth/otp/init'

    headers = {
        'Authorization': f'Basic {credential}',
    }

    response = requests.post(url, headers=headers)

    if response.status_code == 201 or response.status_code == 200:
        data = response.json()
        code = data['code']
        print(f"{code}")

    else:
        # If the request was not successful, print the status code
        print(f'request failed status code {response.status_code}')
        print(response.json())


def run():
    app_id = "232"
    key = "ec21effe-62d9-403f-8177-1087c1be6bcc"

    verify(app_id, key)


run()