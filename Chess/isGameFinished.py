from FIXED_CHESS_VARIABLES import client


def isGameFinished(gameID):
    try:
        client.games.export(gameID)
        return True
    except:
        return False
    # print("THERE2")

# AKHIL NOTE: THIS IS PROLLY INEFFICIENT FOR DETERMINING IF A GAME IS OVER OR NOT...MIGHT NEED TO UPDATE

def run():
    gameID = "W26Ykr8M"
    print(isGameFinished(gameID))

# run()