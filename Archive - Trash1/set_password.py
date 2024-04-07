from Upland.FIXED_VARIABLES import filepath
from openpyxl import load_workbook
from Upland.query_spreadsheet import QueryUplandIDRow

def SetPassword(uplandID, password):
    workbook = load_workbook(filepath)
    worksheet = workbook['Sheet']

    id_index = QueryUplandIDRow(uplandID)

    if id_index != -1:
        worksheet[id_index][6].value = password

    workbook.save(filepath)
    workbook.close()