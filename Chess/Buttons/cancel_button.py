import json
from openpyxl import load_workbook

from FIXED_VARIABLES import cfilepath, conn

from Upland.Escrow.get_escrow_container import GetEscrowContainer
from Upland.SpreadsheetEditing.query_spreadsheet import QueryForIdxByLink



def ChallengeCanceled(link):  # <- Cancel Button clicked
    workbook = load_workbook(cfilepath)
    worksheet = workbook['Sheet']

    challengeIdx = QueryForIdxByLink(link)
    
    escrowID = str(worksheet[challengeIdx][5].value)
    escrow = GetEscrowContainer(escrowID)
    
    if (escrow != -1):
        max_transaction_id = 0
        greatestId = 0

        # Get request parameters
        for asset in escrow['assets']:
            asset_id = int(asset['id'])
            if asset_id > greatestId and asset['status'] == 'user_signature_requested':
                greatestId = asset_id
                max_transaction_id = asset['transactionId']


        url = f"/developers-api/containers/{escrowID}/transactions/{max_transaction_id}"

        payload = json.dumps({
            "expirationPeriodHours": 24
        })

        headers = {
            'Authorization': 'Basic MjMyOmFkMzMxMDkxLTQ3NjItNGZlMS1iNDBmLTFkNGNhMGQwMmQ5Zg==',
            'Cookie': 'sticky-session-1=1701556690.435.2069.742375|9a5cc3e4d08faea009d8e16f5c97bee9'
        }

        try:
            conn.request("DELETE", url, payload, headers)
            
            worksheet[challengeIdx][6].value = "NO"
            worksheet[challengeIdx][7].value = "blank"
        except:
            pass


    workbook.save(cfilepath)
    workbook.close()