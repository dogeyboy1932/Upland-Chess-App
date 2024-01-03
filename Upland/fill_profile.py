from Upland.FIXED_VARIABLES import filepath
from openpyxl import load_workbook
from Upland.query_spreadsheet import QueryUplandIDRow
from Chess.get_chess_rating import GetLichessRating


def FillProfile(uplandID, lichessID, password):
    workbook = load_workbook(filepath)
    worksheet = workbook['Sheet']

    id_index = QueryUplandIDRow(uplandID)

    lichessRating = GetLichessRating(lichessID, "rapid")  # For now, we'll stick with Rapid

    if (id_index == -1):
        return 'no profile found'
    elif (worksheet[id_index][6].value != "null"):
        return 'profile exists'     
    else:
        worksheet[id_index][6].value = password 
        worksheet[id_index][0].value = lichessID 
        worksheet[id_index][2].value = lichessRating   


    workbook.save(filepath)
    workbook.close()

    return "success"


# def run():
#     uid = "dogeyboy1000"
#     # lid = "trashboatsr1000"
#     FillProfile(uid)
#
#
# run()