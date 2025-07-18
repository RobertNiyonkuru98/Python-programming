# Chapter 2

"""a = 5
answer= a + 2.7
print(answer)

a = 5
b = 2
answer = a / b
print(answer)

a = 5
b = 2
c = float(a) / b
print(c)

a = 2
b = 'A'
c = a + b
print(c)


a= 'A'
b = 2*a
print(b)


a= 5
b = 2
a = a + b
b = a - b
a = a - b
print(a)

a = 5
b * b = a
print(b)

(a, b) = (2, 3)
(c, d) = (4, 5)
print((a, b) + (c, d))
#print((a, b) - (c, d))
#print((a, b) * (c, d))

a = 'harsh'
b = a[1: len(a)]
c = [-3, len (a)]
d
e = 'tar'
f = 'rat'
g = [2*(e + f)]
print(b)
print(c)
print(g)

a = 2
b = 5
c = a
a = b
b = c
print(a)
print(b)

import math
a = float(input("Enter the first point, a: "))
b = float(input("Enter the second point, b: "))
(x, y) = (0, 0)
print("(a, b)","=", (a, b))

distance = math.sqrt(a**2 + b**2)

print(distance)

x1 = (float(input("Enter the first position on x1: ",)))
y1 = (float(input("Enter the second position on y1: ",)))
x2 = (float(input("Enter the second position on x2: ")))
y2 = (float(input("Enter the second position on y2: ",)))
Point_1 = (x1, y1)
Point_2 = (x2, y2)
print(Point_1)
print(Point_2)

distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print("distance =", "square root of (x2-x1)**2 + (y2-y1)**2", "=", distance )

import math
x1 = (float(input("Enter the first position on x1: ")))
y1 = (float(input("Enter the second position on y1: ")))
x2 = (float(input("Enter the first position on x2: ")))
y2 = (float(input("Enter the second position on y2: ")))
x3 = (float(input("Enter the first position on x3: ")))
y3 = (float(input("Enter the second position on y3: ")))
Point_1 = (x1, y1)
Point_2 = (x2, y2)
Point_3 = (x3, y3)
print(Point_1)
print(Point_2)
print(Point_3)
DistFrom1_2 = math.sqrt((x2-x1)**2 + (y2-y1)**2)
DistFrom1_3 = math.sqrt((x3-x1)**2 + (y3-y1)**2)
DistFrom2_3 = math.sqrt((x3-x2)**2 + (y3-y2)**2)
print(DistFrom1_2)
print(DistFrom1_3)
print(DistFrom2_3)
Perimeter = DistFrom1_2 + DistFrom1_3 + DistFrom2_3
print(Perimeter)
SemiPerimeter = Perimeter / 2
print(SemiPerimeter)
Area = math.sqrt(SemiPerimeter*(SemiPerimeter - DistFrom1_2)*(SemiPerimeter - DistFrom1_3)*(SemiPerimeter - DistFrom2_3))
print(Area)
if round(Area, 6) == 0:
    print("All the points are collinear.")
else:
    print("The points are not collinear.")

    if round(DistFrom1_2, 6) == round(DistFrom1_3, 6) == round(DistFrom2_3, 6):
        print("The triangle is Equilateral.")
    elif round(DistFrom1_2, 6) == round(DistFrom1_3, 6) or round(DistFrom1_2, 6) == round(DistFrom2_3, 6) or round(DistFrom1_2, 6) == round(DistFrom2_3, 6):
        print("The triangle is Isosceles.")
    else:
        print("The triangle is Scalene.")


# CHAPTER 3

a = input("Enter the first number: ")
b = input("Enter the second number: ")
c = input("Enter the third number: ")

big = (a if (a > c) else c) if (a > b) else (b if (b > c) else c)
print(big)

hbbooks = {'Programming in C#': 2014, 'Algorithms': 2015, 'Python': 2016}
print(hbbooks.get('Programming in C#', 'Wrong Choice'))
print(hbbooks.get('Algorithms', 'Wrong Choice'))
print(hbbooks.get('Python', 'Wrong Choice'))
danbrown = {'The davinci code': 2003, 'Angels and Demons': 2004}
print(danbrown.get('The Davinci code', 'Wrong Choice'))
print(danbrown.get('Angelos and Demons', 'Wrong Choice'))
favbook = {'Dante\'s inferno': 2000, 'Atomic Habits': 2020}
print(favbook.get('Dante inferno', 'Wrong Choice'))
print(favbook.get('Atomic Habits', 'Wrong Choice'))
"""
n = int(input("Enter the factorial number: "))
factorial = 1
i = 1
while i<=n :
    factorial *= i
    i += 1
print('factorial of ', n, 'is', factorial)

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
power = 1
i = 1
while i <= b :
    power *= a
    i += 1
print(a, 'to the power of ', b, 'is', power)

a = int(input("Enter the first term of Arithmetic progression: "))
d = int(input("Enter the common difference: "))
n = int(input("Enter the number of terms of Arithmetic progression: "))
i = 1
sum = 0