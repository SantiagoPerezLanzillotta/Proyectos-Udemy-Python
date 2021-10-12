#Ejercicio 1: PDF Paranoia

'''
Using the os.walk() function from Chapter 10, write a script that will go
through every PDF in a folder (and its subfolders) and encrypt the PDFs
using a password provided on the command line.

Save each encrypted PDF with an _encrypted.pdf suffix added to the original
filename.

Before deleting the original file, have the program attempt to read and
decrypt the file to ensure that it was encrypted correctly.

Then, write a program that finds all encrypted PDFs in a folder (and its
subfolders) and creates a decrypted copy of the PDF using a provided password.

If the password is incorrect, the program should print a message to the user
and continue to the next PDF.

'''
from enum import Flag
import PyPDF2
import os
import sys
import re
import send2trash



def encriptarPdfs():
    regex = re.compile('((.*).pdf$)')
    directorio = input('Ingrese dirección de la carpeta a encriptar PDF: ')
    continuar = input(f'El siguiente directorio y sus subfolders con PDFs serán encriptados {directorio} . ¿Quiere continuar? Si o No ')
    contrasena = str(input('Ingrese contraseña para encriptar los PDFs: '))
    if (os.path.exists(directorio)) & (continuar.lower()=='si'):
        

        for folder, subfolder, filenames in os.walk(directorio):
            for elem in filenames:
                matches = regex.findall(elem)
                #print(matches)
                if len(matches)>0:
                    os.chdir(folder)
                    pdfFile=open(matches[0][0],'rb')
                    readerPDF=PyPDF2.PdfFileReader(pdfFile)
                    if readerPDF.isEncrypted==False:
                        nuevoPDF=PyPDF2.PdfFileWriter() #acá voy a trabajar sobre el nuevo pdf

                        for pageNum in range(readerPDF.numPages): #copio las paginas de un pdf al nuevo
                            page = readerPDF.getPage(pageNum)
                            nuevoPDF.addPage(page)

                        nuevoPDF.encrypt(contrasena)
                        output=open(matches[0][1] +'_encrypted.pdf','wb')
                        nuevoPDF.write(output) #escribo el nuevo pdf

                        try:
                            chequeoLecturaEncriptado = open(matches[0][1] +'_encrypted.pdf','rb')
                            reader = PyPDF2.PdfFileReader(chequeoLecturaEncriptado)
                            print('El encriptado ha fallado')
                        

                        except:
                            print('Encriptado Correctamente')
                        
                            chequeoLecturaEncriptado.close()
                            output.close()
                            pdfFile.close()
                            send2trash.send2trash(elem) #lo mando a la papelera, tambien se podria hacer delete y eliminarlos permanentemente
                    else:
                        continue
                    
                

encriptarPdfs()




