from db import connection
import bcrypt
import getpass
def login():
    cursor = connection.cursor()
    choice = input("Are you a Teacher, Student or Parent \n(Choose one role): ").lower().strip()
    if choice == "student":
        email = input("Enter your email: ")
        password = getpass.getpass("Enter your password: ").encode("utf-8")
        query = "SELECT * FROM student WHERE email = %s"
        values = (email,)
        cursor.execute(query, values)
        user = cursor.fetchone()
        if user:
            userhashed = user[3].encode("utf-8")
            if bcrypt.checkpw(password, userhashed):
                with open("session.txt", "w") as file:
                    file.write(f"Student id: {user[0]}")
                    from dashboard import dashboard
            else:
                print("Password is incorrect")
    elif choice == "teacher":
        email = input("Enter your email: ")
        password = input("Enter your password: ").encode("utf-8")
        query = "SELECT * FROM instructors WHERE email = %s"
        values = (email,)
        cursor.execute(query, values)
        user = cursor.fetchone()
        if user:
            userhashed = user[3].encode("utf-8")
            if bcrypt.checkpw(password, userhashed):
                with open("session.txt", "w") as file:
                    file.write(f"Teacher id: {user[0]}")
                    from dashboard import dashboard
            else:
                print("Password is incorrect")
    elif choice == "parent":
        email = input("Enter your email: ")
        password = input("Enter your password: ").encode("utf-8")
        query = "SELECT * FROM parents WHERE email = %s"
        values = (email,)
        cursor.execute(query, values)
        user = cursor.fetchone()
        if user:
            userhashed = user[3].encode("utf-8")
            if bcrypt.checkpw(password, userhashed):
                with open("session.txt", "w") as file:
                    file.write(f"Parent id: {user[0]}")
                    from dashboard import dashboard
                    dashboard()
            else:
                print("Password is incorrect")
        else:
            print("No user found with this email")
        cursor.close()
login()
