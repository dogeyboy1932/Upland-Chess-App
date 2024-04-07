# # https://lichess.org/api/challenge

import berserk
client = berserk.Client()


def IsGameValid():
    
    challenges = client.challenges

    print(challenges)

    # return newChallenge


def run():
    IsGameValid()


run()