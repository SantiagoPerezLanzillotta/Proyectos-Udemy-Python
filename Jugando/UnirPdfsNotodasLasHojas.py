'''
Este programa agarra 2 pdfs, y une las páginas que el usuario le pasa para tener 1 solo pdf final
con la combinación de las páginas de los 2 pdfs.

(nótese que cada pdf puede empezar en cualquier página y abarcar el rango que el usuario quiera)
'''

import PyPDF2,os

direccionPDF1 = input('Ingrese dirección del primer PDF: ')
desdePDF1=int(input('Ingrese desde donde quiere copiar las hojas (PDF1): '))
hastaPDF1=int(input('Ingrese hasta donde (incluido) quiere copiar las hojas (PDF1): '))


direccionPDF2 =input('Ingrese dirección del segundo PDF: ')
desdePDF2=int(input('Ingrese desde donde quiere copiar las hojas (PDF2): '))
hastaPDF2=int(input('Ingrese hasta donde (incluido) quiere copiar las hojas (PDF2): '))

if os.path.exists(direccionPDF1) & os.path.exists(direccionPDF2):    

    fileObjectPDF1 = open(direccionPDF1,'rb')
    readerPDF1 = PyPDF2.PdfFileReader(direccionPDF1)

    fileObjectPDF2 = open(direccionPDF2,'rb')
    readerPDF2 = PyPDF2.PdfFileReader(direccionPDF2)

    
    writer = PyPDF2.PdfFileWriter()   #acá voy a escribir

    if desdePDF1<0 | desdePDF2<0 | hastaPDF2>readerPDF2.getNumPages() | hastaPDF1>readerPDF1.getNumPages():
        print('Ha ingresado mal el rango de las páginas')
    else:
        for page in range(desdePDF1-1,hastaPDF1):
            pagina = readerPDF1.getPage(page)
            writer.addPage(pagina)
        
        for page in range(desdePDF2-1,hastaPDF2):
            pagina = readerPDF2.getPage(page)
            writer.addPage(pagina)

        outputFile = open('NuevoPDF.pdf','wb')
        writer.write(outputFile)
        outputFile.close()
        fileObjectPDF2.close()
        fileObjectPDF1.close()
        print(os.getcwd())
else:
    print('Error en existencia de directorios')

