from openpyxl import load_workbook
from FIXED_VARIABLES import filepath


def AppendProfile(data):
    workbook = load_workbook(filepath)
    worksheet = workbook['Sheet']

    worksheet.append(data)

    workbook.save(filepath)
    workbook.close()






# df = pd.read_excel(filepath)
# print(df)

# def GetWorkbook():
#     return workbook

# print("CALLED APPEND 1")
# print("Rows ", worksheet.max_row)

# workbook.clear()

# workbook.save('/Users/gogin/Desktop/Metaverse/ChessApp Pycharm Code/ChessDatabase1.xlsx')

# worksheet = workbook.active

# worksheet.append(data)

# worksheet.append("Akhil")






# workbook = load_workbook(filepath)
