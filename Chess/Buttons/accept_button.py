from openpyxl import load_workbook

from FIXED_VARIABLES import cfilepath

from Upland.Escrow.join_escrow_container import JoinEscrow
from Upland.get_user_profile import GetUserProfile
from Upland.SpreadsheetEditing.query_spreadsheet import GetBearerToken, QueryForIdxByLink


def ChallengeAccepted(link, accepter):  # <- Accept Button clicked
    workbook = load_workbook(cfilepath)
    worksheet = workbook['Sheet']

    # Eliminate Errors
    try:
        GetUserProfile(GetBearerToken(accepter))['level']
    except:
        return -2

    if GetUserProfile(GetBearerToken(accepter))['level'] == "Visitor":
        return -1
    
    # Mark challenge accepted
    challengeIdx = QueryForIdxByLink(link)
    worksheet[challengeIdx][6].value = "YES"
    worksheet[challengeIdx][7].value = accepter
    
    workbook.save(cfilepath)
    workbook.close()
    

    # Join Escrow
    bearer = GetBearerToken(accepter)
    eid = worksheet[challengeIdx][5].value
    wager = worksheet[challengeIdx][3].value
    
    JoinEscrow(bearer, eid, wager)


    return "success"