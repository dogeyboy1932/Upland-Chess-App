import json

from FIXED_VARIABLES import conn


def CreateEscrowContainer():
    url = "/developers-api/containers"
    
    payload = json.dumps({
        "expirationPeriodHours": 24
    })

    headers = {
        'Authorization': 'Basic MjMyOmFkMzMxMDkxLTQ3NjItNGZlMS1iNDBmLTFkNGNhMGQwMmQ5Zg==',
        'Cookie': 'sticky-session-1=1701556690.435.2069.742375|9a5cc3e4d08faea009d8e16f5c97bee9'
    }

    try:
        conn.request("POST", url, payload, headers)

        res = conn.getresponse()
        data = json.loads(res.read().decode("utf-8"))

        return data["id"]
    except:
        print(f'Request failed with status code {res.status}')
        return -1   



def run():
    val = CreateEscrowContainer()

    print(val)


# run()