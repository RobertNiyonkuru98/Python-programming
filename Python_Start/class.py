"""
length = 30
width = 10
permiter_rectangle = ( length + width )*2
print("The perimeter is: ", permiter_rectangle, "cm")

# Functions

def add(a, b):
    return a + b

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
result = add(a, b)
print(result)

print(add(2, 7))
"""

List = [1, 2, 3, "GFG", 2.3]
print(List)

print(List[-4])

student_grade = (10, 9, 8, 9, 3, 6, 2)

student_grade[2] = 7
#print(student_grade[2]) # Error elements in a tuple are immutable