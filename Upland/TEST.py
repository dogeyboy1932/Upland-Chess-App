# from FIXED_VARIABLES import filepath
# import pandas as pd
# from openpyxl import load_workbook


# df = pd.read_excel(filepath)
# print(df)


# from FIXED_VARIABLES import conn
# import json


# def GetEscrowContainer(eid):
#     payload = json.dumps({
#         "expirationPeriodHours": 24
#     })

#     headers = {
#         'Authorization': 'Basic MjMyOmFkMzMxMDkxLTQ3NjItNGZlMS1iNDBmLTFkNGNhMGQwMmQ5Zg==',
#         'Cookie': 'sticky-session-1=1701556690.435.2069.742375|9a5cc3e4d08faea009d8e16f5c97bee9'
#     }

#     url = "/developers-api/containers/" + str(eid)

#     conn.request("GET", url, payload, headers)
#     res = conn.getresponse()
#     data = json.loads(res.read().decode("utf-8"))

#     # print(data)

#     return data

# print(GetEscrowContainer(2875))

# def QueryForEOSID(lichessID):
#     if lichessID == "{}":
#         return -1

#     workbook = load_workbook(filepath)
#     worksheet = workbook['Sheet']

#     print(lichessID)
#     for i in range(1, worksheet.max_row + 1):
#         print(worksheet[i][0].value)
#         if worksheet[i][0].value == lichessID:
#             return worksheet[i][5].value

#     return -1


# def run():
    # gameID = "rL3ou9hv"
    # winner = GameWinner(gameID=gameID)
    # corr_uplandID = QueryForEOSID(winner[0])

    # corr_uplandID = QueryForEOSID("trashboatsr")

    # print(corr_uplandID)


# run()

