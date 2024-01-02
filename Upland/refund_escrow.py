from Upland.FIXED_VARIABLES import conn
from Upland.FIXED_VARIABLES import credential
import json;

def RefundEscrowContainer(escrowId):
    url = "/developers-api/containers/" + str(escrowId) + "/refund"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Basic {credential}',
        'Cookie': 'sticky-session-1=1701556690.435.2069.742375|9a5cc3e4d08faea009d8e16f5c97bee9'
    }

    conn.request("POST", url=url, headers=headers)
    res = conn.getresponse()

    if res.status == 200 or res.status == 201:
        data = json.loads(res.read().decode("utf-8"))
        print("Refunded Escrow! Transaction Hash:", data["transactionId"])
        return "success"
    else:
        print(f'Request failed with status code {res.status}')
        print(res.getheaders())
        return "error"


def run():
    escrowId = 2317
    RefundEscrowContainer(escrowId)

# run()