from FIXED_VARIABLES import profiles_db

from Chess.get_lichess_info import GetLichessRating

from Upland.SpreadsheetEditing.edit_profile import FillingLichessInfo
from Upland.SpreadsheetEditing.query_spreadsheet import QueryForUplandID

def FillProfile(uplandID, lichessID, password):   # Called when you submit a created profile
    # Clearing up errors    
    lichessRating = GetLichessRating(lichessID, "rapid")
    if (lichessRating == -1): return 'invalid lichess'

    profile = profiles_db.find_one({"Upland Username": uplandID})

    if profile: prof_pass = profile.get("Password", -1)
    else: prof_pass = -1

    # Depending on parameters, the profile will either be edited or errors will be returned
    if (prof_pass):
        if (prof_pass == password):
            if (lichessID != profile.get("Lichess ID", -1)):
                if QueryForUplandID(lichessID) == -1:
                    FillingLichessInfo(uplandID, lichessID, lichessRating, -1)
                    return 'replaced'
                else:
                    return 'taken'
            else:
                return 'same'
        else:
            return 'wrong password'         
    else:
        FillingLichessInfo(uplandID, lichessID, lichessRating, password)

    return "success"