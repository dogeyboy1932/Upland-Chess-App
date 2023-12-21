import json
import http.client


def JoinEscrow(bearerToken, containerId, upxAmount):
    conn = http.client.HTTPSConnection("api.sandbox.upland.me")

    payload = json.dumps({
        "containerId": containerId,
        "upxAmount": upxAmount,
        "sparkAmount": 0,
        "assets": [],
    })

    bearer = 'Bearer ' + str(bearerToken)
    # print(bearer)
    # print("FIN")

    headers = {
        # 'Authorization': str(bearer),
        'Authorization': bearer,
        'Content-Type': 'application/json',
        'Cookie': 'sticky-session-1=1699553168.246.2069.619172|aebf5e9dc298523c710b3cfe411c6704'
    }

    conn.request("POST", "/developers-api/User/join", payload, headers)
    res = conn.getresponse()

    if res.status == 200 or res.status == 201:
        data = json.loads(res.read().decode("utf-8"))
        print("Joined Escrow! Transaction Hash:", data["transactionId"])
    else:
        print(f'Request failed with status code {res.status}')


def run():
    # print("HERE")
    eid = 2245

    bearer = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiIwOTQ4ZGE1MC04N2Q0LTExZWUtYjBjMi02MzM4M2I3OTUzNjAiLCJhcHBJZCI6MjMyLCJ0b2tlbklkIjoiNDRmMmU1NjEtNmJkNS00NjIyLTkzMzEtMWYwODZkN2NmYTg0IiwiaWF0IjoxNzAzMTMxMDgwfQ.zR2L5ybvc2CkbSXWinJHk6w4KgbIqI4Wl5XCshe3zq8'


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
