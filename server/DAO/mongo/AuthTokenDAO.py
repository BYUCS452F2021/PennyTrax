import uuid
import datetime
import json
from mongo_database import MongoDatabase
from bson.objectid import ObjectId

AUTH_TOKEN_DURATION = 1  # in hours

class AuthTokenDAO:
    def __init__(self):
        self.db = MongoDatabase().db

    def create_auth_token(self, user_id):
        new_auth_token = str(uuid.uuid4())
        expiration_date = datetime.datetime.now(
        ) + datetime.timedelta(hours=AUTH_TOKEN_DURATION)
        data = {'auth_token' : new_auth_token, 'user_id' : user_id, 'expiration_date': expiration_date}
        json_data = json.dumps(data)
        result = self.db.AuthToken.insert_one(json_data)
        return str(result.inserted_id)

    def verify_auth_token(self, auth_token_str):
        result = self.db.AuthToken.find_one({'auth_token': auth_token_str})
        if result:
            result["id"] = str(result["_id"])
            del result["_id"]
            return result
        else:
            return None

    def get_auth_tokens(self):
        pass

    def delete_auth_token(self, auth_token):
        pass
    