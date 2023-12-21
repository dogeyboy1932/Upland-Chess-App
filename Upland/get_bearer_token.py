from Upland.FIXED_VARIABLES import filepath
from openpyxl import load_workbook
import pandas as pd

pd.set_option('display.max_colwidth', None)

def GetBearerToken(uplandID):
    workbook = load_workbook(filepath)
    worksheet = workbook['Sheet']

    # df = pd.read_excel(filepath, usecols="E")
    # print(df)
    # print("HERE")



    for i in range(1, worksheet.max_row + 1):
        # print(worksheet[i][4].value)
        # print("BLANK")
        if worksheet[i][1].value == uplandID:
            return worksheet[i][4].value

    return -1


def run():
    print(GetBearerToken("dogeyboy19"))

# run()
