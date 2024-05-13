import json;

from FIXED_VARIABLES import conn, credential

from Upland.Escrow.get_escrow_container import GetEscrowContainer

def RefundEscrowContainer(escrowId):

    # Clearing up potential errors
    escrow = GetEscrowContainer(escrowId)

    if escrow == -1: return "Processing"

    for i in escrow['assets']:
        if i['status'] == 'changing_ownership':
            return "Processing"

    if escrow['upx'] == 0:
        return "Nothing to refund"


    # Refunding Escrow
    url = "/developers-api/containers/" + str(escrowId) + "/refund"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Basic {credential}',
        'Cookie': 'sticky-session-1=1701556690.435.2069.742375|9a5cc3e4d08faea009d8e16f5c97bee9'
    }

    try:
        conn.request("POST", url=url, headers=headers)
        
        res = conn.getresponse()
        data = json.loads(res.read().decode("utf-8"))
        
        print("Refunded Escrow! Transaction Hash:", data["transactionId"])
        return "success"
    except:
        print(f'Request failed with status code {res.status}')
        return "error"

