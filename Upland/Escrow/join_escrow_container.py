import json

from FIXED_VARIABLES import conn


def JoinEscrow(bearerToken, containerId, upxAmount):
    url = "/developers-api/User/join"

    payload = json.dumps({
        "containerId": containerId,
        "upxAmount": upxAmount,
        "sparkAmount": 0,
        "assets": [],
    })

    bearer = 'Bearer ' + str(bearerToken)

    headers = {
        'Authorization': bearer,
        'Content-Type': 'application/json',
        'Cookie': 'sticky-session-1=1699553168.246.2069.619172|aebf5e9dc298523c710b3cfe411c6704'
    }

    try:
        conn.request("POST", url, payload, headers)
        res = conn.getresponse()
        data = json.loads(res.read().decode("utf-8"))
        
        print("Joined Escrow! Transaction Hash:", data["transactionId"])
        return "success"
    except:
        print(f'Request failed with status code {res.status}')
        return "error"


def run():
    eid = 2283
    # eid = CreateEscrowContainer()
    print(eid)

    bearer = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiIwOTQ4ZGE1MC04N2Q0LTExZWUtYjBjMi02MzM4M2I3OTUzNjAiLCJhcHBJZCI6MjMyLCJ0b2tlbklkIjoiNDE0YTdlYTAtMzE1My00YzZlLTk0MmItMjQ4N2FhZjdjNDQ1IiwiaWF0IjoxNzAzOTU0OTY5fQ.gYBD1eGIaV5ipOJPJUaAkH715hhkxMVPDwwn8GNddrY'

    JoinEscrow(bearer, eid, 100)

# run()






# Old Code (REQUESTS):
# url = "https://api.sandbox.upland.me/developers-api/User/join"
#
# payload = json.dumps({
#     "containerId": containerId,
#     "upxAmount": upxAmount,
#     "sparkAmount": 0,
#     "assets": [],
# })
#
# bearer = 'Bearer ' + bearerToken
# # print(bearer)
#
# headers = {
#     # 'Authorization': str(bearer),
#     'Authorization': bearer,
#     'Content-Type': 'application/json',
#     'Cookie': 'sticky-session-1=1699553168.246.2069.619172|aebf5e9dc298523c710b3cfe411c6704'
# }
#
# response = requests.request("POST", url, headers=headers, data=payload)
#
# print(response.text)
