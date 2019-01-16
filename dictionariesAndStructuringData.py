myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
print(myCat['size'])

print('My cat has ' + myCat['color'] + ' fur.')

spam = {123: 'Luggage combination', 32: 'The answer'}
print(spam[123])

#Dictionaries vs Lists

spam = ['cats', 'dogs', 'moose']
eggs = ['dogs', 'moose', 'cats']
print(spam == eggs)

eggs = {'name': 'Zophie', 'species': 'cat'}
ham = {'species': 'cat', 'name': 'Zophie'}
print(eggs == ham)

#The keys(), values() and items() methods

spam = {'color': 'red', 'age': 32}

for v in spam.values():
    print(v)
    
for k in spam.keys():
    print(k)

for i in spam.items():
    print(i)

for i in spam.items():
    print(list(i))

for x, y in spam.items():
    print('Key: ' + x + ' Value: ' + str(y))

#Checking whether a key or value exists in a dictionary

spam = {'name': 'Zophie', 'age': 7}

print('name' in spam.keys())

print('Zophie' in spam.values())

print('color' in spam.keys())

print('color' not in spam.keys())

#The get() method

picnicItems = {'apples':5, 'cups':2}
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')

print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.')

#The sedefault() method

spam = {'name': 'Pooka', 'age': 5}
print(spam)
if 'color' not in spam:
    spam['color'] = 'black'
print(spam)

spam = {'name': 'Pooka', 'age': 5}
print(spam)
spam.setdefault('color', 'black')
print(spam)

spam = {'name': 'Pooka', 'age': 4}
print(spam)
spam.setdefault('color', 'black')
print(spam)
print(spam.setdefault('color', 'white'))

#Pretty printing

import pprint

message = 'It was a bright cold day in April, and the\
clocks were striking thirteen.'

count = {}

for x in message:
    count.setdefault(x, 0)
    count[x] = count[x] + 1

pprint.pprint(count)

#Using data structures to model real-world things
#Nested dictionaries and lists

allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
              'Bob': {'ham sandwiches': 3, 'apples': 2},
              'Carol': {'cups': 3, 'apples pies': 1}}

def totalBrought(guests, item):
    numBrought = 0
    for x, y in guests.items():
        numBrought = numBrought + y.get(item, 0)
    return numBrought

print('Number of things beeing brought: ')
print(' - Apples ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple pies ' + str(totalBrought(allGuests, 'apple pies')))
print(' - Bananas ' + str(totalBrought(allGuests, 'bananas')))


allGuests = {'Alice': {'apple': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}

def countTotalDelivery(people, item):
    totalItems = 0
    for x, y in people.items():
        totalItems = totalItems + y.get(item, 0)
    


































    

