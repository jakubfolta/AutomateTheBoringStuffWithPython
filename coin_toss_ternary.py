#! python3

'''debugging_coin_toss.py - Simple coin toss game, the player has\
two guesses(simple game). The program has several bugs.\
Find bugs that keep the program from working correctly.---FINISHED'''

import random
import logging

logging.basicConfig(level = logging.INFO, format = '%(asctime)s, %(levelname)s, %(message)s')
logging.disable(logging.INFO)

guess = ''
chance = 0
sides = ['heads', 'tails']
toss = random.randint(0,1)
toss = 'tails' if toss == 0 else 'heads' # Ternary operator
logging.info('Toss is {}.'.format(toss))

while guess not in sides or chance != 2:
    logging.info('Enter the while loop.')
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

    if guess not in sides:
        logging.info('Guess not in sides! Again!')
        continue

    print('You got it! Congratulations!') if toss == guess else print('Nope!')
    if toss == guess:
        break
    chance += 1
    logging.info('It\'s {} chance.'.format(chance))
    continue
else:
    print('I\'m sorry... Try again!')
logging.info('Out of loop.')
