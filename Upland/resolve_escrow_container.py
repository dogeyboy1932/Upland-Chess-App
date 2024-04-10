import json
import base64
from Upland.FIXED_VARIABLES import primeEOS
from Upland.FIXED_VARIABLES import conn
from Upland.get_escrow_container import GetEscrowContainer


def WinResolveEscrow(escrowId, winnerId, loserId, credential, wager):
    url = "/developers-api/containers/" + escrowId + "/resolve"

    totalUpx = GetEscrowContainer(escrowId)['upx']

    if totalUpx != wager * 2:
        return -1

    payload = json.dumps({
        "actions": [
            {
                "category": "upx",
                "targetEosId": winnerId,
                "amount": (totalUpx * .8)
            },
            {
                "category": "upx",
                "targetEosId": loserId,
                "amount": (totalUpx * .1)
            },
            {
                "category": "upx",
                "targetEosId": primeEOS,
                "amount": (totalUpx * .1)
            }
        ]
    })

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Basic {credential}',
        'Cookie': 'sticky-session-1=1701556690.435.2069.742375|9a5cc3e4d08faea009d8e16f5c97bee9'
    }

    conn.request("POST", url, payload, headers)
    res = conn.getresponse()

    if res.status == 200 or res.status == 201:
        data = json.loads(res.read().decode("utf-8"))
        print("Refunded Escrow! Transaction Hash:", data["transactionId"])
        return "success"
    else:
        print(f'Request failed with status code {res.status}')
        # print(res.getheaders())
        return "error"
    
    


def DrawResolveEscrow(escrowId, winnerId, loserId, credential, wager):
    url = "/developers-api/containers/" + escrowId + "/resolve"

    totalUpx = GetEscrowContainer(escrowId)['upx']

    if totalUpx != wager * 2:
        return -1

    payload = json.dumps({
        "actions": [
            {
                "category": "upx",
                "targetEosId": winnerId,
                "amount": (totalUpx * .45)
            },
            {
                "category": "upx",
                "targetEosId": loserId,
                "amount": (totalUpx * .45)
            },
            {
                "category": "upx",
                "targetEosId": primeEOS,
                "amount": (totalUpx * .1)
            }
        ]
    })

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Basic {credential}',
        'Cookie': 'sticky-session-1=1701556690.435.2069.742375|9a5cc3e4d08faea009d8e16f5c97bee9'
    }
    
    conn.request("POST", url, payload, headers)
    res = conn.getresponse()

    if res.status == 200 or res.status == 201:
        data = json.loads(res.read().decode("utf-8"))
        print("Refunded Escrow! Transaction Hash:", data["transactionId"])
        return "success"
    else:
        print(f'Request failed with status code {res.status}')
        # print(res.getheaders())
        return "error"


def ResolveEscrow(eid, winner, loser, drawStatus, credential, wager):

    eid = str(eid)
    if drawStatus == "DRAW":
        return DrawResolveEscrow(eid, str(winner), str(loser), credential, wager)
    else:
        return WinResolveEscrow(eid, str(winner), str(loser), credential, wager)


def run():
    eid = 2148
    # print(eid)

    winner = "mp4n4f2mq3ca"
    loser = "mp4n4f2mq3ca"
    drawStatus = "No Draw"

    appID = "232"
    accessKey = "ad331091-4762-4fe1-b40f-1d4ca0d02d9f"

    credential = base64.b64encode(f'{appID}:{accessKey}'.encode('utf-8')).decode('utf-8')

    # if (GetEscrowContainer(eid)['upx'] == wager * 2)  <- Basically, if escrow account is ready to go...
    # ResolveEscrow(eid, winner, loser, drawStatus, credential)

    print(GetEscrowContainer(eid))

    # LockEscrow(eid=eid)


# run()





# OLD CODE:
#       url = "https://api.sandbox.upland.me/developers-api/containers/" + escrowId + "/resolve"
#
#     totalUpx = GetEscrowContainer(escrowId)['upx']
#     # print(totalUpx)
#
#     payload = json.dumps({
#         "actions": [
#             {
#                 "category": "upx",
#                 "targetEosId": winnerId,
#                 "amount": (totalUpx * .45)
#             },
#             {
#                 "category": "upx",
#                 "targetEosId": loserId,
#                 "amount": (totalUpx * .45)
#             },
#             {
#                 "category": "upx",
#                 "targetEosId": primeEOS,
#                 "amount": (totalUpx * .1)
#             }
#         ]
#     })
#
#     headers = {
#       'Content-Type': 'application/json',
#       'Authorization': 'Basic MjMyOmVjMjFlZmZlLTYyZDktNDAzZi04MTc3LTEwODdjMWJlNmJjYw==',
#       'Cookie': 'sticky-session-1=1699553168.246.2069.619172|aebf5e9dc298523c710b3cfe411c6704'
#     }
#
#     response = requests.request("POST", url, headers=headers, data=payload)
#
#     print(response.text)



# url = "https://api.sandbox.upland.me/developers-api/containers/" + escrowId + "/resolve"
#
#     totalUpx = GetEscrowContainer(escrowId)['upx']
#     # print(totalUpx)
#
# payload = json.dumps({
#     "actions": [
#         {
#             "category": "upx",
#             "targetEosId": winnerId,
#             "amount": (totalUpx * .8)
#         },
#         {
#             "category": "upx",
#             "targetEosId": loserId,
#             "amount": (totalUpx * .1)
#         },
#         {
#             "category": "upx",
#             "targetEosId": primeEOS,
#             "amount": (totalUpx * .1)
#         }
#     ]
# })
#
#     headers = {
#       'Content-Type': 'application/json',
#       'Authorization': 'Basic MjMyOmVjMjFlZmZlLTYyZDktNDAzZi04MTc3LTEwODdjMWJlNmJjYw==',
#       'Cookie': 'sticky-session-1=1699553168.246.2069.619172|aebf5e9dc298523c710b3cfe411c6704',
#     }
#
#     response = requests.request("POST", url, headers=headers, data=payload)
#
#     print(response.text)