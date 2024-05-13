from Upland.get_user_profile import GetUserProfile
from Upland.SpreadsheetEditing.edit_profile import AppendProfile
from Upland.SpreadsheetEditing.query_spreadsheet import QueryUplandIDRow
from Upland.get_user_balance import GetUserBalance

def CreateProfile(bearer_token):   # Called when connecting to ChessApp on Upland
    user_profile = GetUserProfile(bearer_token)
    
    uplandUsername = user_profile['username']
    balance = GetUserBalance(bearer_token)
    eosId = user_profile['eosId']
    userId = user_profile['id']

    PROFILE = ["BLANK_ID", uplandUsername, "BLANK_RATING", balance, bearer_token, eosId, None, userId]


    uplandIdx = QueryUplandIDRow(uplandUsername)

    # Verifies profile doesn't exist already to avoid duplicates
    if uplandIdx == -1:
        # Adds profile to Excel sheet
        AppendProfile(PROFILE)
    
    
    # ONE LICHESS ACCOUNT PER UPLAND USER...IF HE KEEPS CHANGING HIS ACCOUNT HE'LL BE REMOVED!
