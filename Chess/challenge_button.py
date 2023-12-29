from openpyxl import load_workbook

from Chess.FIXED_CHESS_VARIABLES import cfilepath
from Chess.create_open_challenge import CreateOpenChallenge
from Chess.append_challenge import AppendChallenge
from Chess.query_challenge_idx import GetChallengeIdx

from Upland.join_escrow_container import JoinEscrow
from Upland.get_bearer_token import GetBearerToken
from Upland.query_lichessID import QueryForLichessID
from Upland.get_user_balance import GetUserBalanceOnSheet


# FRONTEND DEPENDENT

def ChallengeButtonClicked(uplandID, rated_, wager_):

    if QueryForLichessID(uplandID) == -1:
        print("UPLAND-ID DOES NOT EXIST")
        return -1
    

    if (int(wager_) > GetUserBalanceOnSheet(uplandID)):
        print("NOT ENOUGH BALANCE")
        return -2
    

    challenger = QueryForLichessID(uplandID)
    speed = "rapid"  
    increment = 0 
    rated = rated_
    variant = "standard"
    name = "Challenge by " + uplandID
    wager = wager_

    # Challenge under terms is created
    thisGame = CreateOpenChallenge(challenger=challenger, speed=speed, increment=increment, variant=variant,
                                   rated=rated, name=name)

    # Challenge is appended to spreadsheet (database) + Escrow is created & appended + Challenge ID is extracted
    gameID = AppendChallenge(challenger, wager, thisGame)
    challengeIdx = GetChallengeIdx(gameID)

    # Load Updated Spreadsheet
    workbook = load_workbook(cfilepath)['Sheet']
    # chessWorksheet = workbook['Sheet']

    # Join Escrow Container of this game
    bearer = GetBearerToken(uplandID)
    eid = str(workbook[challengeIdx][5].value)
    wager = int(wager)

    # JoinEscrow(bearer, eid, wager)
    

def run():
    uplandID = "dogeyboy19"
    wager = 100
    rated = "No"

    ChallengeButtonClicked(uplandID, rated, wager)

# run()