#! python3


'''debugging_coin_toss.py - Simple coin toss game, the player has\
two guesses(simple game). The program has several bugs.\
Find bugs that keep the program from working correctly.'''

# Import essential modules.
import random
import logging

logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s, %(levelname)s, %(message)s')
logging.disable(logging.WARNING)

# Set the sides of coin.
sides = ['heads', 'tails']

# Set the coin toss name, number of guesses and guess variable - ternary operator.
toss = random.randint(0, 1) # 0 is heads, 1 is tails
toss = 'heads' if toss == 0 else 'tails'
logging.info('Toss is {}.'.format(toss))
number = 0
guess = ''

# Use while loop to give two guesses and check if input is a proper name.
while guess not in sides or number != 2:
    logging.info('Enter the loop.')
    print('Guess, is it "heads" or "tails"?')
    guess = input()
    logging.info('Guess is {}'.format(guess))
    if guess not in sides:
        logging.info('Guess not in sides!')
        continue
    print('You got it!') if guess == toss else print('Nope!')
    if guess == toss:
        break
    number += 1
else:
    logging.info('Out of loop, not guessed!')
    print('Sorry, try again!')
