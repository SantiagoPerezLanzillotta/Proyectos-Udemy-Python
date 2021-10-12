''' Ejercicio 1: Chess Dictionary Validator

In this chapter, we used the
dictionary value {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen',
'3e': 'wking'} 

Write a function named isValidChessBoard() that takes a dictionary argument and
returns True or False depending on if the board is valid.

A valid board will have exactly one black king and exactly one white king.
Each player can only have at most 16 pieces, at most 8 pawns,
and all pieces must be on a valid space from '1a' to '8h'; that is,
a piece can’t be on space '9z'.
The piece names begin with either a 'w' or 'b' to represent white or black,
followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'.

This function should detect when a bug has resulted in an improper chess board.

8
7
6
5
4
3
2
1
  a b c d e f g h

'''



def isValidChessBoard(ChessBoard):
    HayReyes = 'bking' in ChessBoard.values() and 'wking' in ChessBoard.values()

    CantidadCorrecta = cuento((list(ChessBoard.values())))

    PosicionCorrecta = posicion ((list(ChessBoard.keys())))

    PiezasCorrectas = piezas((list(ChessBoard.values())))

    if (HayReyes and CantidadCorrecta and PosicionCorrecta and PiezasCorrectas)==True:
        return True
    else:
        return False



def cuento(lista):
    negro = 0
    blanco = 0

    for i in lista:    
        if i[0]== 'w':
            blanco+=1
        elif i[0]== 'b':
            negro+=1
        else:
            return False

    if negro <=16 and blanco <= 16:
        return True



def posicion(lista):
    for i in lista:
        if len(i)<2 or len(i)>2:
            return False
        elif int(i[0])<0 or int(i[0])>8 or i[1]>'h': #tengo que poner int para que lo compare bien
            return False

    return True



def piezas(lista):
    peonesNegro =  lista.count('bpawns')
    peonesBlanco = lista.count('wpawns')

    if peonesNegro > 8 or peonesBlanco > 8:
        return False
    
    torresNegro = lista.count('brook')
    torresBlanco = lista.count('wrook')
    
    if torresNegro > 2 or torresBlanco > 2:
        return False

    bishopNegro = lista.count('bbishop')
    bishopBlanco = lista.count('wbishop')
    
    if bishopNegro > 2 or bishopBlanco > 2:
        return False

    queenNegro = lista.count('bqueen')
    queenBlanco = lista.count('wqueen')
    
    if queenNegro > 1 or queenBlanco > 1:
        return False

    knightNegro = lista.count('bknight')
    knightBlanco = lista.count('wknight')
    
    if knightNegro > 2 or knightBlanco > 2:
        return False

    return True


spam = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen',
'3e': 'wking'}
print(isValidChessBoard(spam))



    
