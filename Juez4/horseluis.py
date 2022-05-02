
def laberintoVA(lab, xIni, yIni, casillasVisitadas, objCogidos, objMaximos, mejorSol):
    if xIni <= len(lab)-1 and yIni <= len(lab[0])-1 and objCogidos == objMaximos and casillasVisitadas < mejorSol:
        mejorSol = casillasVisitadas
    else:
        sigMov = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for i in range(len(sigMov)):
            if esFactible(lab, xIni+sigMov[i][0], yIni+sigMov[i][1], objCogidos):
                casillaFutura = lab[xIni + sigMov[i][0]][yIni + sigMov[i][1]]
                cogido = False
                if casillaFutura == objCogidos+1:
                    objCogidos+=1
                    cogido = True
                lab[xIni + sigMov[i][0]][yIni + sigMov[i][1]]=-1
                mejorSol = laberintoVA(lab, xIni+sigMov[i][0], yIni+sigMov[i][1], casillasVisitadas+1, objCogidos, objMaximos, mejorSol)
                if cogido:
                    objCogidos-=1
                lab[xIni + sigMov[i][0]][yIni + sigMov[i][1]] = casillaFutura
    return mejorSol

def esFactible(lab, xIni, yIni, objCogidos):
    return 0 <= xIni < len(lab) and 0 <= yIni < len(lab[0]) and lab[xIni][yIni] != -1 and (lab[xIni][yIni] == 0 or lab[xIni][yIni] == objCogidos+1)

if __name__ == "__main__":
    lineaInfo = input().strip().split()
    numFilas = int(lineaInfo[0])
    numColumnas = int(lineaInfo[1])
    numObj = int(lineaInfo[2])
    lab = list()
    paso = 1
    objCogidos = 0
    for i in range(numFilas):
         lab.append(list(map(int, input().strip().split())))
    if lab[0][0] == 1:
        objCogidos+=1
    lab[0][0] = -1
    casillasVisitadas = laberintoVA(lab, 0, 0, paso, objCogidos, numObj, float('inf'))
    print(casillasVisitadas)