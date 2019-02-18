#Backslash on Windows and Forward Slash on OS X and Linux

import os

os.path.join('usr', 'bin', 'spam')

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(os.path.join('C:\\Users\\asweigart', filename))

#The current working directory

import os

print(os.getcwd())
'''print(os.chdir('C\\Windows\\System32'))'''

#Absolute vs Relative paths
#Creating new folders with os.makedirs()

import os

'''print(os.makedirs('C:\\delicious\\walnut\\waffles'))'''

#The os.path module
#Handling absolute and relative paths
print(os.path.abspath('.'))

print(os.path.abspath(('.\\Scripts')))

print(os.path.isabs(os.path.abspath('.')))

print(os.path.relpath('C:\\Windows', 'C:\\'))

print(os.path.relpath('C:\\Windows', 'C:\\spam\\eggs'))

print(os.getcwd(), 'C:\\Python34')

path = 'C:\\Windows\\System32\\calc.exe'
print(os.path.basename(path))

print(os.path.dirname(path))

calcFilePath = 'C:\\Windows\\System32\\calc.exe'

print(os.path.split(calcFilePath))

print((os.path.dirname(calcFilePath), os.path.basename(calcFilePath)))

print(calcFilePath.split(os.path.sep))
'''
#Finding file sizes and folder contents

print(os.path.getsize('C:\\Windows\\System32\\calc.exe'))

print(os.listdir('C:\\Windows\\System32'))

totalSize = 0
for filename in os.listdir('C:\\Windows\\System32'):
       totalSize = totalSize + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))                   

print(totalSize)
'''
#Checking path validity\

print(os.path.exists('C:\\Windows'))
print(os.path.exists('C:\\Somefolder'))
print(os.path.isdir('C:\\Windows\\System32'))
print(os.path.isfile('C\\Windows\\System32'))
print(os.path.isfile('C:\\Windows\\System32\\calc.exe'))
print(os.path.exists('D:\\'))

#The file reading/writing process
#Opening files with the open() function

hellofile = open('C:\\Users\ogi-8\hello.txt')

#Reading the contents of files

helloContent = hellofile.read()
print(helloContent)

sonnetFile = open('C:\\Users\ogi-8\sonnet29.txt')
print(sonnetFile.readlines())

#Writing to files

baconFile = open('bacon.txt', 'w')
print(baconFile.write('Hello world!\n'))
baconFile.close()

baconFile = open('bacon.txt', 'a')
print(baconFile.write('Bacon is not a vegetable.'))
baconFile.close()

baconFile = open('bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)

#Saving variables with the shelve module

import shelve
shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

shelfFile = shelve.open('mydata')
print(type(shelfFile))
print(shelfFile['cats'])
shelfFile.close()

shelfFile = shelve.open('mydata')
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()

#Saving variables with the pprint.pformat() function
import pprint
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
pprint.pformat(cats)

fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()

fileObj = open('myCats.py')
print(fileObj.read())
fileObj.close()

import myCats

print(myCats.cats)






















