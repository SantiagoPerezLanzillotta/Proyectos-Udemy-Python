#Ejercicio 2: Deleting Unneeded Files
'''
It’s not uncommon for a few unneeded but humongous files or folders to take up
the bulk of the space on your hard drive.If you’re trying to free up room on
your computer, you’ll get the most bang for your buck by deleting the
most massive of the unwanted files. But first you have to find them.

Write a program that walks through a folder tree and searches
for exceptionally large files or folders —say, ones that have a
file size of more than 100MB.

(Remember that to get a file’s size, you can use
os.path.getsize() from the os module.)

Print these files with their absolute path to the screen.
'''
#100 megas = 104857600 Bytes (in binary)
import os
import pprint
directorioARecorrer = str(input('Ingrese la dirección absoluta del directorio a recorrer: '))

archivosGrandes = []
for folder, subfolders, filenames in os.walk(directorioARecorrer):
    for archivo in filenames:
        direccion= folder + '\\' + archivo
        if (os.path.getsize(direccion)>104857600):
            archivosGrandes.append(archivo)
            print(f'Deleting: {archivo}')

pprint.pprint(f'Los siguientes archivos fueron borrados {archivosGrandes}')



