import json

from FIXED_VARIABLES import conn, credential


def GetEscrowContainer(eid):
    url = "/developers-api/containers/" + str(eid)
    
    payload = json.dumps({
        "expirationPeriodHours": 24
    })

    headers = {
        'Authorization': f'Basic {credential}',
        'Cookie': 'sticky-session-1=1701556690.435.2069.742375|9a5cc3e4d08faea009d8e16f5c97bee9'
    }


    try:
        conn.request("GET", url, payload, headers)
        
        res = conn.getresponse()
        data = json.loads(res.read().decode("utf-8"))
        
        return data
    except:
        print("GET ESCROW FAILED")
        return -1


def run():
    print(GetEscrowContainer(4038))


# run()