#! python3

'''debugging_coin_toss.py - Simple coin toss game, the player has\
two guesses(simple game). The program has several bugs.\
Find bugs that keep the program from working correctly.---FINISHED'''

import random
import logging

logging.basicConfig(level = logging.WARNING, format = '%(asctime)s, %(levelname)s, %(message)s')

guess = ''
chance = 0
sides = ['heads', 'tails']
toss = random.randint(0,1)
toss = 'tails' if toss == 0 else 'heads'


while guess not in sides or chance != 2:
    logging.info('Enter the while loop.')
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

    if guess not in sides:
        logging.info('Guess not in sides! Again!')
        continue

    print('You got it! Congratulations!') if toss == guess else print('Nope! Guess again!')
    
    logging.info('One more try.')
    guesss = input()
    print('You got it! Congratulations!') if toss == guess else print('Nope. You are really bad at this game.')

logging.info('Out of loop.')
