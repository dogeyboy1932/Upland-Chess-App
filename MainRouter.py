from flask import Flask, request, jsonify
import pandas as pd
import json

from FIXED_VARIABLES import NumpyArrayEncoder

from Upland.Auth_code import Verify
from Upland.SpreadsheetEditing.create_profile import CreateProfile
from Upland.SpreadsheetEditing.edit_profile import AppendProfileHeader, DeleteProfile
from Upland.SpreadsheetEditing.fill_profile import FillProfile
from Upland.SpreadsheetEditing.query_spreadsheet import QueryForPassword, QueryForLichessID, GetCredentialsByID
from Upland.Escrow.get_escrow_container import GetEscrowContainer

from Chess.NewChallenge.append_challenge import AppendChallengeHeader
from Chess.ChessDatabase.iterate_database import Iterate, UpdateBalances
from Chess.ChessDatabase.handle_finished_games import HandleFinishedGames
from Chess.Buttons.delete_button import ChallengeDeleted
from Chess.NewChallenge.challenge_button import ChallengeButtonClicked
from Chess.Buttons.accept_button import ChallengeAccepted
from Chess.Buttons.cancel_button import ChallengeCanceled
from Chess.get_lichess_info import GetVariant

from flask_cors import CORS 

app = Flask(__name__)

CORS(app)
app.logger.disabled = True

@app.route('/database', methods=['POST'])
def ChallengeDatabase():
    
    UpdateBalances()
    HandleFinishedGames() 
    arr = Iterate()
    
    encodedNumpyData = json.dumps({"array": arr}, cls=NumpyArrayEncoder)

    return encodedNumpyData


@app.route('/auth', methods=['POST'])
def Auth():
    return Verify()


@app.route('/password', methods=['POST'])
def Password():
    uplandID = request.get_json().get('uplandID')

    return str(QueryForPassword(uplandID))


@app.route('/getLichessID', methods=['POST'])
def GetLichessID():
    uplandID = request.get_json().get('uplandID')

    return str(QueryForLichessID(uplandID))


@app.route('/getLichessInfo', methods=['POST'])
def GetLichessInfo():
    lichessID = request.get_json().get('lichessId')

    return jsonify(GetVariant(lichessID, "rapid"))


@app.route('/getEscrow', methods=['POST'])
def GetEscrow():
    escrowId = request.get_json().get('escrowId')

    # print(jsonify(GetEscrowContainer(escrowId)))

    return jsonify(GetEscrowContainer(escrowId))


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


@app.route('/deleteProfile', methods=['POST'])
def DeleteProf():
    uplandID = request.get_json().get('uplandIDRemove')
    password = request.get_json().get('passwordRemove')

    return DeleteProfile(uplandID, password)  


@app.route('/submit-details', methods=['POST'])
def ChallengeButton():
    
    data = request.get_json()

    uplandID = data.get('upland')
    rated = data.get('rated')
    wager = data.get('wager')
    speed = "rapid" # Can be others later on
    variant = "standard" # Can be others later on
    name = "Challenge by " + uplandID
    increment = 0

    return str(ChallengeButtonClicked(uplandID, rated, wager, speed, variant, name, increment))


@app.route('/', methods=['POST'])
def respond():
    try:
        data = request.json
    except:
        print("NOT VALID REQUEST")
        return str(-1)
    
    # print(data)

    if data['type'] == 'AuthenticationSuccess':
        access_token = data['data']['accessToken']
        CreateProfile(access_token)

        # print(access_token)
        # df = pd.read_excel(filepath)
        # print(df)
    
    elif data['type'] == 'UserDisconnectedApplication':
        credentials = GetCredentialsByID(data['data']['userId'])

        if credentials == -1: 
            print("UNABLE TO DELETE PROFILE")
            return

        uplandId = credentials[0]
        password = credentials[1]

        DeleteProfile(uplandId, password)

    return "success"


@app.route('/test')
def test():
    response_body = {
        "name": "Akhil",
        "about" :"Hello! I'm a python stack developer"
    }


    # if (request):
    #     return request + " ..."

    return response_body


# HELPER USE THIS ONLY IF SPREADSHEETS ARE EMPTY
def AddInitial():
    AppendChallengeHeader()
    AppendProfileHeader()


if __name__ == '__main__':
    app.run()

