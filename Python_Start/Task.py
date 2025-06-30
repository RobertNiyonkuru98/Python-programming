#!/usr/bin/env python3

"""number=float(input("Enter a number: "))
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
"""
grades = {"":""}
print(grades, "is the grade")
student = input("Enter a student to add: ")
grade = input("Enter his/her grade to add: ")
grades_input = [student, grade]
grades[student] = grade
print(grades)