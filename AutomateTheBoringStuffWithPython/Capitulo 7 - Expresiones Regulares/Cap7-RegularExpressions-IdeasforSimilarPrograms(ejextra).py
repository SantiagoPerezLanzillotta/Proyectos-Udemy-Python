#Ejercicio extra: Ideas for Similar Programs

'''

Identifying patterns of text (and possibly substituting them with
the sub() method) has many different potential applications.
For example, you could:

1-Find website URLs that begin with http:// or https://.

2-Clean up dates in different date formats (such as 3/14/2019, 03-14-2019,
and 2015/3/19) by replacing them with dates in a single, standard format.

3-Remove sensitive information such as Social Security or credit card numbers.

4-Find common typos such as multiple spaces between words,
accidentally accidentally repeated words,
or multiple exclamation marks at the end of sentences.


'''
#1-
import pyperclip
import re
import pprint

def url(string):
    regex = re.compile(r'''(

    (http://[^\s\n]+) |
    (https://[^\s\n]+)

    )''',re.VERBOSE) #matchea todo menos espacios y saltos de linea

    Links= []

    extractedLinks = regex.findall(string)
    for i in extractedLinks:
        Links.append(i[0])
    return Links



#string = 'https://vacunatepba.gba.gob.ar o http://youtube.com'

pprint.pprint(url(pyperclip.paste()))



#2- 3/14/2019, 03-14-2019, and 2015/3/19)
import re
import pyperclip
import pprint
import copy

def cleanDates(string):
    regex = re.compile(r'''(
\d*\d/\d\d/\d\d\d\d  |

\d\d\d\d/\d*\d/\d\d  |
\d*\d-\d\d-\d\d\d\d

)''',re.VERBOSE)


    fechasMDA = regex.findall(string)
    #print(f'FECHAS MDA{fechasMDA}')
    
    arregladasMDA = []
    for fechabuena in fechasMDA:

        ordenoElem =[]

        
        if len(fechabuena) == 9:     #acá tengo la primera y segunda opcion, pues
            
            if str(fechabuena[6]) == '/':
                dia = fechabuena[7:]    
                mes= list(fechabuena[5]) 
                anio = fechabuena[0:4]    
                mes.insert(0,'0')
                mesarreglado =''.join(mes)

                ordenoElem.append(dia)
                ordenoElem.append(mesarreglado)
                ordenoElem.append(anio)

                arreglada='/'.join(ordenoElem)
                
                arregladasMDA.append(arreglada) #agrego a la lista definitiva

            else:
                dia = fechabuena[2:4]    #como no estoy agarrando las /
                mes= list(fechabuena[0]) #con el join de abajo del final de la condicion
                anio = fechabuena[5:]    #uno el dia mes y año con el /
                mes.insert(0,'0')
                mesarreglado =''.join(mes)
                #print(mesarreglado)

                ordenoElem.append(dia)
                ordenoElem.append(mesarreglado)
                ordenoElem.append(anio)

                arreglada='/'.join(ordenoElem)
                
                arregladasMDA.append(arreglada) #agrego a la lista definitiva

        else:
            if str(fechabuena[7]) == '/':
                dia = fechabuena[8:]
                mes= list(fechabuena[5:7])
                anio = fechabuena[0:4]
                
                ordenoElem.append(dia)
                ordenoElem.append(mesarreglado)
                ordenoElem.append(anio)

                arreglada='/'.join(ordenoElem)

                arregladasMDA.append(arreglada) #agrego a la lista definitiva

            else:
                 dia = fechabuena[3:5]
                 mes = fechabuena[0:2]
                 anio = fechabuena[6:]

                 ordenoElem.append(dia)
                 ordenoElem.append(mes)
                 ordenoElem.append(anio)

                 arreglada='/'.join(ordenoElem)
                 arregladasMDA.append(arreglada)


    stringFinal = string
    #print(fechasMDA)
    for i in range(0,len(arregladasMDA)):
       reemplazo = stringFinal.replace(fechasMDA[i],arregladasMDA[i])
       stringFinal=reemplazo
       #print(id(reemplazo[0]))

    return stringFinal



pprint.pprint(cleanDates('93-14-2019 pero el 3/14/2019 en 2005/5/20 y 2006/06/21'))



#3-
import re
import pyperclip
import pprint
import copy

def ocultarInfo(string):
    regex = re.compile(r'''(
\d\d\d\d\d(\d\d\d)
)''',re.VERBOSE)

    codigosTarjetas = regex.findall(string)

    devuelvoString = regex.sub(r'\2****',string)

    return devuelvoString

print(ocultarInfo('12345678 fiesta 15846897'))
    

    
'''       
4-Find common typos such as multiple spaces between words,
accidentally accidentally repeated words,
or multiple exclamation marks at the end of sentences.
'''
#4-
import re
def erroresEncontrados(string):
    regex=re.compile(r'''(
\s{2,} |
(\b\w+)\s+\2       #el (\2) indica que se fija si es igual al grupo 2 o sea (\w+)




)''',re.VERBOSE)

    lista=regex.findall(string)

    arregloLista = []
    for i in lista:
        arregloLista.append(i[0])

    if len(arregloLista) != 0:
        print(f'He encontrado los siguientes errores {arregloLista}')
    else:
        print('No hay errores')

erroresEncontrados('hola   hola    amigo')

        
            
            
    
    



















    






