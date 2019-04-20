#! python3

'''debugging_coin_toss.py - Simple coin toss game, the player has\
two guesses(simple game). The program has several bugs.\
Find bugs that keep the program from working correctly.---FINISHED'''

import random
import logging

logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s, %(levelname)s, %(message)s')
#logging.disable(logging.INFO)

guess = ''
chance = 0
toss = random.randint(0, 1) # 0 is tails, 1 is heads
toss = 'tails' if toss==0 else 'heads'
logging.info('Toss is a {}.'.format(toss))
sides = ['heads', 'tails']

while guess not in sides or chance != 2:
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

    if guess not in sides: continue

    print('You got it!') if toss == guess else print('Nope!')

    logging.info('Guessed, out of loop.')

    else:
        logging.info('Second guess in else.')

        guess = input()
        print('You got it!') if toss == guess else print('Nope. You are really bad at this game.')
