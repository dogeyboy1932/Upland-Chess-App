import json

from FIXED_VARIABLES import primeEOS, conn, credential

from Upland.Escrow.get_escrow_container import GetEscrowContainer


def WinResolveEscrow(escrowId, winnerId, loserId, totalUpx):
    url = "/developers-api/containers/" + escrowId + "/resolve"

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


    try:
        conn.request("POST", url, payload, headers)
        
        res = conn.getresponse()
        data = json.loads(res.read().decode("utf-8"))
    
        print("Resolved Escrow! Transaction Hash:", data["transactionId"])
        return "success"
    except:
        print(f'Request failed with status code {res.status}')
        return "error"
    


def DrawResolveEscrow(escrowId, winnerId, loserId, totalUpx):
    url = "/developers-api/containers/" + escrowId + "/resolve"

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


    try:
        conn.request("POST", url, payload, headers)
        
        res = conn.getresponse()
        data = json.loads(res.read().decode("utf-8"))
        
        print("Resolved Escrow! Transaction Hash:", data["transactionId"])
        return "success"
    except:
        print(f'Request failed with status code {res.status}')
        return "error"       


def ResolveEscrow(eid, winner, loser, drawStatus, wager):
    
    try:
        totalUpx = GetEscrowContainer(eid)['upx']
    except:
        print("ERROR GETTING ESCROW")
        return -1

    if totalUpx != wager * 2: return -1  # Escrow needs sufficient funds to be resolved
        
        
    if drawStatus == "DRAW":
        return DrawResolveEscrow(str(eid), str(winner), str(loser), totalUpx)
    else:
        return WinResolveEscrow(str(eid), str(winner), str(loser), totalUpx)
