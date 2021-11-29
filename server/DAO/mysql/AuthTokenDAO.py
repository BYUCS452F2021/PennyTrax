import uuid
import datetime
from mysql_database import MysqlDatabase

AUTH_TOKEN_DURATION = 1  # in hours


class AuthTokenDAO:
    def __init__(self):
        self.db = MysqlDatabase()

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

    def verify_auth_token(self, auth_token_str):
        cursor = self.db.connection.cursor()
        sql = "SELECT * FROM AuthToken WHERE auth_token = %(auth_token)s"
        cursor.execute(sql, {"auth_token": auth_token_str})
        result = cursor.fetchall()
        cursor.close()

        if len(result) >= 1:
            row = result[0]
            auth_token = {
                "auth_token": row[0],
                "user_id": row[1],
                "expiration_date": row[2]
            }
            expiration_date = datetime.datetime.strptime(
                str(auth_token["expiration_date"]), '%Y-%m-%d %H:%M:%S')
            if expiration_date < datetime.datetime.now():
                self.delete_auth_token(auth_token_str)
                return None

            return auth_token["user_id"]

        else:
            return None

        # if auth token in auth token table and not expired, update auth_token expiration and return true
        # if expired, delete auth_token from table
        # else return false
        pass

    def get_auth_tokens(self):
        pass

    def delete_auth_token(self, auth_token):
        pass
