from FIXED_VARIABLES import client


def GetAccount(userID):
    return client.users.get_by_id(userID)


def GetVariant(userID, variant):
    accountInfo = GetAccount(userID)

    try:
        variant = accountInfo[0]['perfs'][variant]
        return variant
    except:
        return -1   # Account doesn't exist
        

def GetLichessRating(lichessID, variant):
    accountInfo = GetAccount(lichessID)

    try:
        rating = accountInfo[0]['perfs'][variant]['rating']
        return rating
    except:
        return -1   # Account doesn't exist

