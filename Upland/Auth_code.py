import json
from FIXED_VARIABLES import conn, credential


def Verify():
    url = "/developers-api/auth/otp/init"

    payload = ''
    
    headers = {
        'Authorization': f'Basic {credential}',
        # 'Cookie': 'sticky-session-1=1701556690.435.2069.742375|9a5cc3e4d08faea009d8e16f5c97bee9'
    }

    # print("VERIFY")

    try:
        conn.request("POST", url, payload, headers)
        
        res = conn.getresponse()
        data = json.loads(res.read().decode("utf-8"))
    
        return str(data['code'])
    except:
        print(f'Auth request failed with status code')
        return -1