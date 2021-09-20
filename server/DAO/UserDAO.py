def create_user(user_info):
    pass


def read_user(user_id):
    mock_data = {
        1: {
            "firstName": "Brayden",
            "lastName": "Wood",
            "email": "braydenwood1@gmail.com",
            "password": "test123"
        },
        2: {
            "firstName": "Test",
            "lastName": "Testerson",
            "email": "testing@gmail.com",
            "password": "test123"
        },
        3: {
            "firstName": "Alice",
            "lastName": "Smith",
            "email": "alicesmith@gmail.com",
            "password": "test123"
        }
    }

    return mock_data[user_id]


def update_user(user_id, user_info):
    pass


def delete_user(user_id):
    pass
