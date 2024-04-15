from FIXED_VARIABLES import conn
import json


def CreateEscrowContainer():
    payload = json.dumps({
        "expirationPeriodHours": 24
    })

    headers = {
        'Authorization': 'Basic MjMyOmFkMzMxMDkxLTQ3NjItNGZlMS1iNDBmLTFkNGNhMGQwMmQ5Zg==',
        'Cookie': 'sticky-session-1=1701556690.435.2069.742375|9a5cc3e4d08faea009d8e16f5c97bee9'
    }

    conn.request("POST", "/developers-api/containers", payload, headers)
    res = conn.getresponse()
    data = json.loads(res.read().decode("utf-8"))

    # print(data)
    return data["id"]


def run():
    val = CreateEscrowContainer()

    print(val)


# run()



# Old Code:
    
# import requests
# import json

# def CreateEscrowContainer()
#     url = "https://api.sandbox.upland.me/developers-api/containers"
#
#     payload = json.dumps({
#       "expirationPeriodHours": 24,
#       "userLimitByContainer": 2
#     })
#
#     headers = {
#       'Content-Type': 'application/json',
#       'Authorization': 'Basic MjMyOmVjMjFlZmZlLTYyZDktNDAzZi04MTc3LTEwODdjMWJlNmJjYw==',
#       'Cookie': 'sticky-session-1=1699553168.246.2069.619172|aebf5e9dc298523c710b3cfe411c6704'
#     }
#
#     response = requests.request("POST", url, headers=headers, data=payload)
#     data = response.json()
#
#     print(data)
#
#     return data['id']
