#Ejercicio 3: Regex Version of the strip() Method

'''
Write a function that takes a string and does the same thing as the
strip() string method. If no other arguments are passed other than
the string to strip, then whitespace characters will be removed from the
beginning and end of the string.

Otherwise, the characters specified in the second argument to the function
will be removed from the string.

'''

import re

def regexVersion(string,remov=None):

    if remov != None:
        regex = re.compile(remov)
        regex.findall(string)
        return regex.sub('',string)
    else:
        regex = re.compile(r'''(
^\s+ |  #empieza con 2 espacios o mas O
\s+$    #termina con 2 espacios o mas
    
)''',re.VERBOSE)
        
        lista = regex.findall(string)
        stringNuevo = regex.sub('',string)
        #print(id(stringNuevo))
        return stringNuevo
        



string = '   Quiero borrar Rs    '
print(regexVersion(string))

