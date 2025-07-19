#!/usr/bin/env python3

# First Experiment: Basic Password Check

"""correctPwd = "Tony123"

while True:
    pwd = input("Enter Password: ")
    if pwd == correctPwd:
        print("Access granted")
        break
    else:
        print("Access denied")
"""
# Second Experiment: Improved version

correctPwd = "Tony1234"
attempts = 0

while True:
    pwd = input("Enter Password: ")
    attempts += 1

    # Counting digits using for loop
    digit_count = 0
    for i in pwd:
        if i.isdigit():
            digit_count += 1
    if digit_count == 0:
        print("Error: Must contain at least one digit.")
        continue

    if pwd != correctPwd:
        print("Access denied.")
        if attempts > 1:
            print("Alert: you have entered the wrong password too many times")
        continue

    print("Access granted")
    break