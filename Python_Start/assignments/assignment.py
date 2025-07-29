class Student:
    def __init__(self):
        self.name = ""
        self.classroom = ""
        self.cohort = ""
        self.intake = ""

    def get_name(self):
        print("👋🏿👋🏿👋🏿👋🏿👋🏿👋🏿👋🏿👋🏿👋🏿👋🏿👋🏿👋🏿👋🏿")
        print("SALUTATIONS")
        print("========================")
        print("WELCOME😁")
        print("========================")
        while True:
            name = input("Enter your Name: ")
            if not name.strip():
                print("Input cannot be empty")
            elif not name.replace(" ", "").isalpha():
                print("Input must contain letters")
            else:
                self.name = name.capitalize()
                break

    def get_classroom(self):
        while True:
            classroom = input("Enter your Class: ")
            if not classroom.strip():
                print("Input cannot be empty")
            elif not any(c.isalpha() for c in classroom):
                print("Input must contain letters")
            else:
                self.classroom = classroom.capitalize()
                break

    def get_cohort(self):
        while True:
            cohort = input("Enter your Cohort: ")
            if not cohort.strip():
                print("Input cannot be empty")
            elif not any(c.isalpha() for c in cohort):
                print("Input must contain letters")
            else:
                self.cohort = cohort.capitalize()
                break

    def get_intake(self):
        while True:
            intake = input("Enter your Intake: ")
            if not intake.strip():
                print("Input cannot be empty")
            elif not any(c.isalpha() for c in intake):
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
    FORMATIVE_MAX = 60
    SUMMATIVE_MAX = 40

    def __init__(self):
        super().__init__()
        self.assignments = []
        self.formative_total = 0
        self.summative_total = 0

    def add_assignment(self):
        print("")
        print("======================")
        print("vvvvvvvvvvvvvvvvvvvvvv")
        print("======================")
        while True:
            assignment = input("Enter the Assignment: ").strip()
            if not assignment:
                print("Assignment name cannot be empty.")
            else:
                break

        while True:
            category = input("Enter the Assignment Category (Formative/Summative): ").strip().capitalize()
            if not category:
                print("Category cannot be empty.")
            elif category not in ["Formative", "Summative"]:
                print("Invalid category. Must be 'Formative' or 'Summative'.")
            else:
                break

        while True:
            try:
                weight = float(input("Enter the weight (total of final grade): "))
                if weight <= 0 or weight > 100:
                    print("Weight must be between 1 and 100.")
                else:
                    break
            except ValueError:
                print("Please enter a valid number.")

        while True:
            try:
                grade = float(input("Enter the grade obtained (0-100): "))
                if grade < 0 or grade > 100:
                    print("Grade must be between 0 and 100.")
                else:
                    break
            except ValueError:
                print("Please enter a valid grade.")

        weighted_grade = (grade / 100) * weight

        # Check category limit
        if category == "Formative":
            if self.formative_total + weighted_grade > self.FORMATIVE_MAX:
                print(f"Cannot add. Formative total would exceed {self.FORMATIVE_MAX}%.")
                return
            self.formative_total += weighted_grade
        else:
            if self.summative_total + weighted_grade > self.SUMMATIVE_MAX:
                print(f"Cannot add. Summative total would exceed {self.SUMMATIVE_MAX}%.")
                return
            self.summative_total += weighted_grade

        # Store assignment
        self.assignments.append({
            "name": assignment,
            "category": category,
            "weight": weight,
            "grade": grade,
            "weighted_grade": weighted_grade
        })
        print("")
        print("===================")
        print("vvvvvvvvvvvvvvvvvvv")
        print("===================")
        print(f"Added '{assignment}' ({category}) - Weighted Grade: {weighted_grade:.2f}%")

    def display_report(self):
        print("\n--- STUDENT INFO ---")
        print(f"Name: {self.name}")
        print(f"Classroom: {self.classroom}")
        print(f"Cohort: {self.cohort}")
        print(f"Intake: {self.intake}")

        print("\n--- ASSIGNMENTS ---")
        for i, a in enumerate(self.assignments, 1):
            print(f"{i}. {a['name']} ({a['category']}): Grade = {a['grade']}%, Weight = {a['weight']}/{a['weight']}, Contribution = {a['weighted_grade']:.2f}%")

        print(f"\nFormative Total: {self.formative_total:.2f} / {self.FORMATIVE_MAX}")
        print(f"Summative Total: {self.summative_total:.2f} / {self.SUMMATIVE_MAX}")

    def final_report(self):
        print("")
        print("================")
        print("vvvvvvvvvvvvvvvv")
        print("================")
        total = self.formative_total + self.summative_total
        gpa = (total / 100) * 5

        print(f"\nOverall Grade: {total:.2f}%")
        print(f"GPA: {gpa:.2f} / 5.00")

        if self.formative_total >= (self.FORMATIVE_MAX / 2) and self.summative_total >= (self.SUMMATIVE_MAX / 2):
            print("Result: PASS")
        else:
            print("Result: FAIL")


# Main program
student_report = Report()
student_report.collect_info()

while True:
    student_report.add_assignment()
    more = input("Do you want to add another assignment? (yes/no): ").strip().lower()
    if more != "yes":
        break

student_report.display_report()
student_report.final_report()
