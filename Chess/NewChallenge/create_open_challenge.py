import berserk
client = berserk.Client()


# IMPROVE: CAN CREATE VARIETY OF CHALLENGES LATER ON
def CreateOpenChallenge(challenger, speed, increment, variant, rated, name):
    if name == "": name = (challenger, "'s Game")

    if speed == "rapid": speed = 600
    
    rated = (rated == "Yes")

    newChallenge = client.challenges.create_open(
        clock_limit=speed,
        clock_increment=increment,
        variant=variant,
        position=None,
        rated=rated,
        name=name,
    )

    return newChallenge
