import logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s\
 - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)

logging.info('Start of the program.')

def factorial(n):
    logging.debug('Start of factorial: {}'.format(n))
    total = 1
    for i in range(n + 1):
        total *= i
        logging.warning('i is ' + str(i) + ', total is ' + str(total))
    logging.critical('End of factorial: {}'.format(n))
    return total

print(factorial(5))
logging.debug('End of program.')

# logging.basicConfig(level = logging.DEBUG, format = '%(asctime)\
# - %(levelname) - %(message)s')
