from database import Database


class UserDAO:
    def __init__(self):
        self.db = Database()

    def create_user(self, user_data):

        cursor = self.db.connection.cursor()
        sql = (
            "INSERT INTO User (first_name, last_name, email, password, salt) VALUES (%s, %s, %s, %s, %s)")
        values = (user_data["first_name"],
                  user_data["last_name"],
                  user_data["email"],
                  user_data["password"],
                  user_data["salt"])
        cursor.execute(sql, values)
        self.db.connection.commit()
        cursor.close()

    def get_user(self, id):
        cursor = self.db.connection.cursor()
        sql = "SELECT * FROM User WHERE id = %(id)s"
        cursor.execute(sql, {"id": id})
        result = cursor.fetchall()
        cursor.close()

        if len(result) == 1:
            row = result[0]
            user = {
                "id": row[0],
                "first_name": row[1],
                "last_name": row[2],
                "email": row[3],
                "password": row[4],
                "salt": row[5]
            }
            return user
        else:
            return None

    def get_user_by_email(self, email):
        cursor = self.db.connection.cursor()
        sql = "SELECT * FROM User WHERE email = %(email)s"
        cursor.execute(sql, {"email": email})
        result = cursor.fetchall()
        cursor.close()

        if len(result) == 1:
            userData = result[0]
            user = {}
            user["id"] = userData[0]
            user["first_name"] = userData[1]
            user["last_name"] = userData[2]
            user["email"] = userData[3]
            user["password"] = userData[4]
            user["salt"] = userData[5]
            return user
        else:
            return None

    def get_all_users(self):
        cursor = self.db.connection.cursor()
        sql = "SELECT * FROM User"
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()

        return result

    def update_user(self, id, user_info):
        pass

    def delete_user(self, id):
        pass
