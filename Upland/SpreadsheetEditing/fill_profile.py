from openpyxl import load_workbook

from FIXED_VARIABLES import filepath

from Chess.get_lichess_info import GetLichessRating

from Upland.SpreadsheetEditing.query_spreadsheet import QueryUplandIDRow
from Upland.SpreadsheetEditing.edit_profile import FillingLichessInfo


def FillProfile(uplandID, lichessID, password):   # Called when you submit a created profile
    print("REACHED HERE")
    
    worksheet = load_workbook(filepath)['Sheet']

    # Clearing up errors    
    lichessRating = GetLichessRating(lichessID, "rapid")
    if (lichessRating == -1): return 'invalid lichess'
    
    id_index = QueryUplandIDRow(uplandID)
    if (id_index == -1): return 'no profile found'


    # Getting existing password as a security measure
    prof_pass = worksheet[id_index][6].value


    # Depending on parameters, the profile will either be edited or errors will be returned
    if (prof_pass):
        if (prof_pass == password):
            if (lichessID != worksheet[id_index][0].value):
                FillingLichessInfo(id_index, lichessID, lichessRating, -1)
                return 'replaced'
            else:
                return 'same'
        else:
            return 'wrong password'         
    else:
        FillingLichessInfo(id_index, lichessID, lichessRating, password)

    return "success"