import numpy as np


def inicializarTablero(dim):
    tablero = np.zeros([dim, dim], dtype = int)
    return tablero

def nReinasVA(tab,fil):
    if fil == np.size(tab,0):
        esSol = True
    else:
        esSol = False
        col = 0
        while not esSol and col < np.size(tab,1):
            if EsFactible(tab,fil,col):
                tab[fil,col] = 1
                [tab, esSol] = nReinasVA(tab,fil+1)
                if not esSol:
                    tab[fil, col] = 0
            col += 1
    return  tab,esSol

def EsFactible(tab,f,c):
    colOk = np.max(tab[:,c]) == 0 # Columna:
    diag1Ok = True #Diagonal Principal
    indF = f-1
    indC = c-1
    while diag1Ok and indF >= 0 and indC >= 0:
        diag1Ok = tab[indF, indC] == 0
        indF -=1
        indC -=1
    diag2Ok =True
    indF = f-1
    indC = c+1
    while diag2Ok and indF >= 0 and indC < np.size(tab,1):
        diag2Ok = tab[indF, indC] == 0
        indF -=1
        indC +=1
    return colOk and diag2Ok and diag1Ok


tablero = inicializarTablero(8)
[tablero, esSol] = nReinasVA(tablero,0)
if esSol:
    print(tablero)
else:
    print('No se ha encontrado solución')

