from Upland.edit_profile import AppendProfile
from Upland.fill_profile import FillProfile
from Upland.query_spreadsheet import QueryUplandIDRow
from Upland.get_user_profile import GetUserProfile
from Upland.get_user_balance import GetUserBalance
from Upland.edit_profile import ReplaceProfileSmall


def CreateProfile(access_token, user_id):
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
        ReplaceProfileSmall(uplandIdx, "BLANK")
    
    # ONE LICHESS ACCOUNT PER UPLAND USER...IF HE KEEPS CHANGING HIS ACCOUNT HE'LL BE REMOVED!
