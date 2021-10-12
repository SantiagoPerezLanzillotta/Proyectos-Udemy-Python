#Ejercicio 2: Mad Libs 
'''
Create a Mad Libs program that reads in text files and lets the user add
their own text anywhere the word ADJECTIVE, NOUN, or VERB
appears in the text file. For example, a text file may look like this:

The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
unaffected by these events.


The program would find these occurrences and prompt the user to replace them.

Enter an adjective:
silly
Enter a noun:
chandelier
Enter a verb:
screamed
Enter a noun:
pickup truck


The following text file would then be created:

The silly panda walked to the chandelier and then screamed. A nearby pickup
truck was unaffected by these events.

The results should be printed to the screen and saved to a new text file.
'''

import re


direccionArchivoTexto = str(input('Ingrese la dirección donde se encuentre el texto: '))
adjectivesUser = str(input('Ingrese un Adjetivo: '))
nounsUser = str(input('Ingrese un Noun: '))
verbsUser = str(input('Ingrese un Verb: '))

objetoArchivo = open(direccionArchivoTexto)
textoArchivo = objetoArchivo.read()

regexADJECTIVE = re.compile('ADJECTIVE')
matchAdjectives = regexADJECTIVE.findall(textoArchivo)

regexNOUN = re.compile('NOUN')
matchNoun = regexNOUN.findall(textoArchivo)

regexVERB = re.compile('VERB')
matchVerb = regexVERB.findall(textoArchivo)

textoNuevo = textoArchivo

for i in matchAdjectives:
    textoNuevo = textoNuevo.replace(i,adjectivesUser)
    textoArchivo = textoNuevo

for i in matchNoun:
    textoNuevo = textoNuevo.replace(i,nounsUser)
    textoArchivo = textoNuevo

for i in matchVerb:
    textoNuevo = textoNuevo.replace(i,verbsUser)
    textoArchivo = textoNuevo


objetoArchivoNuevo = open(input('Ingrese PATH absoluto donde se guardará el archivo: '+'\\nuevo.txt'),'w') #windows
objetoArchivoNuevo.write(textoArchivo)

objetoArchivo.close()
objetoArchivoNuevo.close()

print(textoNuevo)



