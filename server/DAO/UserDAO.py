mock_data = [
    {
        "id": 1,
        "firstName": "Brayden",
        "lastName": "Wood",
        "email": "braydenwood1@gmail.com",
        "password": "test123"
    },
    {
        "id": 2,
        "firstName": "Test",
        "lastName": "Testerson",
        "email": "testing@gmail.com",
        "password": "test123"
    },
    {
        "id": 3,
        "firstName": "Alice",
        "lastName": "Smith",
        "email": "alicesmith@gmail.com",
        "password": "test123"
    }
]


class UserDAO:
    def __init__(self):
        # Init DB connection
        pass

    def create_user(self, user_data):
        next_id = max([x["id"] for x in mock_data]) + 1
        print(next_id)
        user_data["id"] = next_id
        mock_data.append(user_data)

    def get_user(self, id):
        user = next((x for x in mock_data if x["id"] == id), None)
        return user

    def get_user_by_email(self, email):
        user = next((x for x in mock_data if x["email"] == email), None)
        return user

    def get_all_users(self):
        return mock_data

    def update_user(self, id, user_info):
        pass

    def delete_user(self, id):
        pass
