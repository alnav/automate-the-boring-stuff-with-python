"""
Write a function that takes a string and does the same thing as the strip() string method. 
If no other arguments are passed other than the string to strip, then whitespace characters will be removed from the beginning and end of the string. 
Otherwise, the characters specified in the second argument to the function will be removed from the string.
"""

# TODO:
# Fix: Currently not stripping letters from start and end of strings, but removing all given characters

import re

s1 = " this is a string that needs to be stripped "
s2 = " this is one starting with space"
s3 = "this is one ending with space"
s4 = "  multiple spaces   "

test_strings = [s1, s2, s3, s4]

def regex_strip(string_to_strip, char_to_remove = ' '):
    pattern = '[' + char_to_remove + ']'
    mod_string = re.sub(pattern, '', string_to_strip)
    return mod_string

for string_item in test_strings:
    print(regex_strip(string_item))