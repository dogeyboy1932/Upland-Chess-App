from FIXED_VARIABLES import conn
from FIXED_VARIABLES import credential
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
    data = json.loads(res.read().decode("utf-8"))
    print(data)


def run():
    escrowId = 2317
    RefundEscrowContainer(escrowId)

# run()