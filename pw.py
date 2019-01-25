#Project: password locker
#Step 1: Program design and data structures

#! python 3
# pw.py - An insecure password locker program

Passwords = {'email': 'fdwfrevrvfd',
             'blog': 'fwrfervkn3475ygvnf',
             'luggage': 'weih78238dehw8'}

import sys
if len (sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # first command line arg is the account name
