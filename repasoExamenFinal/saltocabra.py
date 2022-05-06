
def esSolucion(tab):
    esSol = True
    for i in range(len(tab)-1):
        for j in range(len(tab[0])-1):
            if (tab[i][j]) != -1:
                esSol = False
    return esSol


def cabraBT(tab, iniX, iniY, delante, lado):
    if esSolucion(tab):
        esSol = True
    else:
        esSol = False
        nextMov = [[delante, lado], [-delante,lado], [delante, -lado], [-delante, -lado], [lado, delante], [-lado, delante], [lado, -delante], [-lado, -delante]]
        i = 0
        while i < len(nextMov) and not esSol:
            if esFactible(tab, iniX + nextMov[i][0], iniY + nextMov[i][1]):
                #iniX, iniY = actualizarIndices(tab, iniX+ nextMov[i][0], iniY + nextMov[i][1])
                tab[iniX + nextMov[i][0]][ iniY + nextMov[i][1]] = -1
                esSol = cabraBT(tab, iniX + nextMov[i][0],  iniY + nextMov[i][1], delante, lado)
                if not esSol:
                    tab[iniX + nextMov[i][0]][ iniY + nextMov[i][1]] = 0
            i+=1
    return esSol


def esFactible(tab, iniX, iniY):
    return 0 <= iniX < len(tab) and 0 <= iniY < len(tab) and tab[iniX][iniY] == 0

if __name__ == "__main__":
    N,M,delante,lado = list(map(int,input().strip().split()))
    iniX, iniY = list(map(int,input().strip().split()))

    tablero = list()
    for i in range(N):
        newList = [0] * M
        tablero.append(newList)

    tablero[iniX][iniY] = -1
    esSol = cabraBT(tablero, iniX, iniY, delante, lado)
    print(esSol)