import berserk
import base64
import logging
from json import JSONEncoder
import numpy

token = "lip_ZnYbIrvWC5KDwB8P0wJu"

session = berserk.TokenSession(token)
client = berserk.Client(session=session)

appID = "232"
accessKey = "ad331091-4762-4fe1-b40f-1d4ca0d02d9f"
credential = base64.b64encode(f'{appID}:{accessKey}'.encode('utf-8')).decode('utf-8')


# cfilepath = "/root/ChessApp/XL Spreadsheets/ChallengeMap.xlsx"
cfilepath = r"/Users/gogin/Desktop/ChessApp/ChessApp VS Code/XL Spreadsheets/ChallengeMap.xlsx"


logger = logging.getLogger('werkzeug')
logger.addHandler(logging.NullHandler())

class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)