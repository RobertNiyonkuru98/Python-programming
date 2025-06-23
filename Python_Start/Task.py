#!/usr/bin/env python3

number=float(input("Enter a number: "))
table = range(1,11)
for i in table:
    answer = number * i
    print(number, "x",i,"=", answer)