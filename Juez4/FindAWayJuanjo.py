

def laberintoVA(lab, xIni, yIni, casillasVisitadas):
    if casillasVisitadas == casillasTotales+1 and xIni == len(lab)-1 and yIni == len(lab)-1:
        esSol = True
    else:
        esSol = False
        sigMov = [[1,0],[0,1],[-1,0],[0,-1]]
        i = 0
        while not esSol and i < len(sigMov):
            if esFactible(lab, xIni+sigMov[i][0], yIni+sigMov[i][1]):
                lab[xIni+sigMov[i][0]][yIni+sigMov[i][1]] = casillasVisitadas
                lab, esSol = laberintoVA(lab, xIni+sigMov[i][0], yIni+sigMov[i][1],casillasVisitadas+1)
                if not esSol:
                    lab[xIni+sigMov[i][0]][yIni+sigMov[i][1]] = 0
            i+=1
    return lab, esSol

def esFactible(lab, xIni, yIni):
    return  0 <= xIni < len(lab) and 0 <= yIni < len(lab) and lab[xIni][yIni] == 0

#Prog Ppal
if __name__ == "__main__":
    tamanioLab = int(input())
    lab = []
    casillasTotales = 0
    for i in range(tamanioLab):
        linea = input().strip().split()
        lab.append([0]*tamanioLab)
        for j in range(tamanioLab):
            lab[i][j] = int(linea[j])
            if lab[i][j] == 0:
                casillasTotales+=1
    paso = 1
    lab, esSol = laberintoVA(lab, 0, 0, paso+1)
    if esSol == True:
        print("SI")
    else:
        print("NO")