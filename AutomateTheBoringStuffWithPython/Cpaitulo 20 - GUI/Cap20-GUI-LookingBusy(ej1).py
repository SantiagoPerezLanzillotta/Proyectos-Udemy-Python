#Ejercicio 1: Looking Busy

'''
Many instant messaging programs determine whether you are idle, or away from your computer,
by detecting a lack of mouse movement over some period of time —say, 10 minutes.

Maybe you’re away from your computer but don’t want others to see your
instant messenger status go into idle mode.

Write a script to nudge your mouse cursor slightly every 10 seconds.

The nudge should be small and infrequent enough so that it
won’t get in the way if you do happen to need to use your computer while the script is running.
'''

import pyautogui
pyautogui.PAUSE=10
ancho,alto = pyautogui.size()
pyautogui.moveTo(ancho/2,alto/2)
while True:
    pyautogui.move(-10,-10)
    pyautogui.move(+10,+10)


