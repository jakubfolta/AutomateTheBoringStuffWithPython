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


















    

