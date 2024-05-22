import json

from FIXED_VARIABLES import challenges_db, conn

from Upland.Escrow.get_escrow_container import GetEscrowContainer

def ChallengeCanceled(link):
    challenge = challenges_db.find_one({"link": link})
    
    escrowID = str(challenge.get("escrowID", ""))
    escrow = GetEscrowContainer(escrowID)

    if escrow != -1:
        max_transaction_id = 0
        greatestId = 0

        for asset in escrow['assets']:
            asset_id = int(asset['id'])
            if asset_id > greatestId and asset['status'] == 'user_signature_requested':
                greatestId = asset_id
                max_transaction_id = asset['transactionId']

        url = f"/developers-api/containers/{escrowID}/transactions/{max_transaction_id}"
        
        payload = json.dumps({"expirationPeriodHours": 24})
        
        headers = {
            'Authorization': 'Basic MjMyOmFkMzMxMDkxLTQ3NjItNGZlMS1iNDBmLTFkNGNhMGQwMmQ5Zg==',
            'Cookie': 'sticky-session-1=1701556690.435.2069.742375|9a5cc3e4d08faea009d8e16f5c97bee9'
        }

        try:
            conn.request("DELETE", url, payload, headers)

            challenges_db.update_one(
                {"link": link},
                {"$set": {"accepted?": "NO", "accepter": "blank"}}
            )
            # print("HERE")
        except:
            # print("ERROR")
            pass