from FIXED_CHESS_VARIABLES import client
# from setup_file import requests

# import berserk
#
# token = "lip_ZnYbIrvWC5KDwB8P0wJu"
#
# session = berserk.TokenSession(token)
# client = berserk.Client(session=session)


def GameWinner(gameID):
    thisGame = client.games.export(gameID)

    winner = thisGame.get('winner')

    print(thisGame)

    whiteId = thisGame.get('players').get('white').get('user').get('id')
    blackId = thisGame.get('players').get('black').get('user').get('id')
    # blackId = "blank"

    if thisGame.get('status') == 'draw':
        return [whiteId, blackId, "DRAW"]

    if winner == 'white':
        try:
            return [whiteId, blackId, "NO DRAW"]
        except:
            return "{}"

    elif winner == 'black':
        try:
            return [blackId, whiteId, "NO DRAW"]
        except:
            return "{}"


def run():
    # game_id = "MVqBvxRe"
    # print(GameWinner(game_id))

    game_id = "rL3ou9hv"
    print(GameWinner(game_id))


run()



################################################

# import berserk
# import requests
# from Profile import Profile

# token = "lip_ZnYbIrvWC5KDwB8P0wJu"
#
# session = berserk.TokenSession(token)
# client = berserk.Client(session=session)

################################################



# players = thisGame.get('players')
#
# whiteProfile = players.get('white')
# blackProfile = players.get('black')
#
# whiteID = ""
# blackID = ""
#
# if whiteProfile != {}:
#     whiteID = whiteProfile.get('user').get('id')
#     # print(whiteID)
# else:
#     whiteID = "blank"
#
# if blackProfile != {}:
#     blackID = blackProfile.get('user').get('id')
#     # print(blackID)
# else:
#     whiteID = "blank"

# .get('user').get('id')    print(whiteID)

# return whiteID
# return blackID
