
def laberintoVA(lab, Xini, Yini, casillasVisitadas, objetosCogidos, mejorSol):
    if objetosCogidos == numProd and Xini == (len(lab)-1) and Yini == len(lab[0])-1 and casillasVisitadas < mejorSol:
        mejorSol = casillasVisitadas
    else:
        nextMov = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for i in range(len(nextMov)):
            if esFactible(lab, Xini+nextMov[i][0], Yini+nextMov[i][1]):
                casillaFutura = lab[Xini + nextMov[i][0]][Yini + nextMov[i][1]]
                objetosCogidos += casillaFutura
                lab[Xini + nextMov[i][0]][Yini + nextMov[i][1]] = -1
                mejorSol = laberintoVA(lab, Xini + nextMov[i][0], Yini + nextMov[i][1], casillasVisitadas+1, objetosCogidos, mejorSol)
                lab[Xini + nextMov[i][0]][Yini + nextMov[i][1]] = casillaFutura
                objetosCogidos -= casillaFutura
    return mejorSol

def esFactible(lab, xIni, yIni):
    return 0 <= xIni < len(lab) and 0 <= yIni < len(lab[0]) and lab[xIni][yIni] != -1

if __name__ == "__main__":
    linea = list(map(int, input().strip().split()))
    numFilas = linea[0]
    numColumnas = linea[1]
    numProd = linea[2]
    lab= list()
    casillasVisitables = 0
    paso = 1
    objCogidos = 0
    for i in range(numFilas):
        lab.append(list(map(int,input().strip().split())))
        for j in range(numColumnas):
            if lab[i][j] == 0 or lab[i][j] == 1:
                casillasVisitables += 1
    if lab[0][0] == 1:
        objCogidos = 1
    lab[0][0] == -1
    #Comprobar si hay que poner un infinito o no
    mejorSol = laberintoVA(lab, 0, 0, paso, objCogidos, float('inf'))
    print(mejorSol)
