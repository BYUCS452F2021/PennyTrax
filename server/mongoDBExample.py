import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
mongoUser = os.getenv('MONGO_USER')
mongoPass = os.getenv('MONGO_PASS')
mongoHost = os.getenv('MONGO_HOST')
mongoDatabase = os.getenv('MONGO_DATABASE')
mongoPort = 27017
client = MongoClient(host=mongoHost + ":" + str(mongoPort),
                     username=mongoUser, password=mongoPass)

db = client[mongoDatabase]
usersTable = db.user

for user in usersTable.find():
    print(user)

client.close()
print("Done")
