import re
import logging

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')
logging.disable(logging.CRITICAL)

def resolverWordSearch(string,ancho,alto,palabrasABuscar):
    listaPorLetra= pasarALista(string)
    if len(listaPorLetra)== ancho*alto:
        matriz = armoMatriz(listaPorLetra,ancho,alto)
        #logging.debug('La Matriz queda:%s'%(matriz))
        encontrados = []
    
        for palabra in palabrasABuscar:
            for i in range(0,len(matriz)):
                for y in range(0,ancho):
                    if matriz[i][y] == palabra[0]:
                        DU = buscoDiagonalUP(matriz,palabra,i,y,ancho,alto) #done
                        DER = buscoDERECHA(matriz,palabra,i,y,ancho,alto) #done
                        DDER = buscoDiagonalDOWNDER(matriz,palabra,i,y,ancho,alto) #done
                        D = buscoDOWN(matriz,palabra,i,y,ancho,alto) #done
                        IZQD = buscoDiagonalDOWNIQZ(matriz,palabra,i,y,ancho,alto) #done
                        IZQ = buscoIZQUIERDA(matriz,palabra,i,y,ancho,alto) #done
                        IZQU = buscoDiagonalUPIZQ(matriz,palabra,i,y,ancho,alto) #done
                        U = buscoUP(matriz,palabra,i,y,ancho,alto) #done

                        if DU==True:
                            encontrados.append((palabra,'DiagonalUP',i,y))
                        elif DER==True:
                            encontrados.append((palabra,'DERECHA',i,y))
                        elif DDER==True:
                            encontrados.append((palabra,'DiagonalABAJODER',i,y))
                        elif D==True:
                            encontrados.append((palabra,'ABAJO',i,y))
                        elif IZQD==True:
                            encontrados.append((palabra,'DiagonalABAJOIQZ',i,y))
                        elif IZQ==True:
                            encontrados.append((palabra,'IZQUIERDA',i,y))
                        elif IZQU==True:
                            encontrados.append((palabra,'DiagonalARRIBAIZQ',i,y))
                        elif U==True:
                            encontrados.append((palabra,'ARRIBA',i,y))
        print(encontrados)   
        

    else:
        print('La cantidad de letras insertadas no son correctas')



def buscoDiagonalUPIZQ(matriz,palabra,coordenadaI,coordenadaY,ancho,alto): 
    respuesta = True
    if (coordenadaY-len(palabra)>=-1) & (coordenadaI-len(palabra)>=-1):   
        for i in range(0,len(palabra)):   
            if palabra[i] == matriz[coordenadaI-i][coordenadaY-i]:
                continue
            else:
                return False
        return respuesta
    return False

def buscoDiagonalDOWNIQZ(matriz,palabra,coordenadaI,coordenadaY,ancho,alto): 
    respuesta = True
    if (coordenadaI+len(palabra)<=alto) & (coordenadaY-len(palabra)>=-1):   
        for i in range(0,len(palabra)):   
            if palabra[i] == matriz[coordenadaI+i][coordenadaY-i]:
                continue
            else:
                return False
        return respuesta
    return False


def buscoDiagonalDOWNDER(matriz,palabra,coordenadaI,coordenadaY,ancho,alto): 
    respuesta = True
    if (coordenadaI+len(palabra)<=alto) & (coordenadaY+len(palabra)<=ancho):   
        for i in range(0,len(palabra)):   
            if palabra[i] == matriz[coordenadaI+i][coordenadaY+i]:
                continue
            else:
                return False
        return respuesta
    return False



def buscoDiagonalUP(matriz,palabra,coordenadaI,coordenadaY,ancho,alto): 
    respuesta = True
    if (coordenadaI-len(palabra)>=-1) & (coordenadaY+len(palabra)<=ancho):   
        for i in range(0,len(palabra)):   
            if palabra[i] == matriz[coordenadaI-i][coordenadaY-i]:
                continue
            else:
                return False
        return respuesta
    return False



def buscoDOWN(matriz,palabra,coordenadaI,coordenadaY,ancho,alto): 
    respuesta = True
    if coordenadaI+len(palabra)<=alto:   
        for i in range(0,len(palabra)):   
            if palabra[i] == matriz[coordenadaI+i][coordenadaY]:
                continue
            else:
                return False
        return respuesta
    return False


def buscoUP(matriz,palabra,coordenadaI,coordenadaY,ancho,alto): 
    respuesta = True
    if coordenadaI-len(palabra)>=-1:   
        for i in range(0,len(palabra)):   
            if palabra[i] == matriz[coordenadaI-i][coordenadaY]:
                continue
            else:
                return False
        return respuesta
    return False

   
def buscoDERECHA(matriz,palabra,coordenadaI,coordenadaY,ancho,alto):
    respuesta = True
    if coordenadaY+len(palabra)<=ancho:   
        for i in range(0,len(palabra)):   
            if palabra[i] == matriz[coordenadaI][coordenadaY+i]:
                continue
            else:
                return False
        return respuesta
    return False

def buscoIZQUIERDA(matriz,palabra,coordenadaI,coordenadaY,ancho,alto):
    respuesta = True
    if coordenadaY-len(palabra)<-1:       
        return False
    else:
        for i in range(0,len(palabra)):   
            if palabra[i] == matriz[coordenadaI][coordenadaY-i]:
                continue
            else:
                return False
        return respuesta



def pasarALista(string): #de esta manera evito que cuente el caracter de salto "\n"
    lista = []
    regex = re.compile('[a-zA-Z]')
    for i in string:        
        if len(regex.findall(i))>0:
            lista.append(i)        
    return lista



def armoMatriz(lista,ancho,alto):
    matriz = []
    elemento = 0
    for i in range(0,alto):
        llenoLista = []
        for y in range(0,ancho):
            llenoLista.append(lista[elemento])
            elemento+=1
        matriz.append(llenoLista)
        
    
    return matriz
        
        
    
    
    




ancho = int(input('Ingrese ancho del tablero: '))
alto = int(input('Ingrese alto del tablero: '))
palabrasABuscar = ['jasmine','merida','snowwhite','ariel','cinderella','anna','rapunzel','pocahontas','elsa','tiana','aurora','vanellope','belle','mulan']
resolverWordSearch('''
leleznuparcn
aelnsaeenpil
vailnulaionh
aerrensmecdm
aoenabahsaev
auroraenohra
adiremoaeoen
baeetwzarnle
mlnnwenomtll
pethinlacaal
llieamaaasmo
etljeasmlrap
ertianaaslee
nlmulanojalo
''',ancho,alto,palabrasABuscar)
