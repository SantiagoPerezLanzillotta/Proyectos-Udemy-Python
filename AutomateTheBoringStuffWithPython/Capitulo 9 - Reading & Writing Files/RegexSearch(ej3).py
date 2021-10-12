#Ejercicio 3: Regex Search

'''
Write a program that opens all .txt files in a folder and searches for any
line that matches a user-supplied regular expression.

The results should be printed to the screen.

'''
import re, os, pprint

carpetaUser = str(input('Ingrese dirección absoluta de la carpeta: '))
regularExpUser= str(input('Ingrese expresion regular: '))


regex = re.compile(regularExpUser)

for filename in os.listdir(carpetaUser):
    if filename.endswith('.txt'):
        direccionArchivoTexto = carpetaUser + "\\" + filename
        objetoTexto = open(direccionArchivoTexto)
        textoArchivo = objetoTexto.read()

        #busco el texto
        listaMatches = regex.findall(textoArchivo)
        
        #Imprimo
        pprint.pprint(f'{listaMatches} en {direccionArchivoTexto}')
        
