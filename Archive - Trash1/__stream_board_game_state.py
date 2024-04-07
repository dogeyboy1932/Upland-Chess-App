#NEED HELP




import berserk
token = "lip_ZnYbIrvWC5KDwB8P0wJu"

session = berserk.TokenSession(token)
client = berserk.Client(session=session)



def stream_board_game_state(game_id, bearer_token):
    url = "https://lichess.org/api/board/game/stream/"
    url += str(game_id)


    headers = {
        'Authorization': f"Bearer {bearer_token}",
    }

    response = requests.get(url, headers=headers, params={'gameId': "PF1TK1qe"})

    print(response.content)

    if response.status_code == 200:
        print(response.json())
    else:
        print(f'Request failed with status code {response.status_code}')

def run():
    gameID = "PF1TK1qe"
    bearerToken = "lip_E2i49Z8OMDLbb4xoYJCY"

    stream_board_game_state(gameID, bearerToken)


run()


