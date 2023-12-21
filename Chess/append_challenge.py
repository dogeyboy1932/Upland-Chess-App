from openpyxl import load_workbook
from Chess.FIXED_CHESS_VARIABLES import cfilepath
from Chess.get_chess_rating import GetLichessRating
from Upland.create_escrow_container import CreateEscrowContainer


def AppendChallenge(challenger, wager, thisGame):
    workbook = load_workbook(cfilepath)
    worksheet = workbook['Sheet']

    # Grabbing Details
    gameID = thisGame['challenge']['id']
    rating = GetLichessRating(challenger, "rapid")
    link = thisGame['challenge']['url']
    escrowID = CreateEscrowContainer()

    # Making data
    data = [gameID, challenger, rating, wager, link, escrowID]

    # Appending data to spreadsheet
    worksheet.append(data)

    workbook.save(cfilepath)
    workbook.close()

    return gameID

def AppendInitial():
    workbook = load_workbook(cfilepath)
    worksheet = workbook['Sheet']

    data = ["gameID", "challenger", "rating", "wager", "link", "escrowID"]

    worksheet.append(data)

    workbook.save(cfilepath)
    workbook.close()
