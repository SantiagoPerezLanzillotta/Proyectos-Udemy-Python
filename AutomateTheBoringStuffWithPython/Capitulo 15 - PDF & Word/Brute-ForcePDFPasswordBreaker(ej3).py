#Ejercicio 3: Brute-Force PDF Password Breaker

'''
Say you have an encrypted PDF that you have forgotten the password
to, but you remember it was a single English word.
Trying to guess your forgotten password is quite a boring task.
Instead you can write a program that will decrypt the PDF by trying
every possible English word until it finds one that works.
This is called a brute-force password attack.

Download the text file dictionary.txt from https://nostarch.com/automatestuff2/.
his dictionary file contains over 44,000 English words with one
word per line.

Using the file-reading skills you learned in Chapter 9,
create a list of word strings by reading this file.

Then loop over each word in this list, passing it to the decrypt()
method.

If this method returns the integer 0, the password was wrong and
your program should continue to the next password.

If decrypt() returns 1, then your program should break out of the
loop and print the hacked password.

You should try both the uppercase and lowercase form of each word.

(On my laptop, going through all 88,000 uppercase and
lowercase words from the dictionary file takes a couple of minutes.
This is why you shouldn’t use a simple English word for your passwords.)

'''
import PyPDF2,re,os

diccionarioIngles = open(input('Ingrese dirección absoluta con el diccionario para desencriptar usando fuerza bruta: ')
PDFDesencriptar = input('Ingrese dirección del PDF a desencriptar: ')

regex = re.compile('\w+')
palabrasIngles = diccionarioIngles.read()

listaPalabras =regex.findall(palabrasIngles)
#print(listaPalabras)

pdf = open(PDFDesencriptar,'rb')
readerPDF= PyPDF2.PdfFileReader(pdf)


for name in listaPalabras:
    respuesta1 = readerPDF.decrypt(name.upper())    
    if respuesta1 == 1:        
        break
    respuesta2 = readerPDF.decrypt(name.lower())
    if respuesta2 == 1:        
        break   
    print(f'{name.upper()} FALLO')
    print(f'{name.lower()} FALLO')

if respuesta1==1:
    print(f'La constraseña era: {name.upper()}')
elif respuesta2==1:
    print(f'La constraseña era: {name.lower()}')
else:
    print('Contraseña no hallada')

pdf.close()
diccionarioIngles.close()
