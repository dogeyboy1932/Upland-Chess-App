Akhil - Rough Notes


TO RUN THIS:
 - "npm start" on FRONTEND DIRECTORY!


To do:
 - Test game_ended
 - Setup domain to keep it all running





 
URL TAKES ME TO A FRONTEND DOMAIN:
 - WHAT I SEE:
 - Challenges Tables [Link, UplandID, lichessID, wager amount, lichess rating]
 - Create Challenge Button -> When I click button, I need to enter wager amount
 - Box to enter lichessID (it verifies and saves to profile)
 - Reset Button -> Updates everything (database, accounts, etc)
 - Not signed in? get auth code button + enter lichess code
 - OPTIONAL: Cancel Button -> Cancel a challenge the user made...USER ONLY (param: userID, gameID) <- NEED TO IMPROVE BY ADDING A CANCEL BUTTON FOR EACH CHALLENGE BUT THAT'S FOR AN UPDATED VERSION

When joining app:
 - Player records are added to the profile database
 - Players are asked to enter their lichess ID
 - Each profile has an extra parameter (lichess ID)
 - Map -> lichess id = key | User Profile Struct = Value XXXXX
 - Query spreadsheet for lichessID or UplandID

Wager Money:
 - Create Challenge Button
 - Once button clicked (user enters how much money to wager)
 - Is money less than player balance? If so, you can submit wager.
 - Next screen to setup parameters of challenge and submit to create a challenge.
 - Only if game is started (challenge accepted), balance is immediately deducted and thrown into the escrow
 - ^^ Worst case if we can't set a trigger condition the moment a game starts,
   we'll just have to immediately create an escrow when a challenge is made and
   resolve it if the challenge isn't accepted in 24 hours or if user cancels it

 - Challenge is added to challenges databases (shown on frontend)
 - Click on a link in the database and you are taken to the game
 - User can cancel challenge with cancel button on his screen. Only visible to user. If cancelled. Taken off database

Create an open ended challenge (with wager money added to it)
 - Two players Join
 - Lichess IDs is recorded from game stream X
 - If game is full and active, it is removed from challenges databases X
 - When open ended challenge is created -> record the game ID
 - Extract whiteID & blackID from the game (using boardgame stream & the gameID) X
   ^ Might just have to extract once the game ends. USE EXPORT
 - After game ends, figure out whether black or white wins. If Black wins, send over black id to "distribute function" (this function would connect lichess ID to profile to upland ID)
 - Get Upland ID & send to escrow account


Escrow Account:
 - Inputs: Upland Id of winner & loser
 - 70% winner
 - 20% loser
 - 10% developers


 INSTALL BERSERK
 INSTALL OPENPYXL
 INSTALL PANDAS






Backup chess development links:
 - https://itsourcecode.com/free-projects/pygame/chess-game-in-python-with-source-code/#google_vignette
 - https://www.youtube.com/watch?v=OpL0Gcfn4B4
 -

FRONEND DEV LINKS:
- https://www.youtube.com/watch?v=p5AtOUyf250

`https://www.youtube.com/watch?v=7LNl2JlZKHA




Run the button_clicks python file
Run the frontend... npm start inside FRONTEND directory on cmd



// "start:ngrok": "ngrok http --domain=vocal-shepherd-select.ngrok-free.app 5000",

start:ngrok




ssh root@146.190.145.45
,u5v+bfBhGC!CPB




#IGNORE
const reportWebVitals = onPerfEntry => {
  if (onPerfEntry && onPerfEntry instanceof Function) {
    import('web-vitals').then(({ getCLS, getFID, getFCP, getLCP, getTTFB }) => {
      getCLS(onPerfEntry);
      getFID(onPerfEntry);
      getFCP(onPerfEntry);
      getLCP(onPerfEntry);
      getTTFB(onPerfEntry);
    });
  }
};

export default reportWebVitals;



// pip install -r requirements.txt

        "package": "pip install -r package-list.txt && start",


ngrok http --domain=vocal-shepherd-select.ngrok-free.app 5000


Problems w/ Chess App:
 - Rest APIs (Berserk, figuring out authentication, escrows, etc)
 - Flask (routing msgs to backend)
 - Python (libraries like openpyxl, pandas, http.client, making API calls)
 - React.js + a little CSS
 - Webhooks (forwarding, tunnels  <- This took too long)
 - Integration!!!
