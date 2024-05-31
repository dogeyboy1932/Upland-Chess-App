from FIXED_VARIABLES import profiles_db

from Upland.get_user_profile import GetUserProfile
from Upland.get_user_balance import GetUserBalance

def CreateProfile(bearer_token):   # Called when connecting to ChessApp on Upland
    user_profile = GetUserProfile(bearer_token)
    balance = GetUserBalance(bearer_token)

    print("CREATE BALANCE: ", balance)

    uplandUsername = user_profile['username']
    eosId = user_profile['eosId']
    userId = user_profile['id']
    
    PROFILE = {
        "Lichess ID": "BLANK_ID",
        "Upland Username": uplandUsername,
        "Lichess Rating": "BLANK_RATING",
        "Balance": balance,
        "Bearer Token": bearer_token,
        "Eos Upland ID": eosId,
        "Password": None,
        "UserId": userId,
        "LichessReplaced": 0
    }

    profiles_db.insert_one(PROFILE)    
    
    
    # ONE LICHESS ACCOUNT PER UPLAND USER...IF HE KEEPS CHANGING HIS ACCOUNT HE'LL BE REMOVED!
