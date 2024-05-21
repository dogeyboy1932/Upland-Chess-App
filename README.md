**OFFICIAL WEBSITE:**
https://upland-chess.website/

# Function:
Users create a new profile connecting their Upland & Lichess accounts to it.

Afterwards, they can: 
 - create chess challenges and wager an amount of their choice
 - accept chess challenges that others submitted

# How To Use:
On branch *Main*, enter *Frontend* directory on your shell & type in "npm start"

** If you run into an error like "error:0308010C:digital envelope routines::unsupported", enter the following cmd into your shell and try again: `set NODE_OPTIONS=--openssl-legacy-provider` **

# More Info
## **Branches:**
 - Main: For local testing & development
 - Frontend: All code for frontend -> Deployed on Vercel   [Built w/ Node.js & React]
 - Backend: All code for backend -> Deployed on Heroku     [Built w/ Flask & Python]
 - Akhil: Test branch

## **Packages:**
 - pandas
 - Flask
 - openpyxl
 - berserk
 - Flask_cors
 - node.js ("npm i" in *Frontend* directory)


*This app is reliant on the functionality of the Upland & Lichess APIs. (For the most part, it works fine.)*


## **How Escrow Funds are Resolved:**
 - 80% winner
 - 10% loser
 - 10% developers


[***ngrok***]

For local testing I used ngrok to receive webhook requests: 
- [ngrok http --domain=vocal-shepherd-select.ngrok-free.app 5000]     <- When connecting to app on Upland, this webhook forwards the request to localhost:5000


## **First Problems/Tasks when Building App**

### Had to learn:
 - Rest APIs (Berserk, figuring out authentication, escrows, etc)
 - Flask (routing msgs to backend)
 - Python (libraries like openpyxl, pandas, http.client, making API calls)
 - React.js + a little CSS
 - Webhooks (forwarding, tunnels  <- This took too long)
 - Integration!!!
 - Heroku
 - Vercel
 - CSS, HTML, JS Libraries
 - A bunch of _stuff_ along the way


# Things to work on:
- RESET PASSWORD OPTION
- Using local storage to shift between pages
- Create spinning icon that will momentarily show on the site when reset button is clicked
- Make the reset button a component of its own
- "Improve UI"
