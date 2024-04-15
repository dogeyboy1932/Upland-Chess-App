from openpyxl import load_workbook

from FIXED_VARIABLES import cfilepath, client
from Chess.game_winner import GameWinner
from Upland.resolve_escrow_container import ResolveEscrow
from Upland.SpreadsheetEditing.query_spreadsheet import QueryForEOSID, GetChallengeIdx

# AKHIL NOTE: THIS IS PROLLY INEFFICIENT FOR DETERMINING IF A GAME IS OVER OR NOT...MIGHT NEED TO UPDATE
def isGameFinished(gameID):
    try:
        client.games.export(gameID)
        return True
    except:
        return False
    

def gameEnded(gameID):
    workbook1 = load_workbook(cfilepath)
    chessWorksheet = workbook1['Sheet']

    gameResult = GameWinner(gameID)
    winner = gameResult[0]
    loser = gameResult[1] # loser = "trashboatsr"
    drawStatus = gameResult[2]

    winnerID = QueryForEOSID(winner)
    loserID = QueryForEOSID(loser)

    challengeIdx = GetChallengeIdx(gameID)
    eid = chessWorksheet[challengeIdx][5].value

    wager = chessWorksheet[challengeIdx][3].value
    
    # print(GetEscrowContainer(eid))

    return ResolveEscrow(eid, winnerID, loserID, drawStatus, wager)


def run():
    gameId = "W26Ykr8M"
    gameEnded(gameID=gameId)

# run()