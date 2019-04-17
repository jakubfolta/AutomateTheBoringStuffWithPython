import random
import logging

logging.basicConfig(level = logging.DEBUG,\
format = '%(asctime)s - %(levelname)s - %(message)s')

toss = random.randint(0, 1) # 0 is tails, 1 is heads
toss = 'heads' if toss == 1 else 'tails'

logging.info('Toss = ' + toss)

def check_guess():
    guess = ''
    while guess not in ('heads', 'tails'):
        logging.debug('Enter the while loop.')
        try:
            print('Guess the coin toss! Enter "heads" or "tails":')
            guess = input()
            guess == 'heads' or guess == 'tails'
            logging.info('Toss is a ' + str(toss))
        except:
            continue
    return guess

if toss == check_guess():
    print('You got it!')
else:
    print('Nope! Guess again!')
    if toss == check_guess():
       print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
