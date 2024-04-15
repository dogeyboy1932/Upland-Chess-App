import berserk
client = berserk.Client()


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


# run()
