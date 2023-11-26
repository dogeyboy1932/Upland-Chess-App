from FIXED_VARIABLES import primeEOS
import requests
import json

from get_escrow_container import GetEscrowContainer


def WinResolveEscrow(escrowId, winnerId, loserId):
    url = "https://api.sandbox.upland.me/developers-api/containers/" + escrowId + "/resolve"

    totalUpx = GetEscrowContainer(escrowId)['upx']
    # print(totalUpx)

    payload = json.dumps({
        "actions": [
            {
                "category": "upx",
                "targetEosId": winnerId,
                "amount": (totalUpx * .7)
            },
            {
                "category": "upx",
                "targetEosId": loserId,
                "amount": (totalUpx * .2)
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
        'Authorization': 'Basic MjMyOmVjMjFlZmZlLTYyZDktNDAzZi04MTc3LTEwODdjMWJlNmJjYw==',
        'Cookie': 'sticky-session-1=1699553168.246.2069.619172|aebf5e9dc298523c710b3cfe411c6704'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


def DrawResolveEscrow(escrowId, winnerId, loserId):
    url = "https://api.sandbox.upland.me/developers-api/containers/" + escrowId + "/resolve"

    totalUpx = GetEscrowContainer(escrowId)['upx']
    # print(totalUpx)

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
      'Authorization': 'Basic MjMyOmVjMjFlZmZlLTYyZDktNDAzZi04MTc3LTEwODdjMWJlNmJjYw==',
      'Cookie': 'sticky-session-1=1699553168.246.2069.619172|aebf5e9dc298523c710b3cfe411c6704'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


def LockEscrow(eid):
    url = "https://api.sandbox.upland.me/developers-api/containers/" + str(eid) + "/lock"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic MjMyOmVjMjFlZmZlLTYyZDktNDAzZi04MTc3LTEwODdjMWJlNmJjYw==',
        'Cookie': 'sticky-session-1=1699553168.246.2069.619172|aebf5e9dc298523c710b3cfe411c6704'
    }

    requests.request("POST", url, headers=headers)


def ResolveEscrow(eid, winner, loser, drawStatus):
    eid = str(eid)
    if drawStatus == "DRAW":
        DrawResolveEscrow(eid, winner, loser)
    else:
        WinResolveEscrow(eid, winner, loser)


def run():
    eid = 1902
    # print(eid)

    winner = "mp4n4f2mq3ca"
    loser = "mp4n4f2mq3ca"
    drawStatus = "No Draw"

    # if (GetEscrowContainer(eid)['upx'] != 0)  <- Basically, if escrow account is ready to go...
    # ResolveEscrow(eid, winner, loser, drawStatus)

    print(GetEscrowContainer(eid))

    # LockEscrow(eid=eid)


run()



# print(GetEscrowContainer(eid)['upx'])
