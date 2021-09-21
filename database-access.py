import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

mydb = mysql.connector.connect(
  host = os.getenv('MYSQL_HOST'),
  user = os.getenv('MYSQL_USER'),
  password = os.getenv('MYSQL_PASS'),
  database = os.getenv('MYSQL_DATABASE'),
  auth_plugin = 'mysql_native_password'
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Users")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)