from flask import Flask, request
import pandas as pd
import json

from FIXED_VARIABLES import credential, filepath, NumpyArrayEncoder

from Upland.auth_code import Verify
from Upland.create_profile import CreateProfile
from Upland.SpreadsheetEditing.edit_profile import AppendProfileHeader
from Upland.SpreadsheetEditing.fill_profile import FillProfile
from Upland.SpreadsheetEditing.query_spreadsheet import GetPassword, QueryForLichessID

from Chess.append_challenge import AppendChallengeHeader
from Chess.render_database import Iterate, UpdateBalances
from Chess.handle_finished_games import HandleFinishedGames, ChallengeDeleted
from Chess.challenge_button import ChallengeButtonClicked
from Chess.accept_button import ChallengeAccepted
from Chess.cancel_button import ChallengeCanceled

from flask_cors import CORS 

app = Flask(__name__)

CORS(app)
app.logger.disabled = True

@app.route('/database', methods=['POST'])
def ChallengeDatabase():
    HandleFinishedGames() 
    UpdateBalances()

    arr = Iterate()
    encodedNumpyData = json.dumps({"array": arr}, cls=NumpyArrayEncoder)

    print("RESET")
    
    return encodedNumpyData


@app.route('/auth', methods=['POST'])
def Auth():
    return Verify(credential)


@app.route('/password', methods=['POST'])
def Password():
    uplandID = request.get_json().get('uplandID')

    password = GetPassword(uplandID)
    # print(password)

    return password


@app.route('/getLichessID', methods=['POST'])
def GetLichessID():
    uplandID = request.get_json().get('uplandID')

    return QueryForLichessID(uplandID)


@app.route('/accepted', methods=['POST'])
def Accepted():
    Iterate()

    accepter = request.get_json().get('currentUserUplandID')
    link = request.get_json().get('link')

    res = ChallengeAccepted(link, accepter)
        
    return str(res)



@app.route('/cancel', methods=['POST'])
def Cancel():
    link = request.get_json().get('link')
    
    ChallengeCanceled(link)
    return "Success"


@app.route('/delete', methods=['POST'])
def Deleted():
    link = request.get_json().get('link')

    return ChallengeDeleted(link)
    


@app.route('/credentials', methods=['POST'])
def Credentials():
    uplandID = request.get_json().get('uplandID')
    lichessID = request.get_json().get('lichessID')
    password = request.get_json().get('password')

    return FillProfile(uplandID, lichessID, password)   


@app.route('/submit-details', methods=['POST'])
def ChallengeButton():
    
    data = request.get_json()

    uplandID = data.get('upland')
    rated = data.get('rated')
    wager = data.get('wager')

    return str(ChallengeButtonClicked(uplandID, rated, wager))


@app.route('/', methods=['POST'])
def respond():
    try:
        data = request.json
    except:
        var = 1

    if data['type'] == 'AuthenticationSuccess':
        access_token = data['data']['accessToken']

        CreateProfile(access_token)

        # print(access_token)

        df = pd.read_excel(filepath)
        print(df)

    return "success"


@app.route('/test')
def test():
    response_body = {
        "name": "Akhil",
        "about" :"Hello! I'm a python stack developer"
    }
    return response_body


# HELPER USE THIS ONLY IF SPREADSHEETS ARE EMPTY
def AddInitial():
    AppendChallengeHeader()
    AppendProfileHeader()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug=True)

