from openpyxl import load_workbook

from FIXED_VARIABLES import filepath
from Chess.get_chess_info import GetLichessRating
from Upland.SpreadsheetEditing.query_spreadsheet import QueryUplandIDRow
from Upland.SpreadsheetEditing.edit_profile import ReplaceProfileBig, ReplaceProfileSmall


def FillProfile(uplandID, lichessID, password):
    workbook = load_workbook(filepath)
    worksheet = workbook['Sheet']

    id_index = QueryUplandIDRow(uplandID)

    if (id_index == -1):
        return 'no profile found'

    lichessRating = GetLichessRating(lichessID, "rapid")  # For now, we'll stick with Rapid

    # If LichessID is invalid, give error
    if (lichessRating == -1): return 'invalid lichess'

    # FIX THIS [CHANGE LICHESS ID]
    # if (worksheet[id_index][0].value != "BLANK_ID"): return 'invalid lichess'

    prof_pass = worksheet[id_index][6].value
    bearer = worksheet[id_index][4].value
    
    if (prof_pass != "null" and lichessID != worksheet[id_index][0].value):
        if (prof_pass == password):
            ReplaceProfileSmall(id_index, lichessID, bearer)
            return 'replaced'
        else:
            return 'wrong password'
         
    elif (prof_pass != "null"):
        return 'profile exists'
    else:
        ReplaceProfileBig(id_index, lichessID, lichessRating, password, bearer)


    return "success"


# def run():
#     uid = "dogeyboy1000"
#     # lid = "trashboatsr1000"
#     FillProfile(uid)
#
#
# run()