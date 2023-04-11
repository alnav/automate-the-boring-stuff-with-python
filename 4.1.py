"""
4.1 Comma code

Say you have a list value like this:
spam = ['apples', 'bananas', 'tofu', 'cats']

Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, 
with and inserted before the last item. 
For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. 
But your function should be able to work with any list value passed to it.
"""

def commaCode(list):
    """
    List -> String
    Add comma in between strings in a list, or "and" if element len(list) - 2
    """
    string = ""
    for i in range(len(list)):
        if i == len(list) - 2:
            string += list[i] + " and " + list[i+1]
            print(string)
            return
        else:
            string += list[i] + ", "

commaCode(["1", "2", "3", "4", "5"])
