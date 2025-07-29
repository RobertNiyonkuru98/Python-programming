import mysql.connector
try:
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "practice"
    )
except mysql.connector.Error:
    print("database failed to connector")