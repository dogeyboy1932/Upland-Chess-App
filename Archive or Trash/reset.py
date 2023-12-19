# Frontend Dependent


# def resetButtonClicked():

# If button is clicked, functions will be called to "update"
#
#  - Check for finished games...iterate through 'challengeMap' and record finished games
#  - If game is finished:
#     - Update the frontend database (remove finished games)
#     - Resolve export containers for finished games (params: gameID + players)
#
# This feature might need to get automated in the future

from finished_games import RemoveFinishedGames


def resetButtonClicked():
    RemoveFinishedGames()

