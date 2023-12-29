import json
import http.client
from Upland.create_escrow_container import CreateEscrowContainer


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

    headers = {
        # 'Authorization': str(bearer),
        'Authorization': bearer,
        'Content-Type': 'application/json',
        'Cookie': 'sticky-session-1=1699553168.246.2069.619172|aebf5e9dc298523c710b3cfe411c6704'
    }

    conn.request("POST", "/developers-api/User/join", payload, headers)
    res = conn.getresponse()

    # print(res.getheaders())

    if res.status == 200 or res.status == 201:
        data = json.loads(res.read().decode("utf-8"))
        print("Joined Escrow! Transaction Hash:", data["transactionId"])
        return "success"
    else:
        print(f'Request failed with status code {res.status}')
        return "error"


def run():
    # eid = 2283
    eid = CreateEscrowContainer()
    print(eid)


    bearer = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiI0ODI5OGVhMC0yNDBhLTExZWUtOWMwNC1iMzcyMDk2MTViOGIiLCJhcHBJZCI6MjMyLCJ0b2tlbklkIjoiOTA4MDBmNTQtODJiOS00MjhkLWFhNjAtZjFjMmEyYjViYWRkIiwiaWF0IjoxNzAzMzAwMzA3fQ.dwlDpoQzpSexJ7UYey7iSpzqmmxAooOiOs1pNsci36o'


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
