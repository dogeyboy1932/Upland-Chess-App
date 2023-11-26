from Upland.append_profile import AppendProfile
from fill_profile import FillProfile
from query_uplandID_index import QueryUplandIDRow
from get_user_profile import GetUserProfile
from get_user_balance import GetUserBalance


def CreateProfile(access_token, user_id):
    user_profile = GetUserProfile(access_token, user_id)
    balance = GetUserBalance(access_token, user_id)

    # uplandID = user_profile['id']
    uplandUsername = user_profile['username']
    bearer_token = access_token
    eosId = user_profile['eosId']

    PROFILE = ["BLANK_ID", uplandUsername, "BLANK_RATING", balance, bearer_token, eosId]

    # Verifies profile doesn't exist already to avoid duplicates
    if QueryUplandIDRow(uplandUsername) == -1:
        # Adds profile to Excel sheet
        AppendProfile(PROFILE)

    # Fills out the blanks in profile: [BLANK_ID; BLANK_RATING] or Updates Lichess Info
    # ONE LICHESS ACCOUNT PER UPLAND USER...IF HE KEEPS CHANGING HIS ACCOUNT HE'LL BE REMOVED!
    FillProfile(uplandID=uplandUsername)




# from get_user_balance import get_user_balance
# from Profile import Profile
# from get_lichessID import getLichessID
# from getLichessRating import getLichessRating

# def Create_Verify_Append
#
#     CreateBaseProfile(user_prof)
#     DoesProfileExist(user_prof)

# getLichessRating(lichessID, "rapid")
# LICHESS_MAPPER[lichessID] = Profile(lichessID, rating, user_prof['id'])
# filepath = r"/Users/gogin/Desktop/Metaverse/ChessApp Pycharm Code/ChessDatabase1.xlsx"

# print("User Profile: ", user_prof)
# print(get_user_balance(access_token, user_id))

# print("here")
# print(LICHESS_MAPPER[lichessID].rating)
# print("here2")


#getLichessID()

# print("CreateProfile Called")

    # found = )
    #
    # print("FOUND ", found)