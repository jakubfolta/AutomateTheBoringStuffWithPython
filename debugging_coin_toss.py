import random
import logging

logging.basicConfig(level = logging.DEBUG,\
format = '%(asctime)s - %(levelname)s - %(message)s')

guess = ''
toss = random.randint(0, 1) # 0 is tails, 1 is heads
True if toss == 1 else False
logging.info('Toss = ' + str(toss))
while guess not in ('heads', 'tails'):
    logging.debug('Enter the while loop.')
    try:
        print('Guess the coin toss! Enter "heads" or "tails":')
        guess = input()
        guess == 'heads' or guess == 'tails'
        logging.info('Toss is a ' + str(toss))
    except:
        continue



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
