from openpyxl import load_workbook

from Chess.FIXED_CHESS_VARIABLES import cfilepath
from Chess.query_for_uplandID import QueryForUplandID

from Upland.join_escrow_container import JoinEscrow
from Upland.get_bearer_token import GetBearerToken


def ChallengeAccepted(link, challenger, accepter):  # <- Accept Button clicked
    workbook = load_workbook(cfilepath)
    worksheet = workbook['Sheet']
    
    for i in range(1, worksheet.max_row + 1):
        if worksheet[i][4].value == link:
            worksheet[i][6].value = True
            worksheet[i][7].value = accepter

            challengeIdx = i

    workbook.save(cfilepath)
    workbook.close()

    creator = QueryForUplandID(worksheet[challengeIdx][1].value)
    
    # if (creator == challenger):
    #     return -1 # You can't accept your own challenge!

    bearer = GetBearerToken(challenger)
    eid = worksheet[challengeIdx][5].value
    wager = worksheet[challengeIdx][3].value
    
    JoinEscrow(bearer, eid, wager)

    # print(bearer, " ", eid, " ", wager)