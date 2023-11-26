#NEED HELP




import berserk
token = "lip_ZnYbIrvWC5KDwB8P0wJu"

session = berserk.TokenSession(token)
client = berserk.Client(session=session)

def stream_game_state(gameID):
    return client.board.stream_game_state(gameID)


def run():
    gameID = "PF1TK1qe"
    # bearerToken = "lip_E2i49Z8OMDLbb4xoYJCY"

    # stream_board_game_state(gameID, bearerToken)
    stream = stream_game_state(gameID)

    for event in stream:
        print(event)

run()


# def stream_board_game_state(game_id, bearer_token):
#     url = "https://lichess.org/api/board/game/stream/"
#     url += str(game_id)
#
#
#     headers = {
#         'Authorization': f"Bearer {bearer_token}",
#     }
#
#     response = requests.get(url, headers=headers, params={'gameId': "PF1TK1qe"})
#
#     print(response.content)
#
#     if response.status_code == 200:
#         print(response.json())
#     else:
#         print(f'Request failed with status code {response.status_code}')
#
# def run():
#     gameID = "PF1TK1qe"
#     bearerToken = "lip_E2i49Z8OMDLbb4xoYJCY"
#
#     stream_board_game_state(gameID, bearerToken)
#
#
# run()


# def stream_board_game_state(gameID):
#     thisGame = client.board.stream_game_state(game_id=gameID)
#
#     thisGame2 = client.games.ru
#
#     return thisGame
#
# def run():
#     gameID = "RLyFq9MX"
#
#     state = stream_board_game_state(gameID)
#
#     print(state)
#
# run()

def stream_board_game_state(gameID):
    # is_polite = True
    return client.board.stream_incoming_events()

    # for event in client.bots.stream_incoming_events():
    #     if event['type'] == 'challenge':
    #         print(event)
        # elif event['type'] == 'gameStart':
        #     game = Game(event['id'])
        #     game.start()

def run():
    gameID = "RLyFq9MX"

    state = stream_board_game_state(gameID)

    # for event in state:
    #     print(event)

    print(state)

run()

