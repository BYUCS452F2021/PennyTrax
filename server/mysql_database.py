import os
from dotenv import load_dotenv
import mysql.connector


class MysqlDatabase:
    def __init__(self):
        load_dotenv()
        self.connection = mysql.connector.connect(
            host=os.getenv('MYSQL_HOST'),
            user=os.getenv('MYSQL_USER'),
            password=os.getenv('MYSQL_PASS'),
            database=os.getenv('MYSQL_DATABASE'),
            auth_plugin='mysql_native_password'
        )
