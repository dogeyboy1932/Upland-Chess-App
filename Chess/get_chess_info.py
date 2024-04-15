from FIXED_VARIABLES import client


def getAccount(userID):
    return client.users.get_by_id(userID)


def GetLichessRating(lichessID, variant):
    accountInfo = getAccount(lichessID)

    if accountInfo == []: 
        # print("ACCOUNT DOES NOT EXIST")
        return -1

    rating = accountInfo[0]['perfs'][variant]['rating']

    return rating
