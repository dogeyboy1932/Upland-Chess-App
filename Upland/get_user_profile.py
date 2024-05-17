import json
from FIXED_VARIABLES import conn


def GetUserProfile(upland_access_token):
    url = "/developers-api/user/profile"

    payload = ""

    headers = {
        'Authorization': f'Bearer {upland_access_token}',
    }

    try:
        conn.request("GET", url, payload, headers)

        response = conn.getresponse()
        data = json.loads(response.read().decode("utf-8"))

        return data
    except:
        print(f'GetUserProfile request failed with status code {response.status}')
        return -1