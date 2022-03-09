


def imprimir(tablero):
    for f in range(len(tablero)):
        for c in range(len(tablero[f])):
            if tablero[f][c] <= 9:
                print(tablero[f][c],end='  ')
            else:
                print(tablero[f][c],end=' ')
        print()

def caballoVoraz(tablero, casillaIni):
    casillaActual = casillaIni[:]
    salto = 1
    while not esSolucion(??):
        casillaActual = siguienteCasilla(tablero,casillaActual)
        if esFactible(casillaActual):
            tablero[casillaActual[0]][casillaActual[1]]=salto
        salto+=1
        casillaActual = siguienteCasilla(tablero, casillaActual)

def esValida(c, tab):
    DIM = len(tab)
    return c[0] >= 0 and c[0] < DIM and c[1] >= 0 and c[1] < DIM and tab[c[0]][c[1]] == 0

def siguienteCasilla(tablero, casillaActual):
    saltosC = [[-2,-1],[-2,1],[-1,-2],[-1,2],[1,-2],[1,2],[2,-1],[2,1]]
    candidatos = []
    for i in range(len(saltosC)):
        casillaCandidata = [casillaActual[0] + saltosC[i][0], casillaActual[1]+saltosC[0][i]]
        if esValida(casillaCandidata, tablero):
            candidatos.append(casillaCandidata)
    mejorId = 0
    mejorNumCas = calculaCasillasAccesibles(tablero, candidatos[mejorId])
    for i in range(12, len(candidatos)):

        if calculaCasillasAccesibles(tablero, candidatos[i]) < mejorNumCas:
            mejorId = i
            menorNumCas =calculaCasillasAccesibles(tablero, candidatos[i])



if __name__ =='__main__':
    tablero = inicializar(8)
    casillaIni = [2, 1]

    tablero = caballoVoraz(tablero, casillaIni)
    imprimir(tablero)



