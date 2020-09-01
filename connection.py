import mysql.connector


# database_name = "bank_db"
database_name = "hsachan_bank_db"


# con = mysql.connector.connect(
#     host="localhost",
#     username="local",
#     password="MydB@125#",
#     database=database_name
# )

con = mysql.connector.connect(
    host="johnny.heliohost.org",
    username="hsachan_local",
    password="MydB@125#",
    database=database_name
)

cur = con.cursor()
