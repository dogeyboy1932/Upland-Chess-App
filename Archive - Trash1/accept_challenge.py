import berserk
client = berserk.Client()


def AcceptChallenge(gameID):
    res = client.challenges.accept(gameID)
    return res


def run():
    gameId = "7qPDmgrN"
    print(AcceptChallenge(gameId))

# run()