from FIXED_VARIABLES import cfilepath
from FIXED_VARIABLES import credential
from openpyxl import load_workbook
from Chess.game_winner import GameWinner
from Upland.query_spreadsheet import QueryForEOSID
from Chess.query_challenge_idx import GetChallengeIdx
from Upland.resolve_escrow_container import ResolveEscrow

from Upland.get_escrow_container import GetEscrowContainer



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

    return ResolveEscrow(eid, winnerID, loserID, drawStatus, credential, wager)

def run():
    gameId = "W26Ykr8M"
    gameEnded(gameID=gameId)

# run()