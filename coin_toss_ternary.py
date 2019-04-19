#! python3

'''debugging_coin_toss.py - Simple coin toss game, the player has\
two guesses(simple game). The program has several bugs.\
Find bugs that keep the program from working correctly.---FINISHED'''

import random
import logging

logging.basicConfig(level = logging.WARNING, format = '%(asctime)s, %(levelname)s, %(message)s')

guess = ''
sides = ['heads', 'tails']
toss = random.randint(0,1)
toss = 'tails' if toss == 0 else 'heads'

while toss not in sides:
    logging.info('Enter the while loop.')
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    print('You got it!') if toss == guess else print('Nope! Guess again!')
    if toss == guess: print('Congratulations')
    else:
        guesss = input()
        print('You got it!') if toss == guess else print('Nope. You are really bad at this game.')
    if toss == guess:
       print('You got it!')
    else:
