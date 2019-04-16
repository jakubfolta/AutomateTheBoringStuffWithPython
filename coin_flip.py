import random
heads = 0
for i in range(1, 1001):
    if random.randint(0, 1) == 1:
        heads += 1
    if i == 500:
        print('Halfway done!')
print('Heads came up ' + str(heads) + ' times.')
#
# spam = 7
#
# assert spam >= 10, 'Spam must be greater than 10!'

eggs = 'hello'
bacon = 'HEfllo'

assert eggs.lower() != bacon.lower(), 'Strings can\'t have the same\
 characters, cases don\'t matter! '

assert False, 'This assertion always triggers!'
