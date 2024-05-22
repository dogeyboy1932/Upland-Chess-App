from FIXED_VARIABLES import challenges_db

from Upland.Escrow.refund_escrow import RefundEscrowContainer

def ChallengeDeleted(link):  # <- Delete Button clicked
    challenge = challenges_db.find_one({"link": link})

    escrowID = str(challenge.get("escrowID", ""))
    returnVal = RefundEscrowContainer(escrowID)

    if returnVal != "Processing":
        challenges_db.delete_one({"link": link})
        
    return returnVal