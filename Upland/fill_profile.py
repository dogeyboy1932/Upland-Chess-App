from Upland.FIXED_VARIABLES import filepath
from openpyxl import load_workbook
from Upland.query_spreadsheet import QueryUplandIDRow
from __collect_lichess_info import GetLichessID
from Chess.get_chess_rating import GetLichessRating


def FillProfile(uplandID):
    workbook = load_workbook(filepath)
    worksheet = workbook['Sheet']

    id_index = QueryUplandIDRow(uplandID)

    lichessID = GetLichessID()  # <- FIX THIS
    lichessRating = GetLichessRating(lichessID, "rapid")  # For now, we'll stick with Rapid

    if id_index != -1:
        worksheet[id_index][0].value = lichessID
        worksheet[id_index][2].value = lichessRating

    workbook.save(filepath)
    workbook.close()


# def run():
#     uid = "dogeyboy1000"
#     # lid = "trashboatsr1000"
#     FillProfile(uid)
#
#
# run()