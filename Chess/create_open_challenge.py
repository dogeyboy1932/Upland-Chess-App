import berserk
client = berserk.Client()


def CreateOpenChallenge(challenger, speed, increment, variant, rated, name):
    if name == "":
        name = (challenger, "'s Game")

    if speed == "rapid": speed = 600

    if rated == "Yes": rated = True
    else: rated = False

    client.challenges.create_open()

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


# run()










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

# rated,  # Casual or no?
# clockLimit,
# clockIncrement,
# rules,  # Rematch/noRematch etc