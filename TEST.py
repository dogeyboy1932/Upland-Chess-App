import http.client
import json

# from openpyxl import load_workbook
# from Chess.FIXED_CHESS_VARIABLES import cfilepath

# def AppendInitial():
#     workbook = load_workbook(cfilepath)
#     worksheet = workbook['Sheet']

#     data = ["gameID", "challenger", "rating", "wager", "link", "escrowID", "accepter"]

#     worksheet.append(data)

#     workbook.save(cfilepath)
#     workbook.close()




def GetEscrowContainer(eid):
    conn = http.client.HTTPSConnection("api.sandbox.upland.me")
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


# def JoinEscrow(bearerToken, containerId, upxAmount):
#     conn = http.client.HTTPSConnection("api.sandbox.upland.me")
#     payload = json.dumps({
#         "containerId": containerId,
#         "upxAmount": upxAmount,
#         "sparkAmount": 0,
#         "assets": [],
#     })

#     bearer = 'Bearer ' + str(bearerToken)

#     headers = {
#         # 'Authorization': str(bearer),
#         'Authorization': bearer,
#         'Content-Type': 'application/json',
#         'Cookie': 'sticky-session-1=1699553168.246.2069.619172|aebf5e9dc298523c710b3cfe411c6704'
#     }

#     conn.request("POST", "/developers-api/User/join", payload, headers)
#     res = conn.getresponse()

#     if res.status == 200 or res.status == 201:
#         data = json.loads(res.read().decode("utf-8"))
#         print("Joined Escrow! Transaction Hash:", data["transactionId"])
#         return "success"
#     else:
#         print(f'Request failed with status code {res.status}')
#         return "error"


def run():
    eid = 3968
    # eid = CreateEscrowContainer()
    # print(eid)

    # bearer = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiI0ODI5OGVhMC0yNDBhLTExZWUtOWMwNC1iMzcyMDk2MTViOGIiLCJhcHBJZCI6MjMyLCJ0b2tlbklkIjoiYTUwZWIxZGEtMjI1ZS00MWY5LWFhM2ItN2M5NzQwZjUwZmY1IiwiaWF0IjoxNzA0OTk0MDk2fQ.xxnNviAMmuzmPz2R9cniCJ2BwZOTM6ya823dOjqhhAw'

    # JoinEscrow(bearer, eid, 50)
    print(GetEscrowContainer(eid))

run()

# import http.client
# import json

# conn = http.client.HTTPSConnection("api.sandbox.upland.me")
# payload = json.dumps({
#   "containerId": str(3191),
#   "upxAmount": 10,
#   "sparkAmount": 0,
#   "assets": []
# })
# headers = {
#   'Content-Type': 'application/json',
#   'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiI0ODI5OGVhMC0yNDBhLTExZWUtOWMwNC1iMzcyMDk2MTViOGIiLCJhcHBJZCI6MjMyLCJ0b2tlbklkIjoiYzdjZGYxZmEtNTIxMi00MTI1LTg5ZDctNThiNDk1OTVkZDQzIiwiaWF0IjoxNzA0OTE4ODI5fQ.UdH-iKZddS4pKnfYBuKK0AfYGBfP-cEXlaplsMPnn9o',
#   'Cookie': 'sticky-session-1=1704817779.488.2071.595873|9a5cc3e4d08faea009d8e16f5c97bee9'
# }
# conn.request("POST", "/developers-api/User/join", payload, headers)
# res = conn.getresponse()
# data = res.read()
# # print(res.headers)
# print(data.decode("utf-8"))
# print("HERE")

# from Upland.FIXED_VARIABLES import conn
# import json

# def JoinEscrow(bearerToken, containerId, upxAmount):
#     payload = json.dumps({
#         "containerId": containerId,
#         "upxAmount": upxAmount,
#         "sparkAmount": 0,
#         "assets": [],
#     })

#     bearer = 'Bearer ' + str(bearerToken)

#     headers = {
#         'Authorization': str(bearer),
#         # 'Authorization': bearer,
#         # 'Content-Type': 'application/json',
#         'Cookie': 'sticky-session-1=1699553168.246.2069.619172|aebf5e9dc298523c710b3cfe411c6704'
#     }

#     conn.request("POST", "/developers-api/User/join", payload, headers)
#     res = conn.getresponse()

#     if res.status == 200 or res.status == 201:
#         data = json.loads(res.read().decode("utf-8"))
#         print("Joined Escrow! Transaction Hash:", data["transactionId"])
#         return "success"
#     else:
#         print(f'Request failed with status code {res.status}')
#         print(res.msg)
#         return "error"


# def run():
#     eid = 3191
#     # eid = CreateEscrowContainer()
#     print(eid)

#     bearer = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiI0ODI5OGVhMC0yNDBhLTExZWUtOWMwNC1iMzcyMDk2MTViOGIiLCJhcHBJZCI6MjMyLCJ0b2tlbklkIjoiYTcyNzE2NDEtZTcxMS00YjBiLWE5NWYtMjEwNTA3Y2JlZGQyIiwiaWF0IjoxNzA0MzA1OTU5fQ.suGtQmS0pEEyxgJmqDXkd9ZKf0P4y5_PrTIs9y6_vJA'

#     JoinEscrow(bearer, eid, 100)

# run()

# # l3cn1ph243wu
