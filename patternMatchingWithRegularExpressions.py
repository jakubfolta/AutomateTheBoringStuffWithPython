#Finding patterns of text without regular expressions

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242'))
print('Moshi moshi is a phone number:')
print(isPhoneNumber('Moshi moshi'))        
        
message = 'Call me at 415-555-1011 tomorrow.\
415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')

#Finding patterns of text with regular expressions

'''\d\d\d-\d\d\d-\d\d\d\d
\d{3}-\d{3}-\d{4}'''

#Creating regex objects

import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

#Matching regex objects

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())

#Grouping with parentheses

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('Mu number is 514-345-5654')
print(mo.group(1))
print(mo.group(2))
print('Area code is: ' + mo.group(1))
print(mo.group(0))
print(mo.group())

print(mo.groups())

areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)

phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415) 555-5465.')
print(mo.group(1))
print(mo.group(2))

#Matching multiple groups with the pipe

heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
print(mo1.group())

mo2 = heroRegex.search('Tina Fey and Batman')

print(mo2.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')

print(mo.group())

print(mo.group(1))

#Optional matching with a question mark

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The adventures of Batman')

print(mo1.group())

mo2 = batRegex.search('The adventures of Batwoman')

print(mo2.group())

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-458-7898')

print(mo1.group())

mo2 = phoneRegex.search('My number is 456-4582')

print(mo2.group())

#Matching zero or more with the star

batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The adventures of Batman')

print(mo1.group())

mo2 = batRegex.search('The adventures of Batwoman')

print(mo2.group())

mo3 = batRegex.search('The adventures of Batwowowowoman')

print(mo3.group())

#Matching one or more with the plus

batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The adventures of Batwoman')

print(mo1.group())

mo2 = batRegex.search('The adventures of Batwowowowoman')

print(mo2.group())

mo3 = batRegex.search('The adventures of Batman')
print(mo3 == None)

#Matching specific repetitions with curly brackets

haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')

print(mo1.group())

mo2 = haRegex.search('Ha')
print(mo2 == None)

#Greedy and nongreedy matching

greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())

nonGreedyRegex = re.compile(r'(Ha){3,5}?')
mo2 = nonGreedyRegex.search('HaHaHaHaHaHaHaHa')
print(mo2.group())

#The findall() method

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 234-423-3245 Work: 211-357-5433')
print(mo.group())

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo1 = phoneNumRegex.findall('Cell: 234-423-3245 Work: 211-357-5433')
print(mo1)

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo1 = phoneNumRegex.findall('Cell: 234-423-3245 Work: 211-357-5433')
print(mo1)

#Character classes

xmasRegex = re.compile(r'\d+\s\w+')
mo = xmasRegex.findall('12 drummers, 11 pipers, \
10 lords, 9 ladies, 8 maids, \
7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(mo)

#Making your own character classes

vowelRegex = re.compile(r'[aeiouAEIOU]')
mo = vowelRegex.findall('Robocop eats baby food. BABY FOOD.')
print('-'.join(mo))

consonantRegex = re.compile(r'[^aeiouAEIOU]')
mo = consonantRegex.findall('Robocop eats baby FOOD.')
print(mo)

#The carret and dollar sign characters

beginsWithHello = re.compile(r'^Hello')
mo = beginsWithHello.search('Hello world!')
print(mo)

beginsWithHello.search('He said hello.') == None

endsWithNumber = re.compile(r'\d$')
mo = endsWithNumber.search('Your number is 43')
print(mo)

#The wildcard character

atRegex = re.compile(r'.at')
mo = atRegex.findall('The cat in the hat sat on the flat mat.')
print(mo)

#Matching everything with dot-star

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))
print(mo.group(2))

nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

#Matching newlines with the dot character

noNewLineRegex = re.compile('.*')
mo = noNewLineRegex.search('Serve the public trust.\nProtect the innocet.\nUphold the law.').group()
print(mo)

newLineRegex = re.compile('.*', re.DOTALL)
mo = newLineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
print(mo)

#Case-insensitive matching

regex1 = re.compile('RobocoP')
regex1 = re.compile('RobOcop')
regex1 = re.compile('robocoP')
regex1 = re.compile('RoBocOp')

robocop = re.compile(r'robocop', re.I)
mo = robocop.search('Robocop is a part man, part machine, all cop').group()
print(mo)

mo1 = robocop.search('RoboCOP protects the innocent.').group()
print(mo1)

mo2 = robocop.search('Al, why does your programming book talk about robocop so much?').group()
print(mo2)

#Substituting strings with the sub() method

namesRegex = re.compile(r'Agent \w+')
mo = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print(mo)

agentNamesRegex = re.compile(r'Agent (\w)\w*')
mo = agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol \
that Agent Eve knew Agent Bob was a double Agent.')
print(mo)

#Managing complex regexes

phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?             #area code
(\s|-|\.)?                     #separator
\d{3}                          #first 3 digits
(\s|-|\.)                      #separator
\d{4}                          #last 4 digits
(\s*(ext|x|ext.)\s*\d{2,5})?   #extension
)''', re.VERBOSE)

#Combining re.Ignorecase, re.DOTALL, and re.VERBOSE

someRegexValue = re.compile('foo' ,re.IGNORECASE | re.DOTALL)

someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)

#Project:Phone number and email address extractor

#Practice questions

#Q: How to write a regex that matches a number with
#commas for every three digits?

numberRegex = re.compile(r'^\d{1,3}(,\d{3})*$')

#Q: How would you write a regex that matches the full name of someone
#whose last name is Nakamoto? You can assume that the first name
#that comes before it will always be one
#word that begins with a capital letter.

nameRegex = re.compile(r'[A-Z][a-z]*\sNakamoto')

#Q: How would you write a regex that matches a sentence
#where the first word is either Alice, Bob, or Carol; the
#second word is either eats, pets, or throws; the third 
#word is apples, cats, or baseballs; and the
#sentence ends with a period?
#This regex should be case-insensitive.

textRegex = re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.$', re.IGNORECASE)
mo = textRegex.search('Alice eats apples.')
mor = textRegex.search('ALICE THROWS FOOTBALLS.')
print(mo.group())
print(mor)

#Q: Write a function that uses regular expressions to make sure the password
#string it is passed is strong. A strong password is defined as one that
#is at least eight characters long, contains both uppercase and
#lowercase characters, and has at least one digit. You may need to test
#the string against multiple regex patterns to validate its strength.

passwordRegex = re.compile(r'(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])[a-zA-Z0-9]{8,}')
mo = passwordRegex.search('ghPjghhb4c45def')
print(mo)
if mo != None:
    print('Done')
else:
    print('No match!')

def checkIfStrongPassword():
    print('Your password should be at least 8 characters long and \
should containss at least one lowercase, one uppercase \
character and at least one digit.   ')
    print('Please enter your password to check if it\'s valid:')
    password = input()
    if passwordRegex.search(password) != None:
        print('Your password is valid')
    else:
        print('Your password is not valid')

checkIfStrongPassword()

#Q: Write a function that takes a string and does the same
#thing as the strip() string method. If no other arguments
#are passed other than the string to strip, then whitespace
#characters will be removed from the beginning and end of
#the string. Otherwise, the characters specified in the second
#argument to the function will be removed from the string.

stripRegex = re.compile(r'\s*')
mo = stripRegex.sub('', '" kjghgj "')
print(mo)


























