
def esFactible(tab, xNew, yNew, idObjActual, P):
    return 0 <= xNew < len(tab) and 0 <= yNew < len(tab[0]) and tab[xNew][yNew] != -1 and tab[xNew][yNew] <= P and (tab[xNew][yNew]== 0 or tab[xNew][yNew] == idObjActual+1)

def algoritmoBT(tab, xIni, yIni, casillasRecorridas, idObjActual, P, mejorSolActual):
    if xIni <= len(tab)-1 and yIni <= len(tab[0])-1 and idObjActual == P:
        esSol = True
        if casillasRecorridas < mejorSolActual:
            mejorSolActual = casillasRecorridas
    else:
        esSol = False
        nextMov = [[0,1],[1,0],[-1,0],[0,-1]]
        for i in range(len(nextMov)):
            xNew = xIni + nextMov[i][0]
            yNew = yIni + nextMov[i][1]
            if esFactible(tab, xNew, yNew, idObjActual, P):
                casillaFutura = tab[xNew][yNew]
                cogido = False
                if casillaFutura == idObjActual+1:
                    idObjActual+=1
                    cogido = True
                tab[xNew][yNew] = -1
                esSol, tab, mejorSolActual = algoritmoBT(tab, xNew, yNew, casillasRecorridas+1, idObjActual, P, mejorSolActual)
                tab[xNew][yNew] = casillaFutura
                if cogido:
                    idObjActual-=1
    return esSol, tab, mejorSolActual

if __name__ == "__main__":
    N, M, P = list(map(int,input().strip().split()))
    tab = list()
    for i in range(N):
        tab.append(list(map(int,input().strip().split())))
    objCogidos = 0
    if tab[0][0] == 1:
        objCogidos = 1
    tab[0][0] = -1
    esSol, tab, mejorSol = algoritmoBT(tab, 0, 0, 1, objCogidos, P, float('inf'))
    print(mejorSol)