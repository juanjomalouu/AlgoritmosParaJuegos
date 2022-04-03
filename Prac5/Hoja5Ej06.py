from math import inf
import copy

def inicializar():
    grafo = [[0, 5, inf, 3, inf],[inf, 0, inf, inf, 2], [inf, inf, 0, inf, inf ],[inf,  1, 11, 0, 6],[inf, inf, 1, inf, 0]]
    return grafo

def inicializarCandidatos(distancias,nodoInic):
    candidatos = []
    for i in range(len(distancias)):
        if i != nodoInic:
            candidatos.append([i, distancias[i]])
    return candidatos

def seleccionar(candidatos):
    indMejor = 0
    for i in range(1,len(candidatos)):
        if candidatos[i][1] < candidatos[indMejor][1]:
            indMejor = i
    seleccionado = candidatos[indMejor][:]
    del candidatos[indMejor]
    return seleccionado,candidatos

def actualizarDistancias(dist,sel,grafo,candidatos):
    dist[sel[0]] = sel[1]
    for i in range(len(candidatos)):
        nuevaDistI = sel[1] + grafo[sel[0]][candidatos[i][0]]
        if nuevaDistI < candidatos[i][1] :
            candidatos[i][1] = nuevaDistI
    return dist,candidatos

def Dijkstra(grafo,nodoInic):
    distancias = grafo[nodoInic][:]
    candidatos = inicializarCandidatos(distancias,nodoInic)
    while candidatos != []:
        seleccionado, candidatos = seleccionar(candidatos)
        distancias,candidatos = actualizarDistancias(distancias,seleccionado,grafo,candidatos)
    return distancias

# Prog Ppal:
grafo = inicializar()
nodoInic = 0
solucion = Dijkstra(copy.deepcopy(grafo),nodoInic)
print('Las longitudes de los caminos mínimos desde',nodoInic,'son:')
print(solucion)