from Upland.append_profile import AppendProfile
from Upland.fill_profile import FillProfile
from Upland.query_uplandID_index import QueryUplandIDRow
from Upland.get_user_profile import GetUserProfile
from Upland.get_user_balance import GetUserBalance
from Upland.replace_profile import ReplaceProfile


def CreateProfile(access_token, user_id):
    user_profile = GetUserProfile(access_token, user_id)
    balance = GetUserBalance(access_token)

    # uplandID = user_profile['id']
    uplandUsername = user_profile['username']
    bearer_token = access_token
    eosId = user_profile['eosId']

    PROFILE = ["BLANK_ID", uplandUsername, "BLANK_RATING", balance, bearer_token, eosId, "null"]

    # Verifies profile doesn't exist already to avoid duplicates
    if QueryUplandIDRow(uplandUsername) == -1:
        # Adds profile to Excel sheet
        AppendProfile(PROFILE)
    else:
        # If profile exists? It is replaced w/ updated info
        ReplaceProfile(uplandUsername, PROFILE)
    
    # Fills out the blanks in profile: [BLANK_ID; BLANK_RATING] or Updates Lichess Info
    FillProfile(uplandID=uplandUsername)

    # ONE LICHESS ACCOUNT PER UPLAND USER...IF HE KEEPS CHANGING HIS ACCOUNT HE'LL BE REMOVED!
