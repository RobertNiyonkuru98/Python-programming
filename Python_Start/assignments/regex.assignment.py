import re

# Patterns to be checked
patternEmail = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
patternUrl = r'^https?:\/\/[^\s/$.?#].[^\s]*$'
patternPhone = r'^(\(\d{3}\)\s?|\d{3}[-.])\d{3}[-.]\d{4}$'
patternCredit = r'^(\d{4}[-\s]?){3}\d{4}$'

# User information form

userEmail = input("Enter your username: ")
url = input("Website:")
phone = input("Enter your Phone number \n"
"with country code: ")
credit= input("Enter your Credit number: ")

if re.match(patternEmail, userEmail):
    print("Valid Email")
else:
    print("Invalid Email")

if re.match(patternUrl, url):
    print("Valid URL")
else:
    print("Invalid URL")

if re.match(patternPhone, phone):
    print("Valid Phone number")
else:
    print("Invalid Phone number")

if re.match(patternCredit, credit):
    print("Valid Credit Card")
else:
    print("Invalid Credit Card")
