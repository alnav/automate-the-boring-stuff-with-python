# madlibs.py Mad Libs

# Substitute words to compose a mad libs text

import os
import re

#!TODO substitute word without deleting punctuation

def substituteWord(word):
    if re.compile(r'ADJECTIVE[,.:!?]*').search(word):
        print("Enter an adjective: ")
        return input()
    elif re.compile(r'VERB[,.:!?]*').search(word):
        print("Enter a verb: ")
        return input()
    elif re.compile(r'NOUN[,.:!?]*').search(word):
        print("Enter a noun: ")
        return input()
    else:
        return word

madTxt = open("madlibs.txt")

wordList = madTxt.read().split()

print(wordList)

finalMadLib = ""

for word in wordList:
    temp = substituteWord(word)
    finalMadLib += temp + " "

print(finalMadLib)


