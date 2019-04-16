import random
import logging

logging.basicConfig(level = logging.DEBUG,\
format = '%(asctime)s - %(levelname)s - %(message)s')

guess = ''
while guess not in ('heads', 'tails'):
    logging.debug('Enter the while loop.')
    try:
        print('Guess the coin toss! Enter heads or tails:')
        guess = input()
        toss = random.randint(0, 2) # 0 is tails, 1 is heads
        logging.debug('Toss is a ' + str(toss))

logging.debug('Out of loop.')
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guesss = input()
    if toss == guess:
       print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
