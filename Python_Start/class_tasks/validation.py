import re

# establish a pattern for validating email addresses
pattern = r'^\+250\d{9}$'
userInput = input("Enter your phone number: ")

if re.match(pattern, userInput):
    print("Valid Rwandan phone number")
else:
    print("Invalid Rwandan phone number")