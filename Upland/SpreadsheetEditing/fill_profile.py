from FIXED_VARIABLES import profiles_db

from Chess.get_lichess_info import GetLichessRating

from Upland.SpreadsheetEditing.query_spreadsheet import QueryForLichessID, QueryForPassword
from Upland.SpreadsheetEditing.edit_profile import FillingLichessInfo


def FillProfile(uplandID, lichessID, password):   # Called when you submit a created profile
    # Clearing up errors    
    lichessRating = GetLichessRating(lichessID, "rapid")
    if (lichessRating == -1): return 'invalid lichess'

    if not profiles_db.find_one({"Upland Username": uplandID}): return 'no profile found'

    prof_pass = QueryForPassword(uplandID)

    # Depending on parameters, the profile will either be edited or errors will be returned
    if (prof_pass):
        if (prof_pass == password):
            if (lichessID != QueryForLichessID(uplandID)):
                FillingLichessInfo(uplandID, lichessID, lichessRating, -1)
                return 'replaced'
            else:
                return 'same'
        else:
            return 'wrong password'         
    else:
        FillingLichessInfo(uplandID, lichessID, lichessRating, password)

    return "success"