from Upland.get_user_profile import GetUserProfile
from Upland.SpreadsheetEditing.edit_profile import AppendProfile, ReplaceProfileSmall
from Upland.SpreadsheetEditing.query_spreadsheet import QueryUplandIDRow
from Upland.SpreadsheetEditing.get_user_balance import GetUserBalance

def CreateProfile(access_token):
    user_profile = GetUserProfile(access_token)
    balance = GetUserBalance(access_token)

    uplandUsername = user_profile['username']
    bearer_token = access_token
    eosId = user_profile['eosId']

    PROFILE = ["BLANK_ID", uplandUsername, "BLANK_RATING", balance, bearer_token, eosId, "null"]

    uplandIdx = QueryUplandIDRow(uplandUsername)

    # Verifies profile doesn't exist already to avoid duplicates
    if uplandIdx == -1:
        # Adds profile to Excel sheet
        AppendProfile(PROFILE)
    else:
        # If profile exists? It is replaced w/ updated lichessID
        ReplaceProfileSmall(uplandIdx, "BLANK_ID", bearer_token)
    
    # ONE LICHESS ACCOUNT PER UPLAND USER...IF HE KEEPS CHANGING HIS ACCOUNT HE'LL BE REMOVED!
