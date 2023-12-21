from openpyxl import load_workbook
from Upland.FIXED_VARIABLES import filepath


def AppendProfile(data):
    workbook = load_workbook(filepath)
    worksheet = workbook['Sheet']

    worksheet.append(data)

    workbook.save(filepath)
    workbook.close()
