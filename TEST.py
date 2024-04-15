import berserk
client = berserk.Client()

# from Chess.FIXED_CHESS_VARIABLES import client


def CreateOpenChallenge(challenger, speed, increment, variant, rated, name):
    if name == "":
        name = (challenger, "'s Game")

    if speed == "rapid": speed = 600

    if rated == "Yes": rated = True
    else: rated = False

    newChallenge = client.challenges.create_open(
        clock_limit=speed,
        clock_increment=increment,
        variant=variant,
        position=None,
        rated=rated,
        name=name,
    )

    return newChallenge


def run():
    challenger = "trashboatsr"
    speed = "rapid"
    increment = 0
    variant = "standard"
    rated = "No"
    name = "Akhil vs His Team"

    game = CreateOpenChallenge(challenger, speed, increment, variant, rated, name)
    print(game)


run()










    # clock_limit: int | None = None,
    # clock_increment: int | None = None,
    # variant: Literal[
    #              "chess960", "kingOfTheHill", "threeCheck", "antichess", "atomic", "horde", "racingKings", "crazyhouse", "fromPosition", "standard"] | None = None,
    # position: str | None = None,
    # rated: bool | None = None,
    # name: str | None = None) -> dict[str, Any]



# def create_open_ended_challenge():
#     url = 'https://lichess.org/api/challenge/open'
#
#     bool_var = False
#     var = str(bool_var)
#
#     headers = {
#         'rated': var,
#         'clock.limit': "600",
#         'clock.increment': "0",
#         'variant': "standard",
#         'name': "Akhil Challenge",
#         'rules': "noRematch",
#     }
#
#     response = requests.post(url, headers=headers)
#     data = response.json()
#
#     if response.status_code == 200:
#         print(response.json())
#     else:
#         print(f'Request failed with status code {response.status_code}')
#
#     # gameID = data.get('challenge').get('id')
#



# def create_open_ended_challenge():
#     url = 'https://lichess.org/api/challenge/open'
#
#     headers = {
#         'rated': "true",
#         'clock.limit': '600',
#         'clock.increment': "0",
#         'variant': "standard",
#         'name': "Akhil Challenge",
#         'rules': "noRematch",
#     }
#
#     response = requests.post(url, headers=headers)
#     data = response.json()
#
#     if response.status_code == 200:
#         print(data)
#         return data
#         # return data['challenge']['id']
#     else:
#         print(f'Request failed with status code {response.status_code}')


# def run():
#     create_open_ended_challenge()
#
#
# run()





# from openpyxl import load_workbook
# from Chess.FIXED_CHESS_VARIABLES import cfilepath
# from Chess.get_chess_info import GetLichessRating
# from Upland.create_escrow_container import CreateEscrowContainer

# import pandas as pd

# def AppendChallenge(challenger, wager, thisGame):
#     workbook = load_workbook(cfilepath)
#     worksheet = workbook['Sheet']

#     # Grabbing Details
#     gameID = thisGame['challenge']['id']
#     rating = GetLichessRating(challenger, "rapid")
#     link = thisGame['challenge']['url']
#     escrowID = CreateEscrowContainer()

#     # Making data
#     data = [gameID, challenger, rating, wager, link, escrowID, False, "blank"]

#     # Appending data to spreadsheet
#     worksheet.append(data)

#     workbook.save(cfilepath)
#     workbook.close()

#     return gameID

# def AppendInitial():
#     workbook = load_workbook(cfilepath)
#     worksheet = workbook['Sheet']

#     data = ["gameID", "challenger", "rating", "wager", "link", "escrowID", "accepted?", "accepter"]

#     worksheet.append(data)

#     workbook.save(cfilepath)
#     workbook.close()

    
# AppendInitial()


# nftim	nftim	1,500	4,618	eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiI5Y2I0ZTAxMC1lM2M3LTExZWQtYTAzOS1mMTg3YWI1NGMyZjAiLCJhcHBJZCI6MjMyLCJ0b2tlbklkIjoiMjEyNTM0ZGUtYTc0My00MDVlLWJiNzYtMmM3MzY5YzFmZjA2IiwiaWF0IjoxNzEzMTExMTQ0fQ.VMs7yovq4mh1IP4U6ohuBMpV5Scb3aT46wIXH6oIWrY	jocxxixgixq1	tim
