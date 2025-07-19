# STUDENT INFO
class Student:
    def __init__(self):
        self.name = ""
        self.classroom = ""
        self.cohort = ""
        self.intake = ""

    def get_name(self):
        while True:
            name = input("Enter your Name: ")
            if name == "":
                print("Input cannot be empty")
            elif not name.replace(" ", "").isalpha():
                print("Input must contain letters")
            else:
                self.name = name.capitalize()
                break

    def get_classroom(self):
        while True:
            classroom = input("Enter your Class: ")
            if classroom == "":
                print("Input cannot be empty")
            elif not any(c.isalpha() for c in classroom.capitalize()):
                print("Input must contain letters")
            else:
                self.classroom = classroom.capitalize()
                break

    def get_cohort(self):
        while True:
            cohort = input("Enter your Cohort: ")
            if cohort == "":
                print("Input cannot be empty")
            elif not any(c.isalpha() for c in cohort):
                print("Input must contain letters")
            else:
                self.cohort = cohort.capitalize()
                break

    def get_intake(self):
        while True:
            intake = input("Enter your Intake: ")
            if intake == "":
                print("Input cannot be empty")
            elif not any(i.isalpha() for i in intake):
                print("Input must contain letters")
            else:
                self.intake = intake.capitalize()
                break
    def collect_info(self):
        self.get_name()
        self.get_classroom()
        self.get_cohort()
        self.get_intake()



class Report(Student):
    def __init__(self):
        super().__init__()
        self.assignment = ""
        self.category = ""
        self.weight = 0
        self.grade = 0

    def get_assignment(self):
        while True:
            assignment = input("Enter the Assignment: ")
            if assignment == "":
                print("You did not enter an assignment \nplease correct that")
            else:
                self.assignment = assignment
                break
# Asking the user to Enter the Assignment Category
    def get_category(self):
        while True:
            category = input("Enter the Assignment name: ").strip()
            if category == "":
                print(f"Your Assignment category is empty")
            elif category.lower() not in ["formative", "summative"]:
                print(f"Your Entered Assignment category not valid")
            else:
                self.category = category.capitalize()
                break
# Asking the user to Enter the weight of the assignment

    def get_weight(self):
        while True:
            try:
                weight = int(input("Enter the weight (% of total grade for this assignment): "))
                if weight == "":
                    print("You did not enter the total grade for this \nassignment")
                elif weight <= 0 or weight > 100:
                    print("The weight you entered is invalid")
                else:
                    self.weight = weight
                    break
            except ValueError:
                print("The weight you entered is not numerical")


# Asking the user to Enter his/her obtained grade
    def get_grade(self):
        while True:
            try:
                grade = int(input("Enter the grade obtained (0-100%): "))
                if grade == "":
                    print("You did not enter the grade you obtained")
                elif grade < 0 or grade > 100:
                    print("Your grade must be between 0 and 100")
                else:
                    self.grade = grade
                    break
            except ValueError:
                print("Grade must be a numerical value")
    def calculate_weighted_grade(self):
        return (self.grade / 100) * self.weight

    def display_report(self):
        print("\n --- STUDENT INFORMATION ---")
        print(f"Welcome {self.name}")
        print(f"Classroom: {self.classroom}")
        print(f"Cohort: {self.cohort}")
        print(f"Intake: {self.intake}")
        print("\n--- ASSIGNMENT REPORT ---")
        print(f"Assignment: {self.assignment}")
        print(f"Category: {self.category}")
        print(f"Grade: {self.grade}%")
        print(f"Weight: {self.weight}%")
        print(f"Weighted Contribution to Final Grade: {self.calculate_weighted_grade():.2f}%")

student_report = Report()
student_report.collect_info()
student_report.get_assignment()
student_report.get_category()
student_report.get_weight()
student_report.get_grade()
student_report.display_report()