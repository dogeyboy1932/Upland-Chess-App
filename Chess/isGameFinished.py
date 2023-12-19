from FIXED_CHESS_VARIABLES import client


def isGameFinished(gameID):

    try:
        client.games.export(gameID)
        return True
    except:
        return False


# if gameID == "39TVRlxw" or gameID == "mDJmq7Gi":
#     return True
