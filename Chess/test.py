from FIXED_CHESS_VARIABLES import cfilepath
from FIXED_CHESS_VARIABLES import client
import pandas as pd

df = pd.read_excel(cfilepath)
print(df)

# import berserk

# # Replace 'your_client_id' and 'your_client_secret' with your actual Lichess API credentials
# client_id = 'your_client_id'
# client_secret = 'your_client_secret'

# # Specify the required scopes, e.g., 'board:write'
# scopes = ['board:write']

# # Obtain a token with the specified scopes
# # token = berserk.auth.create_session(client_id, client_secret, scopes)
# token = berserk.Client()

# # from FIXED_CHESS_VARIABLES import token
# # import berserk
# # client = berserk.Client()
# client = berserk.Client(session=token)

# # headers = {"Authorization": f"Bearer {token}"}

# client.board.post_message("1yizMtMm", "TESTING", True)

# # for challenge in challenges:
# #     print(challenge)



