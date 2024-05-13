from FIXED_VARIABLES import client

def GameWinner(gameID):
    thisGame = client.games.export(gameID)
    winner = thisGame.get('winner')
    
    try: whiteId = thisGame.get('players').get('white').get('user').get('name')
    except: 
        whiteId = "blankw"
        print("GAME WINNER ERROR WHITE")
    
    try: blackId = thisGame.get('players').get('black').get('user').get('name')
    except: 
        blackId = "blankb"
        print("GAME WINNER ERROR BLACK")


    if thisGame.get('status') == 'draw':
        return [whiteId, blackId, "DRAW"]

    if winner == 'white':
        return [whiteId, blackId, "NO DRAW"]
    
    if winner == 'black':
        return [blackId, whiteId, "NO DRAW"]
        
