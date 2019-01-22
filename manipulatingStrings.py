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
