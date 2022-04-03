import copy

def inicializar():
    aristas = [[3, 4 ,3], [2, 6, 4], [3, 7, 5], [1, 7, 6], [1, 3, 1], [4, 5, 1], [1, 4, 2], [2, 5, 2], [2, 7, 7], [5, 7, 8], [4, 6, 9]]
    return aristas

def insertarOrdenado(conjAristas,aristaNueva):
    if conjAristas == []:
        conjAristas = [aristaNueva]
    else:
        i = 0
        parar = False
        while not parar:
            parar = i >= len(conjAristas) or conjAristas[i][2] > aristaNueva[2]
            i += 1
        conjAristas.insert(i-1,aristaNueva)
    return conjAristas

def actualizar(aristasCandidatas,aristas,vertice):
    for i in range(len(aristas)):
        if aristas[i][0] == vertice or aristas[i][1] == vertice:
            aristaNueva = list(copy.deepcopy(aristas[i][:]))
            aristasCandidatas = insertarOrdenado(aristasCandidatas,aristaNueva)
    return aristasCandidatas

def Prim(aristas,n):
    verticeInic = 1
    verticeEnSol = [verticeInic]
    aristasCandidatas = []
    aristasCandidatas = actualizar(aristasCandidatas,aristas,verticeInic)
    sol = []
    while len(verticeEnSol) < n:
        aristaSeleccionada = aristasCandidatas[0][:]
        aristasCandidatas = aristasCandidatas[1:][:]
        if (aristaSeleccionada[0] in verticeEnSol and aristaSeleccionada[1] not in verticeEnSol):
            sol.append(aristaSeleccionada)
            verticeEnSol.append(aristaSeleccionada[1])
            aristasCandidatas = actualizar(aristasCandidatas, aristas, aristaSeleccionada[1])
        else:
            if (aristaSeleccionada[1] in verticeEnSol and aristaSeleccionada[0] not in verticeEnSol):
                sol.append(aristaSeleccionada)
                verticeEnSol.append(aristaSeleccionada[0])
                aristasCandidatas = actualizar(aristasCandidatas, aristas, aristaSeleccionada[0])
    return sol

# Prog Ppal:
aristas = inicializar()
n = 7
sol = Prim(aristas,n)
print(sol)