from FIXED_CHESS_VARIABLES import cfilepath
import pandas as pd

df = pd.read_excel(cfilepath)
print(df)