# For the intended use of this code, please ensure you have the necessary libraries installed.
# You can install colorama using pip if it's not already installed:

#from effects import type_print, styled_input, loading_spinner, progress_dots, delayed_response, print_colored
# effects.py
import sys
import time
import itertools
# Download colorama if not already installed
# pip install colorama
from colorama import Fore, Style, init
init(autoreset=True)

# Initialize colorama
init(autoreset=True)

def type_print(text, delay=0.03, color="default"):
    """Print text one character at a time, like typewriter."""
    color_codes = {
        "default": "",
        "red": Fore.RED,
        "green": Fore.GREEN,
        "yellow": Fore.YELLOW,
        "blue": Fore.BLUE,
        "magenta": Fore.MAGENTA,
        "cyan": Fore.CYAN,
        "white": Fore.WHITE,
    }

    color_code = color_codes.get(color.lower(), "")
    for char in text:
        sys.stdout.write(f"{color_code}{char}{Style.RESET_ALL}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def styled_input(prompt, color="cyan", delay=0.02, symbol=">> "):
    """Displays a styled input prompt using type_print, then collects input."""
    type_print(prompt, delay=delay,  color=color)
    return input(symbol).strip()

def loading_spinner(task="Loading", duration=2):
    """Shows a spinning animation for a duration with a task label."""
    spinner = itertools.cycle(["|", "/", "-", "\\"])
    end_time = time.time() + duration
    while time.time() < end_time:
        sys.stdout.write(f'\r{task}: {next(spinner)}')
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r' + ' ' * (len(task) + 5) + '\r')

def progress_dots(task="Processing", dots=3, delay=0.4):
    """Displays task followed by increasing dots."""
    for i in range(1, dots + 1):
        print(f"{task}{'.' * i}", end='\r')
        time.sleep(delay)
    print(" " * (len(task) + dots), end='\r') # Clear line

def delayed_response(text, wait=1.5, color=None):
    """Delays then followed by increasing"""
    time.sleep(wait)
    type_print(text, delay=0.02, color=color)

def print_colored(text, color="GREEN"):
    """Prints colored text instantly."""
    print(getattr(Fore, color.upper(), "") + text + Style.RESET_ALL)
class Student:
    def __init__(self):
        self.name = ""
        self.classroom = ""
        self.cohort = ""
        self.intake = ""

    def get_name(self):
        loading_spinner("Loading")
        print("👋🏿👋🏿👋🏿👋🏿👋🏿👋🏿👋🏿👋🏿👋🏿👋🏿👋🏿👋🏿👋🏿")
        progress_dots("SALUTATIONS")
        print("=" * 25)
        type_print("WELCOME TO YOUR DASHBOARD😁")
        print("=" * 25)
        delayed_response("You ready!!, let's get started", wait=3.5, color="green")
        while True:
            name = styled_input("Enter your Name: ")
            if not name.strip():
                type_print("Input cannot be empty")
            elif not name.replace(" ", "").isalpha():
                type_print("Input must contain letters")
            else:
                self.name = name.capitalize()
                break

    def get_classroom(self):
        while True:
            classroom = styled_input("Enter your Class: ")
            if not classroom.strip():
                print_colored("Input cannot be empty", "red")
                #print_colored("Input cannot be empty")
            elif not any(c.isalpha() for c in classroom):
                print_colored("Input must contain letters", "red")
            else:
                self.classroom = classroom.capitalize()
                break

    def get_cohort(self):
        while True:
            cohort = styled_input("Enter your Cohort: ")
            if not cohort.strip():
                print_colored("Input cannot be empty", "red")
            elif not any(c.isalpha() for c in cohort):
                print_colored("Input must contain letters", "red")
            else:
                self.cohort = cohort.capitalize()
                break

    def get_intake(self):
        while True:
            intake = styled_input("Enter your Intake: ")
            if not intake.strip():
                print_colored("Input cannot be empty", "red")
            elif not any(c.isalpha() for c in intake):
                print_colored("Input must contain letters", "red")
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
        print("=" * 25)
        print("v" * 25)
        print("=" * 25)
        while True:
            assignment = styled_input("Enter the Assignment: ").strip()
            if not assignment:
                print_colored("Assignment name cannot be empty.", "red")
            else:
                break

        while True:
            category = styled_input("Enter the Assignment Category (Formative/Summative): ").strip().capitalize()
            if not category:
                print_colored("Category cannot be empty.", "red")
            elif category not in ["Formative", "Summative"]:
                print_colored("Invalid category. Must be 'Formative' or 'Summative'.", "red")
            else:
                break

        while True:
            try:
                weight = float(styled_input("Enter the weight (total of final grade): "))
                if weight <= 0 or weight > 100:
                    print_colored("Weight must be between 1 and 100.", "red")
                else:
                    break
            except ValueError:
                print_colored("Please enter a valid number.", "red")

        while True:
            try:
                grade = float(styled_input("Enter the grade obtained (0-100): "))
                if grade < 0 or grade > 100:
                    print_colored("Grade must be between 0 and 100.", "red")
                else:
                    break
            except ValueError:
                print_colored("Please enter a valid grade.", "red")

        weighted_grade = (grade / 100) * weight

        # Check category limit
        if category == "Formative":
            if self.formative_total + weighted_grade > self.FORMATIVE_MAX:
                type_print(f"Cannot add. Formative total would exceed {self.FORMATIVE_MAX}%.")
                return
            self.formative_total += weighted_grade
        else:
            if self.summative_total + weighted_grade > self.SUMMATIVE_MAX:
                type_print(f"Cannot add. Summative total would exceed {self.SUMMATIVE_MAX}%.")
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
        loading_spinner("Just a moment")
        print("=" * 25)
        print("v" * 25)
        print("=" * 25)
        delayed_response(f"Added '{assignment}' ({category}) - Weighted Grade: {weighted_grade:.2f}%", wait=1.5, color="green")

    def display_report(self):
        print_colored("\n--- STUDENT INFO ---")
        type_print(f"Name: {self.name}")
        type_print(f"Classroom: {self.classroom}")
        type_print(f"Cohort: {self.cohort}")
        type_print(f"Intake: {self.intake}")

        loading_spinner("Loading Assignments")
        loading_spinner("Please wait")
        print_colored("\n--- ASSIGNMENTS ---")
        for i, a in enumerate(self.assignments, 1):
            delayed_response(f"{i}. {a['name']} ({a['category']}): Grade = {a['grade']}%, Weight = {a['weight']}/{a['weight']}, Contribution = {a['weighted_grade']:.2f}%", wait=1.5, color="cyan")

        type_print(f"\nFormative Total: {self.formative_total:.2f} / {self.FORMATIVE_MAX}")
        type_print(f"Summative Total: {self.summative_total:.2f} / {self.SUMMATIVE_MAX}")

    def final_report(self):
        loading_spinner("Finalizing Report")
        print("=" * 25)
        print("v" * 25)
        print("=" * 25)
        total = self.formative_total + self.summative_total
        gpa = (total / 100) * 5

        type_print(f"\nOverall Grade: {total:.2f}%")
        type_print(f"GPA: {gpa:.2f} / 5.00")

        if self.formative_total >= (self.FORMATIVE_MAX / 2) and self.summative_total >= (self.SUMMATIVE_MAX / 2):
            print_colored("Result: PASS", "green")
        else:
            print_colored("Result: FAIL", "red")


# Main program
student_report = Report()
student_report.collect_info()

while True:
    student_report.add_assignment()
    more = styled_input("Do you want to add another assignment? (yes/no): ").strip().lower()
    if more != "yes":
        break

student_report.display_report()
student_report.final_report()
