"""
Write a function that takes a string and does the same thing as the strip() string method. 
If no other arguments are passed other than the string to strip, then whitespace characters will be removed from the beginning and end of the string. 
Otherwise, the characters specified in the second argument to the function will be removed from the string.
"""

import re

stripRe = re.compile(r'[^\s]+')

s1 = " this is a sting that needs to be stripped "
s2 = " this is one starting with space"
s3 = "this is one ending with space"
s4 = "  multiple spaces   "

mo1 = stripRe.match(s1)
mo2 = stripRe.match(s2)
mo3 = stripRe.match(s3)
mo4 = stripRe.match(s4)

print(mo1)
print(mo2)
print(mo3)
print(mo4)