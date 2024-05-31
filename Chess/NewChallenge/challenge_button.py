from Chess.NewChallenge.create_open_challenge import CreateOpenChallenge
from Chess.NewChallenge.append_challenge import AppendChallenge

from Upland.get_user_profile import GetUserProfile
from Upland.Escrow.join_escrow_container import JoinEscrow
from Upland.SpreadsheetEditing.query_spreadsheet import QueryForLichessID, GetBearerToken, GetUserBalanceOnSheet


# TOO MANY QUERIES
def ChallengeButtonClicked(uplandID, rated_, wager_, speed, variant, name, increment):
    
    balance = GetUserBalanceOnSheet(uplandID)    
    if (balance == -1):
        # print("GET BALANCE API MESS UP")
        return -7
    
    # Eliminating all Errors
    if QueryForLichessID(uplandID) == -1:
        # print("UPLAND-ID DOES NOT EXIST")
        return -1

    if not (rated_ == "No" or rated_ == "Yes"):
        # print("Invalid Rated")
        return -2
    
    if not wager_.isnumeric():
        # print("Invalid Wager")
        return -3

    if (int(wager_) > balance):
        # print("NOT ENOUGH BALANCE")
        return -4
    
    try: 
        GetUserProfile(GetBearerToken(uplandID))['level']
    except:
        # print("BEARER TOKEN IS INVALID")
        return -5
    
    if GetUserProfile(GetBearerToken(uplandID))['level'] == "Visitor":
        # print("VISITOR")
        return -6
   


    # FIX THIS: CHALLENGE PARAMETERS
    challenger = QueryForLichessID(uplandID)
    speed = speed  
    increment = increment
    rated = rated_
    variant = variant
    name = name 
    wager = int(wager_)


    # Challenge under terms is created
    thisGame = CreateOpenChallenge(challenger=challenger, speed=speed, increment=increment, variant=variant,
                                   rated=rated, name=name)
    
    # Join Escrow
    bearer = GetBearerToken(uplandID)
    eid, link = AppendChallenge(challenger, wager, thisGame)  # Challenge is appended to spreadsheet (database) + Escrow is created & appended + Escrow & Link are extracted

    JoinEscrow(bearer, eid, wager)

    # Returning Info
    return link    