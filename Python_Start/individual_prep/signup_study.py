import bcrypt
import getpass
import sys
from db import connection
def signup():
    cursor = connection.cursor()
    choice = input("Are you a Teacher, Student or Parent \n(Choose one role): ").lower().strip()
    if choice == "Student":
        username = input("Enter your Full Name: ")
        email = input("Enter your Email: ")
        password = getpass.getpass("Enter your Password: ").encode("utf-8")
        confirm = getpass.getpass("Confirm your password: ").encode("utf-8")
        if password != confirm:
            print("Passwords do not match. Try again.")
            return
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        classroom = input("Enter your classroom\n(E.g: Primary 6/Senior 3/Senior 6...: ): ")
        query = "INSERT INTO student (name, email, password, classroom) VALUES (%s, %s, %s, %s)"
        values = (username, email, hashed, classroom)
        cursor.execute(query, values)
        connection.commit()
        cursor.close()
    elif choice == "Teacher":
        username = input("Enter your Full Name: ")
        email = input("Enter your Email: ")
        password = input("Enter your Password: ").encode("utf-8")
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        subject = input("Enter your subject speciality \n(E.g: Science/Python Programming/BEL...): ")
        query = "INSERT INTO instructors (name, email, password, subject) VALUES (%s,%s,%s,%s)"
        values = (username, email, hashed, subject)
        cursor.execute(query, values)
        connection.commit()
        cursor.close()
    elif choice == "Parent":
        username = input("Enter your Full Name: ")
        email = input("Enter your Email: ")
        password = input("Enter your Password: ").encode("utf-8")
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        phone_number = input("Enter your phone number: ")
        query = "INSERT INTO parents (name, email, password, phone_number) VALUES (%s,%s,%s,%s)"
        values = (username, email, hashed, phone_number)
        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        choose = input("Do you want to proceed to log in? yes/no: ").lower().strip()

        if choose == 'yes':
            from login import login
        else:
            sys.exit()
    else:
        print(f"{choice} is not among the list \n Your should be either a Student, Teacher or Parent")
signup()
