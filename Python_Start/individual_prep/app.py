#!/usr/bin/env python3

# Starting
"""
age = 20
price = 19.95
first_name = 'Mosh'
is_online = True
print (age)

# Variables and print

patient = 'John Smith'
age = 20
newPatient = True

print ("It is ", newPatient, "That we have a ", age,"year old patient, whose name is ", patient)

# Using input function

name = input("What is your name? ")
print ("Hello " + name)

# Type Conversion

birth_year = input("Enter your birth year: ")
age = 2025 - int(birth_year)
print(age)

First = float(input("Enter the First number: "))
Second = float(input("Enter the Second number: "))
Sum = First + Second
print("Sum is: " + str(Sum))

# Strings

course = 'Python for Beginners'
print(course.upper())
print(course.lower())
print(course.find('y'))
print(course.replace('for', '4'))
print('Python' in course)
print(course)

# Arithmetic operations

x = 10
x += 3
print(x)

# Operator Precedence

x = 10 + 3 * 2
print(x)
# Comparison Operators

x = 3 > 2
print(x)

# Logical Operators

price = 25
print(price > 10 and price < 30)
price = 5
print(price > 10 or price < 30)
print(not price > 10)

# if statements

temperature = 35

if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20:
    print("It's a nice day")
elif temperature > 10:
    print("It's a bit cold")
else:
    print("It's cold")
print("Done")

weight = float(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == 'K':
    print("Weight in Lbs: ", weight / 0.4536)
else:
    print("Weight in kg: ", weight * 0.4536)


# While loops
i = 1
while i <= 10:
    print(i * '*')
    i = i + 1

# Lists

names = ["John", "Bob", "Mosh", "Sam", "Mary"]
names[3] = "Samuel"
print(names[0:4])
print(names)

# List methods

numbers = [1, 2, 3, 4, 5]
numbers.insert(0, -1)
numbers.remove(5)
print(len(numbers))

# For loops

numbers = [1, 2, 3, 4, 5]
for i in numbers:
    print(i)

j = 0
while j < len(numbers):
    print(numbers[j])
    j = j + 1

# The range() function

numbers = range(5, 10, 2)
for number in numbers:
    print(number)


# Tuples

numbers = (1, 2, 3)


tup1 = (2, 3)
print(tup1)
(a, b) = tup1
print('The first element is ',a)
print('The second element is ',b)
tup2 = (101, 'Hari')
tup3 = (102, 'Shiv')
(code1, name1)=tup2
(code2, name2)=tup3
print('The code of ',name1,' is ',code1,'The code of ',name2, ' is ',code2 )
print('The code of ',name2, ' is ',code2)



#FUNCTIONS

def greet():
    print("Hi there")
    print("Welcome aboard")


greet()

#Arguments

def greet(first_name, last_name):
    print(f"Hello {first_name} {last_name}")
    print("Welcome aboard")

greet("Tony", "Robert")
greet("Oleg", "Scott")

# Types of functions
# 1- Perform a task
# 2- Return a value

def get_greeting(name):
    return f"Hello {name}"

message = get_greeting("Robert")
file = open("context.txt", "w")
file.write(message) #??
file.close()


def increment(number, by):
    return number + by

print(increment(10, 20))

# Default argument

def increment(number, by=1):
    return number + by

print(increment(10, 20))

# args, wait and what?

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

print(multiply(2, 3, 4, 5))

#ARGS

def save_user(**user):
    print(user["name"])

save_user(id=1, name="Tony", age=22)

def capital_city(**city):
    print(city)

capital_city(Nigeria="Abuja", Zambia="Lusaka", Rwanda="Kigali")


# Scope

message = "a"
def greet(name):
    global message
    message = "b"

greet("Robert")
print(message)

# Exercise

def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"

    return input

print(fizz_buzz(int(input("Enter a number: "))))
"""
import numbers

# for loop

for i in range(1, 10, 2):
    print("Attempt", i, i * ".")