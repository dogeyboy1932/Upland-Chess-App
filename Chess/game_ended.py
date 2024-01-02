from Chess.FIXED_CHESS_VARIABLES import cfilepath
from Chess.FIXED_CHESS_VARIABLES import credential
from openpyxl import load_workbook
from Chess.game_winner import GameWinner
from Upland.query_for_eosId import QueryForEOSID
from Chess.query_challenge_idx import GetChallengeIdx
from Upland.resolve_escrow_container import ResolveEscrow

from Upland.get_escrow_container import GetEscrowContainer

workbook1 = load_workbook(cfilepath)
chessWorksheet = workbook1['Sheet']


def gameEnded(gameID):
    print("GAME ENDED")
    gameResult = GameWinner(gameID)
    winner = gameResult[0]
    loser = gameResult[1] # loser = "trashboatsr"
    drawStatus = gameResult[2]

    winnerID = QueryForEOSID(winner)
    loserID = QueryForEOSID(loser)

    challengeIdx = GetChallengeIdx(gameID)
    eid = chessWorksheet[challengeIdx][5].value

    print(GetEscrowContainer(eid))

    ResolveEscrow(eid, winnerID, loserID, drawStatus, credential)
    # print("END")


def run():
    gameId = "W26Ykr8M"
    gameEnded(gameID=gameId)

# run()