#! python3

'''coin_solidifying.py - Simple coin toss game, the player has\
two guesses(simple game). The program has several bugs.\
Find bugs that keep the program from working correctly.'''

# Import essential modules.
import random
import logging
logging.basicConfig(level = logging.INFO, format = '%(levelname)s, %(message)s')
#logging.disable(logging.CRITICAL)

# Set essential variables: guess, number, toss, sides.
guess = ''
number = 0
sides = ['heads', 'tails']
toss = random.randint(0, 1) # 0 is heads, 1 is tails.

# Set toss to one of two coin sides.
toss = 'heads' if toss == 0 else 'tails'
logging.info('Toss is {}.'.format(toss))
# Use while loop to check if user guess is right and act appropriately.
while guess not in sides or number != 2:
    print('Guess, "heads" or "tails"')
    guess = input()
    logging.info('Guess is {}.'.format(guess))
    if guess not in sides:
        logging.info('Guess not in sides.')
        continue
    print('You got it!') if guess == toss else print('Nope.')
    if guess == toss:
        logging.info('Guess is equal to toss!')
        break
    number += 1
    logging.info('Number is {}.'.format(number))
else:
    logging.info('Out of loop, not guessed.')
    print('Try again if you dare to.')
