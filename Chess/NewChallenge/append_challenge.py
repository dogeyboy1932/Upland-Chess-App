from FIXED_VARIABLES import challenges_db

from Chess.get_lichess_info import GetLichessRating

from Upland.Escrow.create_escrow_container import CreateEscrowContainer


def AppendChallenge(challenger, wager, thisGame):
    # Grabbing Details
    gameID = thisGame['challenge']['id']
    rating = GetLichessRating(challenger, "rapid")
    link = thisGame['challenge']['url']
    escrowID = CreateEscrowContainer()

    # Making data
    data = {
        "gameID": gameID,
        "challenger": challenger,
        "rating": rating,
        "wager": wager,
        "link": link,
        "escrowID": escrowID,
        "accepter": "blank",
        "accepted?": "NO",
        "readyStatus": "NO"
    }

    # Appending data to spreadsheet
    challenges_db.insert_one(data)

    return escrowID, link