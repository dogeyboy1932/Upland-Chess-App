# from flask import Flask, request, jsonify
# import json
# from Chess.FIXED_CHESS_VARIABLES import NumpyArrayEncoder
# from Chess.render_database import Iterate
# from Chess.handle_finished_games import HandleFinishedGames


# app = Flask(__name__)
# app.logger.disabled = True

# @app.route('/test', methods=['POST'])
# def ChallengeButtonClicked():
#     return "Success"  # UPDATE THIS

# @app.route('/database', methods=['POST'])
# def ChallengeDatabase():
#     HandleFinishedGames()
#     arr = Iterate()

#     encodedNumpyData = json.dumps({"array": arr}, cls=NumpyArrayEncoder)

#     return encodedNumpyData

# if __name__ == '__main__':
#     app.run(debug=True)





# Frontend Dependent

# ALL CONTACT BETWEEN FRONTEND AND BACKEND HAPPENS HERE

# THIS PIECES TOGETHER THE FRONTEND AND BACKEND


# challenge button clicked -> challengeButtonClicked(WITH PARAMETERS)
# reset button clicked -> resetButtonClicked

# from flask import Flask

# app = Flask(__name__)

# Members API Route
# @app.route("/test")
# def members():
#     return {"members": ["Member1", "Member2", "Member3"]}


# @app.route("/test2")
# def members2():
#     return {"hi": "Hi"}


# if __name__ == "__main__":
#     app.run(debug=True)
    

    # @app.route('/test2', methods=['POST'])
# def ResetButtonClicked():
    
#     print("Reset Button Clicked")
#     return "Success"
    

    

    # for row in arr:
    #     # ind = char(index)
    #     print(row[0], row[1], row[2], row[3])
    #     # res.append[{row[0], row[1], row[2], row[3]}]
