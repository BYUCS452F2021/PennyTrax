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

    def clean_id(data, additional_fields=[]):
        """
        A helper function to convert the _id ObjectId field to a string called id.
        Can also do other fields (without renaming) if specified.
        """
        if type(data) is list:
            for d in data:
                # Switch _id to id
                d["id"] = str(d["_id"])
                del d["_id"]
                # If there are additional fields listed, do those as well
                if len(additional_fields):
                    for f in additional_fields:
                        d[f] = str(d[f])
        else:
            data["id"] = str(data["_id"])
            del data["_id"]
            # If there are additional fields listed, do those as well
            if len(additional_fields):
                for f in additional_fields:
                    data[f] = str(data[f])