from Chess.FIXED_CHESS_VARIABLES import client
# from get_chess_account import getAccount


def getAccount(userID):
    return client.users.get_by_id(userID)


def GetLichessRating(lichessID, variant):
    accountInfo = getAccount(lichessID)
    rating = accountInfo[0]['perfs'][variant]['rating']

    return rating
