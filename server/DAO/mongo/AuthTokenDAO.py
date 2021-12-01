from mongo_database import MongoDatabase
from bson.objectid import ObjectId

class AuthTokenDAO:
    def __init__(self):
        self.db = MongoDatabase().db

    def create_auth_token(self, user_id):
        result = self.db.authToken.insert_one(user_id)
        return str(result.inserted_id)

    def verify_auth_token(self, auth_token_str):
        result = self.db.authToken.find_one({'auth_token': auth_token_str})
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
    