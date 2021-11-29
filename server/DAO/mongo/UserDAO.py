from mongo_database import MongoDatabase
from bson.objectid import ObjectId


class UserDAO:
    def __init__(self):
        self.db = MongoDatabase().db

    def create_user(self, user_data):
        result = self.db.user.insert_one(user_data)
        return str(result.inserted_id)

    def get_user(self, id):
        obj_id = ObjectId(id)
        result = self.db.user.find_one({'_id': obj_id})
        if result:
            result["id"] = str(result["_id"])
            del result["_id"]
            return result
        else:
            return None

    def get_user_by_email(self, email):
        result = self.db.user.find_one({'email': email})
        if result:
            result["id"] = str(result["_id"])
            del result["_id"]
            return result
        else:
            return None

    def get_all_users(self):
        users = []
        for user in self.db.user.find():
            user["id"] = str(user["_id"])
            del user["_id"]
            users.append(user)
        return users

    def update_user(self, id, user_info):
        pass

    def delete_user(self, id):
        pass
