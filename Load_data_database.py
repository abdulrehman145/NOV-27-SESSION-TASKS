import mysql.connector
from mysql.connector import error

try:
    connection=mysql.connector.connect(
        host="local_host",
        database="database_name",
        user="user_name",
        password="password"
    )
    if connection.is_connected():
        print("connected to database, successfully")
        cursor=connection.cursor()
        result=cursor.execute("SQL command")
        print(result)
except error as e:
    print("error! while fetching database")
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("database connection is closed.")
