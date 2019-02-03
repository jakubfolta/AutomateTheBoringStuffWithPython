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


















