#Ejercicio 1 

'''
The following program is meant to be a simple coin toss guessing game.
The player gets two guesses (it’s an easy game). However, the program
has several bugs in it.

Run through the program a few times to find the bugs that keep the program
from working correctly.
'''
import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')


import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    logging.debug('Clase del guess %s'%(type(guess)))
    logging.debug('valor guess1 %s'%(guess))
    
toss = random.randint(0, 1) # 0 is tails, 1 is heads
logging.debug('Clase del toss %s'%(type(toss)))
logging.debug('valor toss %s'%(toss))


if (toss == 0) & (guess=='heads'):
    print('You got it!')
else:
    if (toss == 1) & (guess=='tails'):
        print('You got it!')        
    else:
        print('Nope! Guess again!')
        guess = input()
        logging.debug('valor guess2 %s'%(guess))
        if (toss == 0) & (guess=='heads'):
            print('You got it!')
        else:
            print('Nope. You are really bad at this game.')
