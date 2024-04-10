from Upland.FIXED_VARIABLES import filepath
from openpyxl import load_workbook
from Upland.query_spreadsheet import QueryUplandIDRow
from Chess.get_chess_rating import GetLichessRating
from Upland.edit_profile import ReplaceProfileBig
from Upland.edit_profile import ReplaceProfileSmall

def FillProfile(uplandID, lichessID, password):
    workbook = load_workbook(filepath)
    worksheet = workbook['Sheet']

    id_index = QueryUplandIDRow(uplandID)

    if (id_index == -1):
        return 'no profile found'

    lichessRating = GetLichessRating(lichessID, "rapid")  # For now, we'll stick with Rapid

    prof_pass = worksheet[id_index][6].value
    
    if (prof_pass != "null" and lichessID != worksheet[id_index][0].value):
        if (prof_pass == password):
            ReplaceProfileSmall(id_index, lichessID)
            return 'replaced'
        else:
            return 'wrong password'
         
    elif (prof_pass != "null"):
        return 'profile exists'
    else:
        ReplaceProfileBig(id_index, lichessID, lichessRating, password)


    return "success"


# def run():
#     uid = "dogeyboy1000"
#     # lid = "trashboatsr1000"
#     FillProfile(uid)
#
#
# run()