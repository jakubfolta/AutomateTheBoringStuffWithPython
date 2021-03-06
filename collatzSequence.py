import time

print('Hi there, this program will explore what\'s called "Collatz Sequence". What\'s funny, even mathematicians aren\'t sure why it works!')
print()
time.sleep(2)

def checkOddOrEvenNumber(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2

    else:
        print(3 * number + 1)
        return 3 * number + 1

play = 'yes'
while play == 'yes' or play == 'y':
    try:
        enteredNumber = input('Enter some number: ')
        while enteredNumber != 1:
            enteredNumber = checkOddOrEvenNumber(int(enteredNumber))
        else:
            print('Great! Collatz sequence works!\n')
    except ValueError:
        print('Please enter a valid number!')

    play = input('Do you want to check another number? yes/no: ')
     
else:
    print('Alright, see you next time.')

time.sleep(2)
exit()
