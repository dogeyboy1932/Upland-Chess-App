import http.client
import base64
import berserk

import logging
# from json import JSONEncoder
# import numpy

from pymongo import MongoClient

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


# Smoothing Methods
logger = logging.getLogger('werkzeug')
logger.addHandler(logging.NullHandler())

# class NumpyArrayEncoder(JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, numpy.ndarray):
#             return obj.tolist()
#         return JSONEncoder.default(self, obj)

# pd.set_option('display.max_colwidth', None)




# Create the connection string
connection_string = 'mongodb+srv://vagogineni:KingBlackMask25@cluster0.rfvxrov.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'

# Connect to the MongoDB server
mongoClient = MongoClient(connection_string)

challenges_db = mongoClient['Upland_Chess_App']['Challenges']
profiles_db = mongoClient['Upland_Chess_App']['Profiles']
test_db = mongoClient['Upland_Chess_App']['Test']