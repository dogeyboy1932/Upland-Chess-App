from FIXED_CHESS_VARIABLES import filepath
import pandas as pd

# FRONTEND DEPENDENT <- Translates spreadsheet into frontend database


def Iterate():
    print("HERE")

    ######################
    # INSTRUCTION
    # All we're doing here is rendering the excel spreadsheet on the frontend
    # in form of a database
    ######################

    df = pd.read_excel(filepath)
    print(df)


def run():
    Iterate()


run()
