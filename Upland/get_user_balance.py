import json
from FIXED_VARIABLES import conn


def GetUserBalance(upland_access_token):
    url = "/developers-api/user/balances"

    payload = ""
    
    headers = {
        'Authorization': f'Bearer {upland_access_token}',
    }

    try:
        conn.request("GET", url, payload, headers)
        
        res = conn.getresponse()    
        data = json.loads(res.read().decode("utf-8"))
        
        return data['availableUpx']
    except:
        print("getBalanced call failed")
        return -1