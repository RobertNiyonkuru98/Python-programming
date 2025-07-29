from db import connection
from login_study import login
def dashboard():
    cursor = connection.cursor()
    with open("session.txt", "r") as file:
        username = file.read()
    print(f"========Welcome to the DASHBOARD========\n ")
