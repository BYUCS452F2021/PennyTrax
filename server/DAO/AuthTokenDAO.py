import uuid
import datetime

mock_data = [
    {
        "auth_token": "1",
        "user_id": 1,
        "expiration_date": "2021-12-01T00:00:00"
    },
    {
        "auth_token": "2",
        "user_id": 2,
        "expiration_date": "2021-12-01T00:00:00"
    },
    {
        "auth_token": "3",
        "user_id": 3,
        "expiration_date": "2021-12-01T00:00:00"
    }
]

AUTH_TOKEN_DURATION = 1  # in hours


class AuthTokenDAO:
    def __init__(self):
        # Init DB connection
        pass

    def create_auth_token(self, user_id):
        new_auth_token = uuid.uuid4()
        mock_data.append({
            "auth_token": new_auth_token,
            "user_id": user_id,
            "expiration_date": datetime.datetime.today() + datetime.timedelta(hours=AUTH_TOKEN_DURATION)
        })
        return new_auth_token

    def verify_auth_token(self, user_id, auth_token):
        # if auth token in auth token table and not expired, update auth_token expiration and return true
        # if expired, delete auth_token from table
        # else return false
        pass

    def get_auth_tokens(self):
        return mock_data

    def delete_auth_token(self, auth_token):
        pass
