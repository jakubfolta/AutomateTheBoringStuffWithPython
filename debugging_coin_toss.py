#! python3

'''debugging_coin_toss.py - Simple coin toss game, the player has\
two guesses(simple game). The program has several bugs.\
Find bugs that keep the program from working correctly.'''

import random
import logging

logging.basicConfig(level = logging.DEBUG,\
format = '%(asctime)s - %(levelname)s - %(message)s')

toss = random.randint(0, 1) # 0 is tails, 1 is heads
toss = 'heads' if toss == 1 else 'tails'

logging.info('Toss = ' + toss)

guess = ''
num = 1
while guess not in ('heads', 'tails') or num != 2:
    logging.debug('Enter the while loop.')
    print('Guess the coin toss! Enter "heads" or "tails":')
    guess = input()
    print('You got it!') if toss == guess else print('Nope! Wrong answer!')
    if toss == guess:
        break
    logging.info('Toss is a ' + str(toss))
    num += 1
    logging.debug('num ' + str(num))
else:
    print('You are really bad at this game!')
