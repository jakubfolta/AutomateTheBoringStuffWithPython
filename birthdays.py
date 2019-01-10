birthdayFile = open('FriendsFamilyBirthdays.txt', 'w')
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
birthdayFile.write(str(birthdays))


while True:
    print('Enter a name to check: (blank to quit)')
    name = input()
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + 'is the birthaday of ' + name + '.')
    else:
        print('I don\'t have birthday info of ' + name + '.')
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')

birthdayFile.close()

exit()
