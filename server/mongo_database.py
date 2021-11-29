import os
from dotenv import load_dotenv
from pymongo import MongoClient


class MongoDatabase:
    def __init__(self):
        load_dotenv()
        mongoUser = os.getenv('MONGO_USER')
        mongoPass = os.getenv('MONGO_PASS')
        mongoHost = os.getenv('MONGO_HOST')
        mongoDatabase = os.getenv('MONGO_DATABASE')
        mongoPort = 27017
        self.client = MongoClient(host=mongoHost + ":" + str(mongoPort),
                                  username=mongoUser, password=mongoPass)

        self.db = self.client[mongoDatabase]

    def __del__(self):
        self.client.close()
