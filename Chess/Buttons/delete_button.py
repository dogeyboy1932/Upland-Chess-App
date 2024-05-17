from openpyxl import load_workbook

from FIXED_VARIABLES import cfilepath

from Upland.Escrow.refund_escrow import RefundEscrowContainer
from Upland.SpreadsheetEditing.query_spreadsheet import QueryForIdxByLink

def ChallengeDeleted(link):  # <- Delete Button clicked
    workbook = load_workbook(cfilepath)
    worksheet = workbook['Sheet']
    
    challengeIdx = QueryForIdxByLink(link)
    
    eid = worksheet[challengeIdx][5].value
    returnVal = RefundEscrowContainer(eid)
    
    if returnVal != "Processing":
        worksheet.delete_rows(challengeIdx)

    workbook.save(cfilepath)
    workbook.close()

    return returnVal