from FIXED_VARIABLES import challenges_db

from Upland.Escrow.join_escrow_container import JoinEscrow
from Upland.get_user_profile import GetUserProfile
from Upland.SpreadsheetEditing.query_spreadsheet import GetBearerToken, QueryForEOS, QueryForWager, QueryGameIDByLink


def ChallengeAccepted(link, accepter):  # <- Accept Button clicked

    # Eliminate Errors
    try:
        GetUserProfile(GetBearerToken(accepter))['level']
    except:
        return -2

    if GetUserProfile(GetBearerToken(accepter))['level'] == "Visitor":
        return -1
    
    # Mark challenge accepted
    challenges_db.update_one(
        {"link": link},
        {"$set": {
            "accepted?": "YES",
            "accepter": accepter,
            "readyStatus": "NO"  # assuming you want to set this field as well
        }}
    )


    gameID = QueryGameIDByLink(link)
    
    # Join Escrow
    bearer = GetBearerToken(accepter)
    eid = QueryForEOS(gameID)
    wager = QueryForWager(gameID)
    
    JoinEscrow(bearer, eid, wager)


    return "success"