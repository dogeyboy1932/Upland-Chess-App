# Hit the run button ^^^

from flask import Flask, request, jsonify
import pandas as pd
import json

from openpyxl import load_workbook

from Upland.FIXED_VARIABLES import credential
from Upland.FIXED_VARIABLES import filepath
from Upland.append_profile import AppendProfile
from Upland.create_profile import CreateProfile
from Upland.query_spreadsheet import QueryUplandIDRow
from Upland.auth_code import Verify
from Upland.query_spreadsheet import GetPassword

from Chess.FIXED_CHESS_VARIABLES import NumpyArrayEncoder
from Chess.render_database import Iterate
from Chess.handle_finished_games import HandleFinishedGames
from Chess.challenge_button import ChallengeButtonClicked
from Chess.accept_button import ChallengeAccepted
from Chess.cancel_button import ChallengeCanceled
from Chess.handle_finished_games import ChallengeDeleted

from flask_cors import CORS 

app = Flask(__name__)
CORS(app)
app.logger.disabled = True

went = False

@app.route('/database', methods=['POST'])
def ChallengeDatabase():
    global went #FIX THIS

    if not went:
        arr = Iterate()
        went = True
    else:
        HandleFinishedGames() 
        arr = Iterate()

    encodedNumpyData = json.dumps({"array": arr}, cls=NumpyArrayEncoder)

    return encodedNumpyData


@app.route('/auth', methods=['POST'])
def Auth():
    return Verify(credential)


@app.route('/password', methods=['POST'])
def Password():
    username = request.get_json().get('username')

    return GetPassword(username)


@app.route('/accepted', methods=['POST'])
def Accepted():
    Iterate()

    accepter = request.get_json().get('currentUserUplandID')
    link = request.get_json().get('link')
    challenger = request.get_json().get('UplandID')

    ChallengeAccepted(link, challenger, accepter)

    return ChallengeDatabase()


@app.route('/cancel', methods=['POST'])
def Cancel():
    link = request.get_json().get('link')
    
    ChallengeCanceled(link)
    return "Success"


@app.route('/delete', methods=['POST'])
def Deleted():
    link = request.get_json().get('link')
    
    ChallengeDeleted(link)
    return "Success"


@app.route('/credentials', methods=['POST'])
def Credentials():
    username = request.get_json().get('username')
    password = request.get_json().get('password')

    workbook = load_workbook(filepath)
    worksheet = workbook['Sheet']

    prof_pass = -1
    for i in range(1, worksheet.max_row + 1):
        if worksheet[i][1].value == username:
            prof_pass = worksheet[i][6].value

    if (prof_pass == -1):
        return 'no profile found'
    elif (prof_pass == "null"):
        worksheet[i][6].value = password 
    else:
        return 'profile exists'        

    workbook.save(filepath)
    workbook.close()

    return 'success'


@app.route('/submit-details', methods=['POST'])
def ChallengeButton():
    data = request.get_json()

    uplandID = data.get('upland')
    rated = data.get('rated')
    wager = data.get('wager')

    return str(ChallengeButtonClicked(uplandID, rated, wager))


@app.route('/', methods=['POST'])
def respond():
    data = request.json

    if data['type'] == 'AuthenticationSuccess':
        user_id = data['data']['userId']
        access_token = data['data']['accessToken']

        # print(access_token)

        CreateProfile(access_token, user_id)

        df = pd.read_excel(filepath)
        print(df)

    return "success"


def AddInitial():
    data = ["Lichess ID", "Upland Username", "Lichess Rating", "Balance", "Bearer Token", "Eos Upland ID", "Password"]
    if QueryUplandIDRow("Upland Username") == -1:
        AppendProfile(data)


if __name__ == '__main__':
    AddInitial()
    app.run(host="0.0.0.0", port=5000, debug=True)








# print(user_id)
# print(access_token)

# print("MAIN PRINT")
# print("IT WORKS")


# import http.client
#
# conn = http.client.HTTPSConnection('eot5eeu5bgtksf7.m.pipedream.net')
# conn.request("POST", "/", '{"test": "event"}', {'Content-Type': 'application/json'})

# filepath = r"/Users/gogin/Desktop/Metaverse/ChessApp Pycharm Code/ChessDatabase1.xlsx"
