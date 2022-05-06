
def actualizarCompConexa(compConexas, seleccionado):
    origen = seleccionado[0]
    destino = seleccionado[1]
    ccOrigen = compConexas[origen]
    ccDestino = compConexas[destino]
    for i in range(len(compConexas)):
        if ccOrigen == compConexas[i]:
            compConexas[i] = ccDestino
    return compConexas


def kruskal(candidatos, P):
    sol = []
    compConexas = []
    for i in range(N):
        compConexas.append(i+1)
    while len(sol) <= N and infoSalas != []:
        seleccionado = candidatos[0]
        candidatos.pop(0)
        if compConexas[seleccionado[0]] != compConexas[seleccionado[1]]:
            sol.append(seleccionado)
            compConexas = actualizarCompConexa(compConexas, seleccionado)
    return sol

import copy

def inicializarCandidatos(distancias, nodoInic):
    candidatos = []
    for i in range(len(distancias)):
        if i != nodoInic:
            candidatos.append([i, distancias[i]])
    return candidatos

def seleccionar(candidatos, listaCaminoRecorrido):
    indMejor = 0
    for i in range(1, len(candidatos)):
        if candidatos[i][1] < candidatos[indMejor][1]:
            indMejor = i
    seleccionado = candidatos[indMejor][:]
    #listaCaminoRecorrido.append(candidatos[indMejor][0])
    del candidatos[indMejor]
    return seleccionado, candidatos, listaCaminoRecorrido

def actualizarDistancias(dist, sel, grafo, candidatos, listaCand):
    dist[sel[0]] = sel[1]
    listaCand[sel[0]] = sel[0]
    for i in range(len(candidatos)):
        nuevaDistI = sel[1] + grafo[sel[0]][candidatos[i][0]]
        if nuevaDistI < candidatos[i][1]:
            candidatos[i][1] = nuevaDistI
            listaCand[i] = -1
    return dist, candidatos,listaCand

def Dijsktra(grafo, nodoInic):
    distancias = grafo[nodoInic][:]
    candidatos = inicializarCandidatos(distancias, nodoInic)
    listaCandidatos = [-1] * len(distancias)
    while candidatos != []:
        seleccionado, candidatos, listaCandidatos = seleccionar(candidatos,listaCandidatos )
        distancias, candidatos, listaCandidatos = actualizarDistancias(distancias, seleccionado, grafo, candidatos, listaCandidatos)
    return distancias, listaCandidatos


if __name__ == "__main__":
    N, M, P = list(map(int,input().strip().split()))
    salasEnemigos = list(map(int,input().strip().split()))
    infoSalas = list()
    for i in range(M):
        infoSalas.append(list(map(int,input().strip().split())))

    listaSol = Dijsktra(infoSalas, 0)
    print(listaSol)


