import mysql.connector


database_name = "bank_db"


con = mysql.connector.connect(
    host="localhost",
    username="root",
    password="MyNewPass",
    database=database_name
)

cur = con.cursor()
