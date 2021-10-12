#Ejercicio 2: Blank Row Inserter

'''
Create a program blankRowInserter.py that takes two integers and a filename
string as command line arguments.

Let’s call the first integer N and the second integer M. Starting at row N,
the program should INSERT M blank rows into the spreadsheet. For example, when
the program is run like this:

python blankRowInserter.py 1 2 myProduce.xlsx

BEFORE:
1-prueba   chau  adios buenas  quiero   saludo
2-un      salto  alto   auto    espumas    y
3-fiesta  dormir  con   agua    y      luz

After:
1-
2-
3-prueba   chau  adios buenas  quiero   saludo
4-un      salto  alto   auto    espumas    y
5-fiesta  dormir  con   agua    y     luz
'''

import openpyxl
#from openpyxl.utils import get_column_letter, column_index_from_string
import sys

if len(sys.argv)== 4:
    desde = int(sys.argv[1])
    cantidadAgregar = int(sys.argv[2])
    archivoExcel = sys.argv[3]

    wb=openpyxl.load_workbook(archivoExcel)
    sheet = wb.worksheets[0]

    for i in range(cantidadAgregar):
        sheet.insert_rows(desde)
    wb.save('modificado.xlsx')
    print('Terminado')
else:
    print('Faltan datos: Desde, LineasAAgregar, excel')



 



