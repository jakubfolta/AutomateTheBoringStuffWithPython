#The list data type
[1, 2, 3, 'cat', 'dog']

spam = ['dog', 'cat']
print(spam)
#Getting individual values in a list with indexes
spam = ['cat', 'dog', 'bat', 'elephant']
print(spam[0])
print(spam[1])
print(spam[2])

print('The ' + spam[2] + ' ate the ' + spam[0] + '.')

spam = [['cat', 'bat', 'rat'],[20, 45, 56, 67]]

print(spam[0])
print(spam[1][3])
#Negative indexes
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[-1])
print('The ' + spam[-1] + ' is afraid of the ' + spam[-3] + '.')
#Getting sublists with slices
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[0:4])
print(spam[0:-1])

print(spam[:4])
print(spam[0:])
print(spam[:])
#List's length with len()
spam = ['cat', 'dog', 'moose']
print(len(spam))
#Changing values in a list with indexes 
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam)
spam[1] = 'aardvark'
print(spam)
spam[2] = spam[1]
print(spam)
spam[-1] = 1234
print(spam)
#Lists concatenation and replication
spam = [1, 2, 3]
bacon = ['cat', 'dog', 'rat']
spamBacon = spam + bacon
print(spamBacon)
spam = spam * 3
print(spam)
#Removing values from a list with del statements
spam = ['cat', 'bat', 'rat', 'elephant']
del spam[2]
print(spam)
del spam[2]
print(spam)
#Working with lists
catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop): ')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]

print('The cat names are: ')
for x in catNames:
    print('    ' + x)
#Using for loops with lists
for i in range(4):
    print(i)

supplies = ['pens', 'staplers', 'flame-thrower', 'binder']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is a ' + supplies[i] + '.')
#The in and not in operators
print('howdy' in ['hello', 'hi', 'howdy', 'heyas'])
spam = ['hello', 'hi', 'howdy', 'heyas']
print('cat' in spam)

myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name: ')
name = input()
if name not in myPets:
    print('I do not have pet named ' + name + '.')
else:
    print(name + ' is my pet.')
#The multiple assignment trick
cat = ['fat', 'orange', 'loud']
size, color, disposition = cat
print(size)

a, b = 'Alice', 'Bob'
a, b = b, a

print(a)
#Augmented assignment operators
spam = 42
spam = spam + 1
print(spam)

spam = 44
spam += 2
print(spam)

spam = 'Hello'
spam += ' World!'
print(spam)

spam = ['Zophie']
spam *= 3
print(spam)
#Methods
spam = ['hello', 'hi', 'howdy']
print(spam.index('hello'))
#print(spam.index('heyas'))

spam = ['Zophie', 'Pooka', 'Elvis', 'Pooka']
print(spam.index('Pooka')) # first appearance
#Adding values to lists with the append() and insert() methods
spam = ['cat', 'dog', 'bat']
spam.append('moose')
print(spam)
spam = ['cat', 'dog', 'bat']
spam.insert(1, 'moose')
print(spam)
#Removing values from lists with remove()
spam = ['cat', 'bat', 'rat']
print(spam)
spam.remove('bat')
print(spam)
del spam[0]
print(spam)
#Sorting the values in a list with the sort() method
spam = [1, 3, 5, 65, 23, 54, 46, 233, 6]
spam.sort()
print(spam)

spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
spam.sort()
print(spam)
spam.sort(reverse = True)
print(spam)

spam = ['Alice', 'ants', 'Bob', 'cat', 'Rogers']
spam.sort()
print(spam)
spam.sort(key = str.lower)
print(spam)
#Example program: Magic 8 ball with a list
import random

messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']
print(messages[random.randint(0, len(messages) - 1)])

print('Four score and seven ' + \
      'years ago...')
#List-like types: Strings and Tuples 
name = 'Zophie'
print(name[0])
print(name[-2])
print(name[0:3])
print('Zo' in name)

for i in name:
    print('***' + i + '***')
#Mutable and inmutable data types
name = 'Zophie a cat'
newName = name[0:7] + 'the' + name[8:12]
print(name)
print(newName)

eggs = [1, 2, 3]
print(eggs)
eggs = [4, 5, 6]
print(eggs)

eggs = [1, 2, 4]
print(eggs)
del eggs[0]
del eggs[1]
del eggs[0]

eggs.append(4)
eggs.append(5)
eggs.append(6)
print(eggs)
#The tuple data type
eggs = ('hello', 4, 5.4)
print(eggs[0])
print(eggs[1])

print(type(('hello',)))
print(type(('hello')))
#Converting types with the list() and tuple() functions
print(tuple(['cat', 'dog', 5]))
print(list(('cat', 'dog', 5)))
#References
spam = 42
cheese = spam
spam = 288
print(spam)
print(cheese)

spam = [1, 2, 3, 4, 5]
cheese = spam
cheese[1] = 'Hello!'
print(spam)
print(cheese)
#Passing references

































