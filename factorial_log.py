import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s\
 - %(message)s')
 
#logging.disable(logging.CRITICAL)

logging.debug('Start of the program.')

def factorial(n):
    logging.debug('Start of factorial: {}'.format(n))
    total = 1
    for i in range(n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial: {}'.format(n))
    return total

print(factorial(5))
logging.debug('End of program.')
