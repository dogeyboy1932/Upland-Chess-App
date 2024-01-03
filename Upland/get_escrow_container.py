from Upland.FIXED_VARIABLES import conn
import json


def GetEscrowContainer(eid):
    payload = json.dumps({
        "expirationPeriodHours": 24
    })

    headers = {
        'Authorization': 'Basic MjMyOmFkMzMxMDkxLTQ3NjItNGZlMS1iNDBmLTFkNGNhMGQwMmQ5Zg==',
        'Cookie': 'sticky-session-1=1701556690.435.2069.742375|9a5cc3e4d08faea009d8e16f5c97bee9'
    }

    url = "/developers-api/containers/" + str(eid)

    conn.request("GET", url, payload, headers)
    res = conn.getresponse()
    data = json.loads(res.read().decode("utf-8"))

    # print(data)

    return data


def run():
    print(GetEscrowContainer(2317))


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
