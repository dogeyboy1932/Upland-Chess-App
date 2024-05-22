from FIXED_VARIABLES import challenges_db, client

from Chess.ChessDatabase.game_winner import GameWinner

from Upland.Escrow.resolve_escrow_container import ResolveEscrow
from Upland.SpreadsheetEditing.query_spreadsheet import QueryForEOSID

# AKHIL NOTE: THIS IS PROLLY INEFFICIENT FOR DETERMINING IF A GAME IS OVER OR NOT...MIGHT NEED TO UPDATE
def isGameFinished(gameID):
    try:
        client.games.export(gameID)
        return True
    except:
        return False
    

def gameEnded(gameID):
    challenge = challenges_db.find_one({"gameID": gameID})
    gameResult = GameWinner(gameID)

    if gameResult == None: return -2 # THIS IS JUST AN ERROR

    winner = QueryForEOSID(gameResult[0])
    loser = QueryForEOSID(gameResult[1])
    drawStatus = gameResult[2]
    eid = int(challenge.get("escrowID", ""))
    wager = int(challenge.get("wager", ""))
    
    return ResolveEscrow(eid, winner, loser, drawStatus, wager)

