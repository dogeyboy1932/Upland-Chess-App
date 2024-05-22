from FIXED_VARIABLES import profiles_db

from FIXED_VARIABLES import challenges_db

from pymongo import MongoClient

def QueryForLichessID(uplandID):
    # Query the MongoDB collection for the uplandID
    user_profile = profiles_db.find_one({"Upland Username": uplandID})
    
    # Return the Lichess ID if the profile exists, otherwise return -1
    return user_profile.get("Lichess ID", -1) if user_profile else -1

def GetUserBalanceOnSheet(uplandID):
    # Query the MongoDB collection for the uplandID
    user_profile = profiles_db.find_one({"Upland Username": uplandID})
    
    # Return the balance if the profile exists, otherwise return -1
    return user_profile.get("Balance", -1) if user_profile else -1

def GetBearerToken(uplandID):
    # Query the MongoDB collection for the uplandID
    user_profile = profiles_db.find_one({"Upland Username": uplandID})
    
    # Return the bearer token if the profile exists, otherwise return -1
    return user_profile.get("Bearer Token", -1) if user_profile else -1

def QueryForPassword(uplandID):
    # Query the MongoDB collection for the uplandID
    user_profile = profiles_db.find_one({"Upland Username": uplandID})
    
    # Return the password if the profile exists, otherwise return -1
    return user_profile.get("Password", -1) if user_profile else -1


def QueryForEOSID(lichessID):
    # Query the MongoDB collection for the profile with the given lichessID
    user_profile = profiles_db.find_one({"Lichess ID": lichessID})
    
    # Return the EOS Upland ID if the profile exists, otherwise return -1
    return user_profile.get("Eos Upland ID", -1) if user_profile else -1


def QueryForUplandID(lichessID):
    # Query the MongoDB collection for the profile with the given lichessID
    user_profile = profiles_db.find_one({"Lichess ID": lichessID})
    
    # Return the Upland ID if the profile exists, otherwise return -1
    return user_profile.get("Upland Username", -1) if user_profile else -1


def GetCredentialsByID(userId):
    # Query the MongoDB collection for the profile with the given userId
    user_profile = profiles_db.find_one({"UserId": userId})
    
    # If the profile exists, return the Upland Username and Password as a tuple
    return [user_profile.get("Upland Username", ""), user_profile.get("Password", "")] if user_profile else -1




# By Index
def QueryForEOS(gameID):
    challenge = challenges_db.find_one({"gameID": gameID})
    
    return str(challenge.get("escrowID", "")) if challenge else ""


def QueryForLink(gameID):
    challenge = challenges_db.find_one({"gameID": gameID})
    
    return str(challenge.get("link", "")) if challenge else ""


def QueryForWager(gameID):
    challenge = challenges_db.find_one({"gameID": gameID})
    
    return str(challenge.get("wager", "")) if challenge else ""



def QueryGameIDByLink(link):
    challenge = challenges_db.find_one({"link": link})
    
    return str(challenge.get("gameID", "")) if challenge else ""
