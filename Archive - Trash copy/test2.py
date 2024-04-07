import berserk
token = "lip_ZnYbIrvWC5KDwB8P0wJu"

session = berserk.TokenSession(token)
client = berserk.Client(session=session)

gameID = "gIMf5rSl"
board = berserk.clients.Board(session=session)

board.post_message(game_id=gameID,text="HI",spectator=False)


# for event in stream:
#     print(event)