from FIXED_CHESS_VARIABLES import client
# from setup_file import requests


def GameLoser(gameID):
    thisGame = client.games.export(gameID)

    if thisGame.get('status') == 'draw':
        return "DRAW"

    winner = thisGame.get('winner')

    if winner == 'black':
        try:
            return thisGame.get('players').get('white').get('user').get('id')
        except:
            return "{}"

    elif winner == 'white':
        try:
            return thisGame.get('players').get('black').get('user').get('id')
        except:
            return "{}"

#
# def run():
#     game_id = "vhgbjWnL"
#     print(GameLoser(game_id))
#
#     game_id = "RLyFq9MX"
#     print(GameLoser(game_id))
#
#
# run()