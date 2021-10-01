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


def create_user(user_data):
    next_id = max([x["id"] for x in mock_data]) + 1
    print(next_id)
    user_data["id"] = next_id
    mock_data.append(user_data)


def read_user(user_id):
    user = next((x for x in mock_data if x["id"] == user_id), None)
    return user


def update_user(user_id, user_info):
    pass


def delete_user(user_id):
    pass
