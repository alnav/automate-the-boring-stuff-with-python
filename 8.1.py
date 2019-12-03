import os
import shelve

text = open("/home/ale/Desktop/automateTheBoringStuffWithPython/text.txt")

print(text.readlines())

shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()
