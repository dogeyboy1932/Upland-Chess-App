from Chess.FIXED_CHESS_VARIABLES import cfilepath
from Chess.FIXED_CHESS_VARIABLES import credential
from openpyxl import load_workbook
from Chess.chess_game_winner import GameWinner
from Upland.query_for_eosId import QueryForEOSID
from Chess.query_challenge_idx import GetChallengeIdx
from Upland.resolve_escrow_container import ResolveEscrow


workbook1 = load_workbook(cfilepath)
chessWorksheet = workbook1['Sheet']


def gameEnded(gameID):
    gameResult = GameWinner(gameID)
    winner = gameResult[0]
    loser = gameResult[1]
    drawStatus = gameResult[2]

    winnerID = QueryForEOSID(winner)
    loserID = QueryForEOSID(loser)

    challengeIdx = GetChallengeIdx(gameID)
    eid = chessWorksheet[challengeIdx][5].value

    # ResolveEscrow(eid, winnerID, loserID, drawStatus, credential)


def run():
    gameId = "8s1uE1np"
    gameEnded(gameID=gameId)

# run()