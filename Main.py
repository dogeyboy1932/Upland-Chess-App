from flask import Flask, request
from Upland.FIXED_VARIABLES import filepath
import pandas as pd
import asyncio
from Upland.append_profile import AppendProfile
from Upland.create_profile import CreateProfile
from Chess.get_challenges import GetAllChallenges

app = Flask(__name__)

games = []


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

@app.route('/', methods=['GET'])
def hello():
    return "test"

@app.route('/lichess', methods=['POST'])
def postid():
    data = request.json

    uplandID = data['upland']
    lichessID = data['lichess']

    # Debug
    print(uplandID, lichessID)

    # Save the lichess ID to the database using the upland ID

@app.route('/createchallenge', methods=['POST'])
def create_challenge():
    data = request.json

    wager = data['wager']

    # These need to be retrieved from the frontend somehow (they can probably be stored in localStorage for now, since this is a dev site)
    lichessID = data['lichess']
    uplandID = data['upland']

    # Use challengeButtonClicked() from Chess.__run_chess_app.py to retrieve the escrow container ID and the chess game link

    # RETURN THE LINK SO IT CAN BE ADDED TO THE FRONTEND

@app.route('/challengeclicked', methods=['POST'])
def challenge_clicked():
    data = request.json

    challenge_id = data['challenge']
    lichess_id = data['lichess']

    # Use challengeAccepted() from Chess.__run_chess_app.py to run the game

    # What can be done is add this game to a map/set of IDs, and then have a 
    # loop to keep checking whether the game ended and who won
    # Then run a function to resolve the escrow container and give the winner his cash!

    # EXAMPLE:
    # games.append(challenge_id)

@app.route("/challenges", methods=['GET'])
def get_challenges():
    # Iterate over the challenges list and return to the frontend a list of challenges
    # The columns should be [Link, UplandID, lichessID, wager amount, lichess rating] (can skip the rating since it can be hard for now)

    
    return GetAllChallenges()

@app.route('/getBalance', methods=['POST'])
def get_balance():
    data = request.json

    uplandID = data['upland']

    # Get the balance of the user and return it using get_user_balance and get_user_profile
    return 

def AddInitial():
    # filepath = r"/Users/gogin/Desktop/Metaverse/ChessApp Pycharm Code/ChessDatabase1.xlsx"
    data = ["Lichess ID", "Upland Username", "Lichess Rating", "Balance", "Bearer Token", "Eos Upland ID"]
    AppendProfile(data)


def stop():
    task.cancel()

async def checkGames():
    for game in games:
        # CHECK IF GAME ENDED. IF GAME ENDED, RESOLVE ESCROW CONTAINER
        print("a") # debug
    await asyncio.sleep(300)

if __name__ == '__main__':
    AddInitial()
    app.run(host="0.0.0.0", port=2000)
    loop = asyncio.get_event_loop()
    loop.call_later(5, stop)
    task = loop.create_task(checkGames())

    try:
        loop.run_until_complete(task)
    except asyncio.CancelledError:
        pass










# print(user_id)
# print(access_token)

# print("MAIN PRINT")
# print("IT WORKS")
