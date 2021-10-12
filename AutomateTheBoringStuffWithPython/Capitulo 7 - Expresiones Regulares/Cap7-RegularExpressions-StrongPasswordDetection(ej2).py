#Ejercicio 2:Strong Password Detection
'''


Write a function that uses regular expressions to make sure the password
string it is passed is strong.

A strong password is defined as one that:
is at least eight characters long,
contains both uppercase and lowercase characters,
and has at least one digit.

You may need to test the string against
multiple regex patterns to validate its strength.

'''

import re

def strongPass(string): 
    regex = re.compile(r'''(
(?=.*[A-Z])         #si tiene mayusculas
(?=.*[a-z])         #si tiene minusculas
(?=.*[0-9])         #si tiene digitos
[A-Za-z0-9_#@%\*\-] #matchea todos estos caracteres
{8,}                #con la condición que el tamaño sea 8 minimo
  ) ''',re.VERBOSE)


    match = regex.findall(string)
    print(match)
    if len(match) != 0:
        return True
    else:
        return False


string = 'AvgaGTB1' #valido
mayusc = '9AAAAAAA'
Amayusc='aaaaaaaA'
novalido = 'aaa98972' #invalido
print(strongPass(novalido))


