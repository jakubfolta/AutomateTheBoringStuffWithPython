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

















