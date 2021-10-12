#Ejercicio 2 : Using the Clipboard to Read a Text Field

'''
While you can send keystrokes to an application’s text fields with pyautogui.write(), you
can’t use PyAutoGUI alone to read the text already inside a text field.
This is where the Pyperclip module can help.

You can use PyAutoGUI to obtain the window for a text editor such as Mu or Notepad, 
bring it to the front of the screen by clicking on it, click inside the text field,
and then send the CTRL-A or image-A hotkey to “select all” and CTRL-C or image-C hotkey to
“copy to clipboard.”

Your Python script can then read the clipboard text by running import pyperclip and pyperclip.paste().

Write a program that follows this procedure for copying the text from a window’s text
fields. Use pyautogui.getWindowsWithTitle('Notepad') (or whichever text editor you choose)
to obtain a Window object. The top and left attributes of this Window object can tell you
where this window is, while the activate() method will ensure it is at the front of the
screen.

You can then click the main text field of the text editor by adding, say, 100 or 200
pixels to the top and left attribute values with pyautogui.click() to put the keyboard focus
there.

Call pyautogui.hotkey('ctrl', 'a') and pyautogui.hotkey('ctrl', 'c') to select all the text and copy it to
the clipboard. 

Finally, call pyperclip.paste() to retrieve the text from the clipboard and paste it into your Python program. 

From there, you can use this string however you want, but just pass it to print() for now.

Note that the window functions of PyAutoGUI only work on Windows as of PyAutoGUI version 1.0.0,
and not on macOS or Linux.
'''
import pyautogui,pyperclip,time

notepad = pyautogui.getWindowsWithTitle('Bloc de notas')
notepad[0].activate()

if notepad[0].isMaximized == False: #si está minimizada la maximizo para que funcione
    notepad[0].maximize()

pyautogui.hotkey('ctrl','e') #selecciono todo el texto del notepad
#time.sleep(2)
pyautogui.hotkey('ctrl','c') #copio todo el texto del notepad
#time.sleep(2)
notepad[0].minimize()
print(pyperclip.paste())
