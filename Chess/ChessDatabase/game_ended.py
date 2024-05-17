from openpyxl import load_workbook

from FIXED_VARIABLES import cfilepath, client

from Chess.ChessDatabase.game_winner import GameWinner

from Upland.Escrow.resolve_escrow_container import ResolveEscrow
from Upland.SpreadsheetEditing.query_spreadsheet import QueryForEOSID, GetChallengeIdx

# AKHIL NOTE: THIS IS PROLLY INEFFICIENT FOR DETERMINING IF A GAME IS OVER OR NOT...MIGHT NEED TO UPDATE
def isGameFinished(gameID):
    try:
        client.games.export(gameID)
        return True
    except:
        return False
    

def gameEnded(gameID):
    workbook = load_workbook(cfilepath)
    chessWorksheet = workbook['Sheet']

    challengeIdx = GetChallengeIdx(gameID)
    gameResult = GameWinner(gameID)

    if gameResult == None: return -2 # THIS IS JUST AN ERROR

    winner = QueryForEOSID(gameResult[0])
    loser = QueryForEOSID(gameResult[1])
    drawStatus = gameResult[2]
    eid = chessWorksheet[challengeIdx][5].value
    wager = chessWorksheet[challengeIdx][3].value
    
    return ResolveEscrow(eid, winner, loser, drawStatus, wager)

