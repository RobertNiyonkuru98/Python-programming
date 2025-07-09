#!/usr/bin/env python3
"""# Activity

fruits = ["apple", "banana", "cherry", "mango", "Cherry"]

print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

new_fruit = input("Enter fruit name: ")
fruits.append(new_fruit)

print("\nAllfruits:")
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

student_grades = {"Tony":"A", "Robert":"B", "Mitali":"C"}
print("Tony's grade: ",student_grades["Tony"])

student_grades["Oleg"] = "B+"
print("\nAll student grades: ")
for name, grade in student_grades.items():
    print(f"{name}: {grade}")


# ACTIVITY 2
number=float(input("Enter a number: "))
table = range(1,11)
for i in table:
    answer = number * i
    print(number, "x",i,"=", answer)


capital_city = {"Nigeria":"Abuja", "Burundi":"Bujumbura", "Zambia":"Lusaka"}
for country, city in capital_city.items():
    print(f"The Capital city of {country} is {city} ")

# Activity 1

fruits = ["apple", "banana", "cherry", "orange", "avocado"]
print(f"The first fruit is {fruits[0]}")
print(f"The second fruit is {fruits[4]}")

add_fruit = input("Enter another fruit to add: ")
fruits.append(add_fruit)

for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# Activity 2

student_grades = {"Tony":"A+", "Robert":"A", "Oleg":"A-"}
print(student_grades["Tony"],"s the grade of Tony")

student_grades["Audrey"] = "A++"
print(student_grades)

for name, grade in student_grades.items():
 print(f"{name} : {grade}")

grades = {"":""}
print(grades, "is the grade")
student = input("Enter a student to add: ")
grade = input("Enter his/her grade to add: ")
grades_input = [student, grade]
grades[student] = grade
print(grades)
"""

# Activity

"""class Laptops:

    # HardDisk = None
    # Architecture = None
    # Model = None

    def __init__(self,HardDisk,Architecture,Model):
        self.HardDisk = HardDisk
        self.Architecture = Architecture
        self.Model = Model

    def TurnOn(self):
        print("This Laptop can run on by pressing the power button")

    def bits(self):
        print("This Type might support a few software applications")

    def specs(self):
        print(f"Model: {self.Model}")
        print(f"HardDisk: {self.HardDisk}")
        print(f"Architecture: {self.Architecture}")
"""

# Activity 2

"""class Car:
    def __init__(self,Model,Price,Color,Buildyear):
        self.Model = Model
        self.Price = Price
        self.Color = Color
        self.Buildyear = Buildyear

    def model(self):
        print(f"Model: {self.Model}")
    def price(self):
        print(f"Price: {self.Price}")
    def color(self):
        print(f"Color: {self.Color}")
    def buildyear(self):
        print(f"Buildyear: {self.Buildyear}")

Car1 = Car("Audi","10K","Orange", "2020")
print(Car1)
Car1.model()
Car1.price()
Car1.color()
Car1.buildyear()"""

# Activity 3

"""class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"The engine is starting")
        print(f"for The Car with Brand {self.brand}, Model {self.model} and Year {self.year}")

display_info = Car("TOYOTA", "COROLLA", "2022")
print(display_info)
display_info.start_engine()

"""

# Activity 4

class Plane:
    def __init__(self, Passenger, weight):
        self.Passenger = Passenger
        self.weight = weight
class Booking(Plane):
    def __init__(self, Passenger, weight, flight_number):
        self.flight_number = flight_number
        super().__init__(Passenger, weight)

    def __str__(self):
        return f"Hi {self.Passenger},Thank you for choosing us, \nCurrent weight: 0{self.weight}kg"

    def passenger(self):
        Passenger = input("Enter your name: ")
        self.Passenger = Passenger
        print(f"The Passenger is {self.Passenger}")
    def Weight(self):
        weight = int(input("Enter your weight in kgs: "))
        self.weight = weight
        if self.weight <= 300:
            print(f"All good {self.Passenger} you can board the plane")
        else:
            print(f"The Overall Weight {self.weight} exceeds the weight limit"
                  f"and you can't board the plane")
    def Flight_number(self):
        print(f"The flight number is {self.flight_number}\n"
              f"Welcome {self.Passenger} to Flight {self.flight_number}!\n"
              f"Enjoy your Flight")
Passenger = (Booking(" "," ", "A002"))
print(Passenger)
Passenger.passenger()
Passenger.Weight()
Passenger.Flight_number()
