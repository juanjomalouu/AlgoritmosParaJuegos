
def laberintoVA(tab, iniX, iniY, casillasVisitadas, casillasTotales):
    if iniX == len(tab)-1 and iniY == len(tab)-1 and casillasVisitadas == casillasTotales:
        esSol = True
    else:
        esSol = False
        nextMove = [[1,0],[0,1],[-1,0],[0,-1]]
        i = 0
        while not esSol and i < len(nextMove):
            if esFactible(tab, iniX+nextMove[i][0], iniY+nextMove[i][1]):
                tab[ iniX+nextMove[i][0]][iniY+nextMove[i][1]] = -1
                esSol, casillasVisitadas = laberintoVA(tab,  iniX+nextMove[i][0], iniY+nextMove[i][1], casillasVisitadas+1, casillasTotales)
                if not esSol:
                    tab[ iniX+nextMove[i][0]][iniY+nextMove[i][1]] = 0
            i+=1
    return esSol, casillasVisitadas
def esFactible(tab, iniX, iniY):
    return 0 <= iniX < len(tab) and 0 <= iniY < len(tab)

if __name__ == "__main__":
    N =int(input())
    tab = list()
    for i in range(N):
        tab.append(list(map(int,input().strip().split())))
    casillasVisitables = 0
    for i in range(N):
        for j in range(N):
            if tab[i][j] == 0:
                casillasVisitables +=1
    tab[0][0] = -1
    esSol, casillas = laberintoVA(tab, 0, 0, 1, casillasVisitables)
    print(casillas)
    print(esSol)