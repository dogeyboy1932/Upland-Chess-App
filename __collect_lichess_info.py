# FRONTEND DEPENDENT
from Upland.FIXED_VARIABLES import filepath
from openpyxl import load_workbook
from Upland.query_spreadsheet import QueryUplandIDRow

def GetLichessID():
    #####################
    # INSTRUCTIONS
    # User would give in details to pop up when asking for lichess information
    # lichessID = {POPUP_ANSWER} Lookup account... if no response return not valid
    # We need to verify these accounts exist: verify_lichessID(lid) && verify_uplandID(id)
    # Write function for this that collects the details and verifies

    lichessID = "trashboatsr"  # <- Placeholder
    # lichessID = "RichDogeyBoy"  # <- Placeholder
    #####################

    print(lichessID)

    ## Call FillProfile everytime you need to update rating...user needs to (sign in) again

    return lichessID
