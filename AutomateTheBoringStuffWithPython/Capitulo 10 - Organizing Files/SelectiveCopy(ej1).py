#Ejercicio 1: Selective Copy
'''
Write a program that walks through a folder tree and searches for files
with a certain file extension (such as .pdf or .jpg).

Copy these files from whatever location they are in to a new folder.
'''

import os,shutil

rutaACaminar = str(input('Inserte una dirección absoluta a recorrer: ' ))
usuario = str(input('Ingrese su nombre de usuario: ' ))

for foldername,subfolders,filenames in os.walk(rutaACaminar):
    if len(filenames) != 0:
        for archivo in filenames:
            if archivo.endswith('.pdf') | archivo.endswith('jpg'):
                shutil.copy(foldername +'\\'+ archivo,fr'C:\Users\{usuario}\Desktop\CopiasCreadas')
        
    
#fr sirve para combinar strings junto con un string raw.
