''' Ejercicio 2 - Coin Flip Streaks:

For this exercise, we’ll try doing an experiment. If you flip a coin 100 times
and write down an “H” for each heads and “T” for each tails, you’ll create a
list that looks like “T T T T H H H H T T.”
If you ask a human to make up 100 random coin flips, you’ll
probably end up with alternating head-tail results like “H T H T H H T H T T,”
which looks random (to humans), but isn’t mathematically random.
A human will almost never write down a streak of six heads or six tails in a row,
even though it is highly likely to happen in truly random coin flips.
Humans are predictably bad at being random.
Write a program to find out how often a streak of six heads
or a streak of six tails comes up in a randomly generated list of heads and
tails.
Your program breaks up the experiment into two parts: the first part generates
a list of randomly selected 'heads' and 'tails' values,
and the second part checks if there is a streak in it.
Put all of this code in a loop that repeats the experiment 10,000 times
so we can find out what percentage of the coin flips contains a streak of six
heads or tails in a row. As a hint, the function call random.randint(0, 1)
will return a 0 value 50% of the time and a 1 value the other 50% of the time.

You can start with the following template:

import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.

    # Code that checks if there is a streak of 6 heads or tails in a row.
print('Chance of streak: %s%%' % (numberOfStreaks / 100))

'''
'''
# 0 = Head
# 1 = Tail

import random
numberOfStreaks = 0

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    listaHT=[]
    for i in range(0,101):        
        HoT = random.randint(0,1)
        listaHT.append(HoT)

    # Code that checks if there is a streak of 6 heads or tails in a row.
    H = 0
    T = 0
    valorAntiguo = 0
    for valorLista in listaHT:
        if valorLista == 0 and valorAntiguo == 0:
            H+=1
            
        if valorLista == 1 and valorAntiguo == 1:
            T+=1

        if H==6 or T==6:
            numberOfStreaks+=1
            H=0
            T=0
        
        if valorLista == 0 and valorAntiguo == 1:
            H=1
            T=0
            valorAntiguo = valorLista
            
        if valorLista == 1 and valorAntiguo == 0:
            H=0
            T=1
            valorAntiguo = valorLista
            
            
       
        
print('Chance of streak: %s%%' % ( (numberOfStreaks / (100*10000))*100))
'''


#extra (v2)

# 0 = Head
# 1 = Tail

import random
Streak6IgualesSeguidos = 0
aparicionesDeH = 0
aparicionesDeT = 0
probDeTenerStreakEn10000 = 0

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    listaHT=[]
    for i in range(0,101):        
        HoT = random.randint(0,1)
        listaHT.append(HoT)

    # Code that checks if there is a streak of 6 heads or tails in a row.
    H = 0
    T = 0
    valorAntiguo = 0
    hayStreaken100 = False
    
    for valorLista in listaHT:
        
        if(valorLista==0):       #calculo la probabilidad de aparicion de H y T
            aparicionesDeH+=1
        else:
            aparicionesDeT+=1 
                        
        if valorLista == 0 and valorAntiguo == 0:
            H+=1
            
        if valorLista == 1 and valorAntiguo == 1:
            T+=1

        if H==6 or T==6:
            Streak6IgualesSeguidos+=1
            H=0
            T=0
            hayStreaken100=True
        
        if valorLista == 0 and valorAntiguo == 1:
            H=1
            T=0
            valorAntiguo = valorLista
            
        if valorLista == 1 and valorAntiguo == 0:
            H=0
            T=1
            valorAntiguo = valorLista
                       
    if hayStreaken100==True:
        probDeTenerStreakEn10000+=1
       
        
print('Probabilidad de tener 6 iguales seguidos: %s%%' % ((Streak6IgualesSeguidos / (100*10000))*100))


#extra
print('aparicionesDeH: %s%%' % ((aparicionesDeH / (100*10000))*100))
print('aparicionesDeT: %s%%' % ((aparicionesDeT / (100*10000))*100))
print('prob de tener streak en 100: %s%%' % ((probDeTenerStreakEn10000 / 100)))

