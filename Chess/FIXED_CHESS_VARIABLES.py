import berserk
import base64

token = "lip_ZnYbIrvWC5KDwB8P0wJu"

session = berserk.TokenSession(token)
client = berserk.Client(session=session)

appID = "232"
accessKey = "ad331091-4762-4fe1-b40f-1d4ca0d02d9f"
credential = base64.b64encode(f'{appID}:{accessKey}'.encode('utf-8')).decode('utf-8')


cfilepath = "/Users/gogin/Desktop/ChessApp/ChessApp VS Code/XL Spreadsheets/ChallengeMap.xlsx"
