from FIXED_VARIABLES import profiles_db, challenges_db

from Upland.get_user_balance import GetUserBalance
from Upland.SpreadsheetEditing.query_spreadsheet import QueryForUplandID


def Iterate():  # <- Translates spreadsheet into frontend database
    challenges = challenges_db.find()    
    table = []

    for challenge in challenges:
        challenger = challenge.get("challenger", "")
        rating = challenge.get("rating", "")
        wager = challenge.get("wager", "")
        link = challenge.get("link", "")
        uplandID = QueryForUplandID(challenger)
        accepted = challenge.get("accepted?", "")
        accepter = challenge.get("accepter", "")
        readyStatus = challenge.get("readyStatus", "")
        escrowID = challenge.get("escrowID", "")

        # Append the extracted data to the table
        table.append([challenger, rating, wager, link, uplandID, accepted, accepter, readyStatus, escrowID])

    return table



def UpdateBalance(upland_access_token):
    availableUpx = GetUserBalance(upland_access_token)

    print("AVAIL: ", availableUpx)
    if availableUpx == -1: return -1

    profiles_db.update_one(
        {"Bearer Token": upland_access_token},
        {"$set": {"Balance": availableUpx}}
    )


def UpdateBalances():
    for profile in profiles_db.find():
        UpdateBalance(profile.get('Bearer Token'))