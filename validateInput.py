while True:
    print('Enter your age: ')
    age = input()
    if age.isdecimal():
        break
    print('Please enter the number for your age.')

while True:
    print('Please enter a new password(letters and numbers only):')
    password = input()
    if password.isalnum():
        print('Password updated.')
        break
    print('Numbers and letters!')


