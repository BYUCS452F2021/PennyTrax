import uuid
import datetime
from database import Database

AUTH_TOKEN_DURATION = 1  # in hours


class AuthTokenDAO:
    def __init__(self):
        self.db = Database()

    def create_auth_token(self, user_id):
        new_auth_token = str(uuid.uuid4())
        expiration_date = datetime.datetime.now(
        ) + datetime.timedelta(hours=AUTH_TOKEN_DURATION)
        cursor = self.db.connection.cursor()
        sql = (
            "INSERT INTO AuthToken (auth_token, user_id, expiration_date) VALUES (%s, %s, %s)")
        values = (new_auth_token, user_id, expiration_date)
        cursor.execute(sql, values)
        self.db.connection.commit()
        cursor.close()
        return new_auth_token

    def verify_auth_token(self, user_id, auth_token):
        # if auth token in auth token table and not expired, update auth_token expiration and return true
        # if expired, delete auth_token from table
        # else return false
        pass

    def get_auth_tokens(self):
        pass

    def delete_auth_token(self, auth_token):
        pass
