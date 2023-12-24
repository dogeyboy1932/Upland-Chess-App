from flask import Flask, request, jsonify
import pandas as pd
import json

from Upland.FIXED_VARIABLES import filepath
from Upland.append_profile import AppendProfile
from Upland.create_profile import CreateProfile
from Upland.query_uplandID_index import QueryUplandIDRow

from Chess.FIXED_CHESS_VARIABLES import NumpyArrayEncoder
from Chess.render_database import Iterate
from Chess.handle_finished_games import HandleFinishedGames


app = Flask(__name__)
app.logger.disabled = True

@app.route('/test', methods=['POST'])
def ChallengeButtonClicked():
    return "Success"  # UPDATE THIS

@app.route('/database', methods=['POST'])
def ChallengeDatabase():
    HandleFinishedGames()
    arr = Iterate()

    encodedNumpyData = json.dumps({"array": arr}, cls=NumpyArrayEncoder)

    return encodedNumpyData


@app.route('/', methods=['POST'])
def respond():

    data = request.json

    if data['type'] == 'AuthenticationSuccess':
        user_id = data['data']['userId']
        access_token = data['data']['accessToken']

        print(access_token)

        CreateProfile(access_token, user_id)

        df = pd.read_excel(filepath)
        print(df)

    return "success"


def AddInitial():
    data = ["Lichess ID", "Upland Username", "Lichess Rating", "Balance", "Bearer Token", "Eos Upland ID"]
    if QueryUplandIDRow("Upland Username") == -1:
        AppendProfile(data)


if __name__ == '__main__':
    AddInitial()
    app.run(host="0.0.0.0", port=5000)








# print(user_id)
# print(access_token)

# print("MAIN PRINT")
# print("IT WORKS")


# import http.client
#
# conn = http.client.HTTPSConnection('eot5eeu5bgtksf7.m.pipedream.net')
# conn.request("POST", "/", '{"test": "event"}', {'Content-Type': 'application/json'})

# filepath = r"/Users/gogin/Desktop/Metaverse/ChessApp Pycharm Code/ChessDatabase1.xlsx"
