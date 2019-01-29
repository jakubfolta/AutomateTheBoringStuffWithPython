#! python3

import random
import time

messages =
['As I see it, yes', 
'Ask again later', 
'Better not tell you now', 
'Cannot predict now', 
'Concentrate and ask again',
'Don\’t count on it', 
'It is certain', 
'It is decidedly so', 
'Most likely', 
'My reply is no', 
'My sources say no', 
'Outlook good', 
'Outlook not so good', 
'Reply hazy try again', 
'Signs point to yes', 
'Very doubtful', 
'Without a doubt', 
'Yes', 
'Yes, definitely', 
'You may rely on it']

def magic8Ball():
    print('Think about your question and press enter \
to get an answer from Magic 8 Ball...')
    input()

    time.sleep(1)

    print('Magic 8 Ball says...')
    print()

    time.sleep(1)

    ballAnswer = messages[random.randint(0, len(messages))]

    time.sleep(1)

    return ballAnswer.upper()


answer = 'yes'
while answer == 'yes' or answer == 'y':
    print(magic8Ball())
    print()

    print('Do you want to ask again???')
    answer = input()
    
print('See you next time!!!')
time.sleep(1)
exit()
      
