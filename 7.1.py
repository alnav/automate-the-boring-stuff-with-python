'''
Strong Password Detection
Write a function that uses regular expressions to make sure the password string it is passed is strong. 
A strong password is defined as one that is at least eight characters long, contains both uppercase and lowercase characters, and has at least one digit. 
You may need to test the string against multiple regex patterns to validate its strength.
'''

import re

passLength = re.compile(r'[\w|\W]{8,}')
passUpper = re.compile(r'[\w|\W]*[A-Z]')
passLower = re.compile(r'[\w|\W]*[a-z]')
passDigit = re.compile(r'[\w|\W]*\d+')

print("Insert password: ")
password = input()

moLenght = passLength.match(password)
moUpper = passUpper.match(password)
moLower = passLower.match(password)
moDigit = passDigit.match(password)

print(moLenght)
print(moUpper)
print(moLower)
print(moDigit)

if moLenght and moUpper and moLower and moDigit:
    print(password + " is strong enough")

