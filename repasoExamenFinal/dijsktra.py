def dijsktra(origen, conexiones, numNodos):
    vectorDist = [float("inf")] * numNodos
    vectorDist[origen] = 0
    vectorCam = [-1] * numNodos
    vectorCam[origen] = origen
    noVisitados = list(range(numNodos))
    actual = origen
    while len(noVisitados) >1:
        noVisitados.remove(actual)
        salidasDelNodo = buscarSalidas(actual, conexiones)
        vectorDist, vectorCam = actualizarVectores(vectorDist, vectorCam, actual, salidasDelNodo)
        actual = siguienteNodo(vectorDist, noVisitados)
    return vectorDist, vectorCam

def siguienteNodo(vectorDist, noVisitados):
    siguienteNodo = noVisitados[0]
    for i in range(1, len(noVisitados)):
        if vectorDist[noVisitados[i]] < vectorDist[siguienteNodo]:
            siguienteNodo = noVisitados[i]
    return siguienteNodo

def actualizarVectores(vectorDist, vectorCam, actual, salidasDelNodo):
    for arista in salidasDelNodo:
        if arista[0] == actual:
            if vectorDist[arista[1]] > vectorDist[actual] + arista[2]:
                vectorDist[arista[1]] = vectorDist[actual] + arista[2]
                vectorCam[arista[1]] = actual
        elif arista[1] == actual:
            if vectorDist[arista[0]] > vectorDist[actual] + arista[2]:
                vectorDist[arista[0]] = vectorDist[actual] + arista[2]
                vectorCam[arista[0]] = actual
    return vectorDist, vectorCam

def buscarSalidas(actual, conexiones):
    salidas = list()
    for conexion in conexiones:
        if conexion[0] == actual or conexion[1] == actual:
            salidas.append(conexion)
    return salidas

def imprimirCamino(vectorCam, origen, destino):
    actual = destino
    camino = list()
    while actual != origen:
        camino.append(actual)
        actual = vectorCam[actual]
    camino.append(origen)
    camino.reverse()
    for nodo in camino:
        print(nodo, end=" ")


if __name__ == "__main__":
    N, M = map(int, input().strip().split())
    conexiones = list(range(M))
    for i in range(M):
        conexiones[i] = list(map(int, input().strip().split()))
    origen, destino = map(int, input().strip().split())
    vectorDist, vectorCam = dijsktra(origen, conexiones, N)
    print(vectorCam)
    print(vectorDist[destino])
    imprimirCamino(vectorCam, origen, destino)
