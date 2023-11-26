from Chess.FIXED_CHESS_VARIABLES import client


def getAccount(userID):
    return client.users.get_by_id(userID)
