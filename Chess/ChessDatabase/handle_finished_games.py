from FIXED_VARIABLES import challenges_db

from Chess.ChessDatabase.game_ended import gameEnded, isGameFinished

from Upland.Escrow.get_escrow_container import GetEscrowContainer


def FindAndRemoveRow(gameID):  # THIS REMOVES THE ROW IN THE CHALLENGES DATABASE CONTAINING THE GAMEID
    challenges_db.delete_one({"gameID": gameID})


def MarkResolving(gameID): # THIS INDICATES THAT THE CHESS GAME IS OVER AND THE ESCROW IS BEING RESOLVED
    challenges_db.update_one(
        {"gameID": gameID},
        {"$set": {
            "readyStatus": "RESOLVING",
        }}
    )


def MarkCompleted(gameID): # THIS INDICATES THAT THE CHESS GAME IS OVER AND THE ESCROW IS BEING RESOLVED
    challenges_db.update_one(
        {"gameID": gameID},
        {"$set": {
            "accepted?": "COMPLETED",
        }}
    )


def MarkReadyStatus(escrowID):  # THIS INDICATES THAT THE FUNDS HAVE TRANSFERRED TO THE ESCROW
    escrow = GetEscrowContainer(escrowID)

    if (escrow != -1):
        success = True

        assets = escrow['assets']
        
        for i in assets:
            # print("THIS: ", i['status'])
            if i['status'] == 'user_signature_requested' or i['status'] == 'expired':
                success = False
                break
            
        if success:
            challenges_db.update_one(
                {"escrowID": escrowID},
                {"$set": {
                    "readyStatus": "YES",
                }}
            )


def HandleFinishedGames():
    challenges = challenges_db.find()
 
    finishedGames = []
    for challenge in challenges:
        gameID = str(challenge.get("gameID", ""))
        escrowID = challenge.get("escrowID", "")
        isAccepted = str(challenge.get("accepted?", ""))
        
        if isGameFinished(gameID):
            finishedGames.append(gameID)

        if (isAccepted != "NO"):
            MarkReadyStatus(escrowID)
    

    for game in finishedGames:
        status = gameEnded(game)
        print(status)
    
        if (status == -3):   # This means escrow was not resolvable (due to insufficient funds)
            FindAndRemoveRow(game)
        elif (status == -2):
            MarkResolving(game)
        
        MarkCompleted(game)
            
