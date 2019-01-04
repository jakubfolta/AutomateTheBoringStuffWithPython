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





































