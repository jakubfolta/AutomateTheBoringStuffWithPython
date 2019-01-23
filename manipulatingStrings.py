#Double quotes

spam = "That is Alice's cat."
print(spam)

#Escape characters

spam = 'Say hi to Bob\'s mother'
print(spam)

print('Hello there!\nHow are you?\nI\'m doing fine.')

#Raw strings

print(r'That is Carol\'s cat.')

#Multiline strings with triple quotes

print('''Dear Alice,
Eve's cat has been arrested for catnapping, cat burglary, and extortion.
Sincerely,
Bob''')

#Multiline comments

'''This is a test Python program.
Written by Al Sweigart al@inventwithpython.com

This program was designed for Python 3, not Python 2.
'''

def spam():
    '''This is a multiline comment to help
explain what the spam() function does.'''
    print('Hello!')

spam()

#Indexing and slicing integers

spam = 'Hello world!'
print(spam[0])
print(spam[4])
print(spam[-1])
print(spam[0:5])
print(spam[:5])
print(spam[6:])
fizz = spam[0:5]
print(fizz)
print(spam)

#The in and not in operators with strings

print('Hello' in 'Hello world')
print('HELLO' in 'Hello world!')

#Useful string methods

spam = 'Hello world'
spam = spam.upper()
print(spam)
spam = spam.lower()
print(spam)
spam = spam.title()
print(spam)
print(spam.lower())
print(spam)

print('How are you?')
feeling = input()
if feeling.lower() == 'great':
    print('I feel great too!')
else:
    print('I hope the rest of your day is good.')

print(spam.islower())
print(spam.isupper())
print('HELLO'.isupper())

print('Hello'.upper())
print('Hello'.upper().lower().upper())
print('Hello'.lower().islower())

#The isx string methods

print('hello'.isalpha())
print('hello123'.isalpha())
print('hello123'.isalnum())
print('hello'.isalnum())
print('123'.isdecimal())
print('   '.isspace())
print('This Is Title Case'.istitle())

#The startswith() and endswith() string methods

print('Hello world!'.startswith('Hello'))
print('Hello world!'.endswith('world!'))

#The join() and split() string methods

print(', '.join(['cats', 'rats', 'bats']))
print('ABC'.join(['My', 'name', 'is', 'Simon.']))

print('My name is Simon.'.split())
print('MyABCnameABCisABCSimon.'.split('ABC'))
print('My name is Simon'.split('m'))

spam = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".

Please do not drink it.
Sincerely,
Bob'''
print(spam.split('\n'))

#Justifying text with rjust(), ljust(), and center()

print('Hello'.rjust(10))
print('"Hello"'.ljust(20))


















