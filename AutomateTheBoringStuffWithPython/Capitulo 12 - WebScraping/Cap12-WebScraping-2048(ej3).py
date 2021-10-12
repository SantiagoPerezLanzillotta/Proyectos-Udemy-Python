#Ejercico 3: 2048
'''
2048 is a simple game where you combine tiles by sliding themup, down, left,
or right with the arrow keys. You can actually get a fairly high score
by repeatedly sliding in an up, right, down, and left pattern over and over again.

Write a program that will open the game at https://gabrielecirulli.github.io/2048/
and keep sending up, right, down, and left keystrokes to automatically play the game

'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys # esto es para tener las tecls
import random
import time

browser = webdriver.Firefox()

browser.get('https://gabrielecirulli.github.io/2048/')

time.sleep(2)

nuevaPartidaBoton = browser.find_element_by_css_selector('.restart-button')
nuevaPartidaBoton.click()

for i in range(900):
    teclas = [Keys.DOWN,Keys.UP,Keys.LEFT,Keys.RIGHT]

    teclaRandom = random.choices(teclas)

    
    pantalla = browser.find_element_by_css_selector('html')
    pantalla.send_keys(teclaRandom)
    print(teclaRandom)     
    

print(f'Todo terminado {i}')
