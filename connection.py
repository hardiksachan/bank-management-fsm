import mysql.connector


database_name = "bank_db"


con = mysql.connector.connect(
    host="localhost",
    username="local",
    password="MydB@125#",
    database=database_name
)

cur = con.cursor()
