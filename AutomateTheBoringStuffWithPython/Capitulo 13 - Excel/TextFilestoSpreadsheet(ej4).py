#Ejercicio 4: Text Files to Spreadsheet

'''
Write a program to read in the contents of several text files (you can make
the text files yourself) and insert those contents into a spreadsheet,
with one line of text per row. The lines of the first text file will be
in the cells of column A, the lines of the second text file
will be in the cells of column B, and so on.

Use the readlines() File object method to return a list of strings, one string
per line in the file.

For the first file, output the first line to column 1, row 1.
The second line should be written to column 1, row 2, and so on.

The next file that is read with readlines() will be written to column 2,
the next file to column 3, and so on.
'''
import openpyxl

termino = False
listaFiles =[]
file1 = input('Ingrese dirección del archivo de texto: ')

listaFiles.append(file1)


while True:
    respuesta= input('Desea seguir agregando archivos de texto?')
    if respuesta.lower()=='no':        
        break
    else:
        file = input('Ingrese dirección del archivo de texto: ')
        listaFiles.append(file)

wb=openpyxl.Workbook()

sheet = wb.worksheets[0]

for i in range(0,len(listaFiles)):
    file = open(listaFiles[i])
    listaLinea = file.readlines()
    #print(listaLinea)

    for y in range(0,len(listaLinea)):
        sheet.cell(row=y+1,column=i+1).value = listaLinea[y]
    file.close()

wb.save('TextosLineas.xlsx')
    

        
        
                     
    
