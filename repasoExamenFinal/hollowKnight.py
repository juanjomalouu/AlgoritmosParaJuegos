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
    N,M = list(map(int,input().strip().split()))
    conexiones = [-1] * N
    for i in range(len(conexiones)):
        conexiones[i] = [float('inf')] * N
    for i in range(M):
        z1, z2, dist = list(map(int,input().strip().split()))
        conexiones[z1][z2] = dist
        conexiones[z2][z1] = dist
    inicio,destino = list(map(int,input().strip().split()))

    soluciones = list()
    listaCand = list()
    solucion, listaCand = Dijsktra(copy.deepcopy(conexiones), inicio)
    # for i in range(N):
    #    soluciones.append(Dijsktra(copy.deepcopy(conexiones), inicio))
    print("a",listaCand)
    print("b", solucion)
    #print(soluciones[inicio][destino])