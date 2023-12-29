import http.client
import base64
conn = http.client.HTTPSConnection("api.sandbox.upland.me")

appID = "232"
accessKey = "ad331091-4762-4fe1-b40f-1d4ca0d02d9f"
credential = base64.b64encode(f'{appID}:{accessKey}'.encode('utf-8')).decode('utf-8')

filepath = r"/Users/gogin/Desktop/ChessApp/ChessApp VS Code/XL Spreadsheets/ProfileDatabase.xlsx"
primeEOS = "mp4n4f2mq3ca"

