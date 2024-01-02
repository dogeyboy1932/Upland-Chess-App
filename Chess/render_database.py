from Chess.FIXED_CHESS_VARIABLES import cfilepath
import pandas as pd
from Chess.query_for_uplandID import QueryForUplandID

# FRONTEND DEPENDENT <- Translates spreadsheet into frontend database


def Iterate():
    df = pd.read_excel(cfilepath, usecols='B:H,')
    res = []

    for index, row in df.iterrows():
        uplandID = QueryForUplandID(row.iloc[0])
        res.append([row.iloc[0], row.iloc[1], row.iloc[2], row.iloc[3], uplandID, row.iloc[5], row.iloc[6]])
    
    return res


def run():
    Iterate()


# run()
