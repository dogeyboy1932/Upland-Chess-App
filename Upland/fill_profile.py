from FIXED_VARIABLES import filepath
from openpyxl import load_workbook
from Chess.__collect_lichess_info import GetLichessID
from Chess.get_chess_rating import GetLichessRating
from query_uplandID_index import QueryUplandIDRow


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


# df = pd.read_excel(filepath)
# print(df)

# print(worksheet[i][2])
# row = list(worksheet.rows)[i]
# print(row[3].value)

# workbook.save(filepath)
#
# workbook.close()


# print("QUERY CALLED")
#
# returnIndex = -1
#

# print("MADE IT INSIDE")
# compareValue = worksheet[i][3].value
# print(compareValue)
# df = pd.read_excel(filepath)
# print(df)
# print("RETURN INDEX", returnIndex)
# print("QUERY DONE")

# print("FillProfile Called")
# print("MAX row", worksheet.max_row)
# print(lichessID)
# print(lichessRating)
# print("AFTER FILLED")
# print("Made inside")
# print(worksheet[index][0].value)
# print(worksheet[index][1].value)
# print("SPACE")
# print(worksheet[index][0].value)
# print(worksheet[index][1].value)
