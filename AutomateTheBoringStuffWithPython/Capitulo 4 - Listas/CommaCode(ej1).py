'''Ejercicio 1 - Comma Code:

Say you have a list value like this:

spam = ['apples', 'bananas', 'tofu', 'cats']

Write a function that takes a list value as an argument and returns a
string with all the items separated by a comma and a space, with 'and' inserted
before the last item.

For example, passing the previous spam list to the function would return 'apples,
bananas, tofu, and cats'.

But your function should be able to work with any list value passed to it.
Be sure to test the case where an empty list [] is passed to your function.
'''

def comma(lista):
    lista.insert(3,'and') #if the index is bigger than the length of your list, the item will just be appended.
    print("'", end='')
    if len(lista)==1:
        print(lista[0],end="'")
    else:
        for i in range(0,len(lista)):
            if(i!=len(lista)-1):
                print(lista[i] + ',',end=' ') #el end te dice con que termina(por default salto de linea)
            else:
                print(lista[i], end='')
        print ("'")
    
        
        

#spam = []
spam = ['apples', 'bananas', 'tofu', 'cats']
comma(spam)



#Usando .join():
'''
def comma(lista):
    lista.insert(3,'and')
    print(', '.join(spam))
        
        
spam = ['apples', 'bananas', 'tofu', 'cats']
comma(spam)

'''

