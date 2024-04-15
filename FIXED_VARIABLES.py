import http.client
import base64
import berserk

import logging
from json import JSONEncoder
import numpy


# MY EOS BLOCKCHAIN ID
primeEOS = "mp4n4f2mq3ca"


# Upland API Client
conn = http.client.HTTPSConnection("api.sandbox.upland.me")

appID = "232"
accessKey = "ad331091-4762-4fe1-b40f-1d4ca0d02d9f"
credential = base64.b64encode(f'{appID}:{accessKey}'.encode('utf-8')).decode('utf-8')


# Lichess API Client
token = "lip_ZnYbIrvWC5KDwB8P0wJu"
session = berserk.TokenSession(token)
client = berserk.Client(session=session)


# Spreadsheet Paths
filepath = r"/Users/gogin/Desktop/ChessApp/ChessApp VS Code/XL Spreadsheets/ProfileDatabase.xlsx"
cfilepath = r"/Users/gogin/Desktop/ChessApp/ChessApp VS Code/XL Spreadsheets/ChallengeMap.xlsx"


# Smoothing Methods
logger = logging.getLogger('werkzeug')
logger.addHandler(logging.NullHandler())

class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)

# pd.set_option('display.max_colwidth', None)
