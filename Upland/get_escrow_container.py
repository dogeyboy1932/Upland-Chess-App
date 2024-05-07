import json
from FIXED_VARIABLES import conn
from FIXED_VARIABLES import credential


def GetEscrowContainer(eid):
    payload = json.dumps({
        "expirationPeriodHours": 24
    })

    headers = {
        'Authorization': f'Basic {credential}',
        'Cookie': 'sticky-session-1=1701556690.435.2069.742375|9a5cc3e4d08faea009d8e16f5c97bee9'
    }

    url = "/developers-api/containers/" + str(eid)

    try:
        conn.request("GET", url, payload, headers)
    except:
        return -1
    
    res = conn.getresponse()
    data = json.loads(res.read().decode("utf-8"))

    return data


def run():
    print(GetEscrowContainer(4038))


# run()



# OLD CODE:
#     url = ("https://api.sandbox.upland.me/developers-api/containers/" + str(eid))
#     # print(url)
#
#     headers = {
#       'Content-Type': 'application/json',
#       'Authorization': 'Basic MjMyOmVjMjFlZmZlLTYyZDktNDAzZi04MTc3LTEwODdjMWJlNmJjYw==',
#     }
#
#     response = requests.request("GET", url, headers=headers)
#     data = response.json()
#
#     # print(data)
#
#     return data
