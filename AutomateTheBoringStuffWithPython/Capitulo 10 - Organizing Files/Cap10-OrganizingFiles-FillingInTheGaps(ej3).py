#Ejercicio 3: Filling in the Gaps

'''
Write a program that finds all files with a given prefix,
such as spam001.txt, spam002.txt, and so on,
in a single folder and locates any gaps in the numbering
(such as if there is a spam001.txt and spam003.txt but no spam002.txt).
Have the program rename all the later files to close this gap.

As an added challenge, write another program that can insert gaps.
into numbered files so that a new file can be added.

prefix = lo de adelante
'''
import os,re,shutil

#función auxiliar
def cambioDigito(string):
    numero=int(string)
    numero+=1
    lista=list(str(numero))
    while len(lista)<len(string):
        lista.insert(0,'0')
    respuesta= ('').join(lista)    
    
    return respuesta


#Acá abajo función principal
ciclo=False

while ciclo==False:
    carpeta = str(input('Ingrese dirección absoluta de la carpeta: '))
    if os.path.exists(carpeta):
        ciclo=True
    else:
        print('La dirección no existe, intente de nuevo')
    
prefix = str(input('Ingrese prefijo del archivo: '))

regex = re.compile(prefix + r'\d{1,}.\w+')

listaTodosLosArchivos = []

for file in os.listdir(carpeta):      #junto todos los archivos
    if os.path.isfile(carpeta + '\\' + file):
        listaTodosLosArchivos.append(file)


listaArchivosConPrefijo = []

for elemento in listaTodosLosArchivos: #busco los archivos que cumplen el prefijo
    matcheo = regex.findall(elemento)
    if len(matcheo)>0:
        listaArchivosConPrefijo.append(matcheo[0])



if len(listaArchivosConPrefijo)>0:
    contadorHastaPunto = -1               #me guardo el indice del ultimo numero
    archivo = listaArchivosConPrefijo[0] 
    for i in range(0,len(archivo)):
        if archivo[i] != '.':
            contadorHastaPunto+=1
        else:
            break

    
    listaArchivosConPrefijo.sort() #ordeno pues no puedo asumir que viene en orden
    hayGAP = False #con false no hay gap    
    GAP=1
    for i in range(0,len(listaArchivosConPrefijo)): #chequeo que los numeros que siguen se incrementen en 1
        elemento = listaArchivosConPrefijo[i]
        if int(elemento[len(prefix):contadorHastaPunto+1]) == GAP: #int(001)==1 ->true
            GAP +=1
        else:
            hayGAP=True
            break


    if hayGAP==True:
        digitos = '001'
        sufijo = contadorHastaPunto + 1
        
        parteFinal=elemento[sufijo:]
        for elemento in listaArchivosConPrefijo:
            
            
            shutil.move(carpeta+'\\'+elemento,carpeta+'\\'+prefix+digitos+parteFinal)
            digitos = cambioDigito(digitos)
            

        


    


#print(contadorHastaPunto)
#print(hayGAP)
#print(listaArchivosConPrefijo)
#print(digitos)



    
    
