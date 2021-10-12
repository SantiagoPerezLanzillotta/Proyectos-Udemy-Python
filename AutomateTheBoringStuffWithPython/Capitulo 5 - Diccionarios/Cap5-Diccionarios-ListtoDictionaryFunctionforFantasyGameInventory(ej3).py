''' Ejercicio 3: - List to Dictionary Function for Fantasy Game Inventory

Imagine that a vanquished dragon’s loot is represented as a list of strings like
this:
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

Write a function named addToInventory(inventory, addedItems), where the
inventory parameter is a dictionary representing the player’s inventory
(like in the previous project) and the addedItems parameter is a list like
dragonLoot.
The addToInventory() function should return a dictionary that represents the
updated inventory. Note that the addedItems list can contain multiples of the
same item.
Your code could look something like this:

def addToInventory(inventory, addedItems):
    # your code goes here

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)

'''
import pprint

def addToInventory(inventory, addedItems):
    # your code goes here
    listaKeys = inventory.keys()
    for elemento in addedItems:
        
        if elemento not in listaKeys:
            inventory.setdefault(elemento,0)
        else:
            inventory[elemento]+=1
    return inventory



def displayInventory(inv):
    pprint.pprint(dict(inv))


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby','agua','fuego','fiesta','vida'] #tengo 3 gold coins


inv = addToInventory(inv, dragonLoot)
displayInventory(inv)

