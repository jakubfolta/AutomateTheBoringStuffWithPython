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
toss = random.randint(0, 1) # 0 is heads, 1 is tails.

# Set toss to one of two coin sides.
toss = 'heads' if toss == 0 else 'tails'

# TODO: Use while loop to check if user guess is right and act appropriately.
while guess not in sides and number != 2:
    
