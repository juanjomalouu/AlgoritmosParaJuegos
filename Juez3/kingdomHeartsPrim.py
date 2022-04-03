import copy

def actualizar(aristasCand, aristas, vertice):
    for i in range(len(aristas)):
        if aristas[i][0] == vertice or aristas[i][1]==vertice:
            aristaNueva = list(copy.deepcopy(aristas[i][:]))
            if aristasCand == []:
                aristasCand = [aristaNueva]
            else:
                i = 0
                parar = False
                while not parar:
                    parar = i >= len(aristasCand) or aristasCand[i][2] > aristaNueva[2]
                    i += 1
                aristasCand.insert(i - 1, aristaNueva)
    return aristasCand

def prim(listaConexiones, N):
    verticeInicial=0
    verticeEnSol = [verticeInicial]
    aristasCandidatas = []
    aristasCandidatas = actualizar(aristasCandidatas,listaConexiones,verticeInicial)
    sol =[]
    while len(verticeEnSol) < N:
        aristaSeleccionada = aristasCandidatas[0][:]
        aristasCandidatas = aristasCandidatas[1:][:]
        if(aristaSeleccionada[0] in verticeEnSol and aristaSeleccionada[1] not in verticeEnSol):
            sol.append(aristaSeleccionada)
            verticeEnSol.append(aristaSeleccionada[1])
            aristasCandidatas = actualizar(aristasCandidatas, listaConexiones, aristaSeleccionada[1])
        else:
            if(aristaSeleccionada[1] in verticeEnSol and aristaSeleccionada[0] not in verticeEnSol):
                sol.append(aristaSeleccionada)
                verticeEnSol.append(aristaSeleccionada[0])
                aristasCandidatas = actualizar(aristasCandidatas, listaConexiones, aristaSeleccionada[0])
    return sol;









entrada = list(map(int,input().strip().split()))
numUniv = entrada[0]
numCarre = entrada[1]
listaCarreteras = [0]*numCarre

for i in range(numCarre):
    listaCarreteras[i] = list(map(int,input().strip().split()))


suma=0
listaSol = prim(listaCarreteras,numUniv)
for i in range(len(listaSol)):
    suma+= listaSol[i][2]
print(suma)
