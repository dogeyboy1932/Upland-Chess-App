from flask import Flask, request
from FIXED_VARIABLES import filepath
import pandas as pd
from Upland.append_profile import AppendProfile
from create_profile import CreateProfile

app = Flask(__name__)


@app.route('/', methods=['POST'])
def respond():
    data = request.json

    if data['type'] == 'AuthenticationSuccess':
        user_id = data['data']['userId']
        access_token = data['data']['accessToken']

        CreateProfile(access_token, user_id)

        print(access_token)

        df = pd.read_excel(filepath)
        print(df)

    return "success"


def AddInitial():
    # filepath = r"/Users/gogin/Desktop/Metaverse/ChessApp Pycharm Code/ChessDatabase1.xlsx"
    data = ["Lichess ID", "Upland Username", "Lichess Rating", "Balance", "Bearer Token", "Eos Upland ID"]
    AppendProfile(data)


if __name__ == '__main__':
    AddInitial()
    app.run(host="0.0.0.0", port=5000)








# print(user_id)
# print(access_token)

# print("MAIN PRINT")
# print("IT WORKS")
