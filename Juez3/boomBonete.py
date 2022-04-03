def prim(grafo, inicial):
    nodosVisitados = [False] * len(grafo)
    minDistanciaPorNodo = {}
    for i in range(len(grafo)):
        minDistanciaPorNodo[i] = float('inf')
    minDistanciaPorNodo[inicial] = 0
    while False in nodosVisitados:
        minDistancia = float('inf')
        n = -1
        #Selecciona el siguiente nodo a explorar
        for nodoI, dist in minDistanciaPorNodo.items():
            if dist < minDistancia and not nodosVisitados[nodoI]:
                minDistancia = dist
                n = nodoI
        #explora el nodo
        for nodoHijo, dist in grafo[n]['conex'].items():
            dist += minDistanciaPorNodo[n]
            minDistanciaPorNodo[nodoHijo] = min(dist, minDistanciaPorNodo[nodoHijo])
        nodosVisitados[n] = True
    return minDistanciaPorNodo


def minDist(tipo, distancias):
    i=0
    minimo = float('inf')
    while i < len(tipo) - 1:
        j = i + 1
        while j < len(tipo):
            minimo = min(minimo, distancias[tipo[i]][tipo[j]])
            j += 1
        i += 1
    return minimo


#Programa principal
N, M = map(int, input().strip().split())
T = list(map(int, input().strip().split()))
tipo={}
for i in range(max(T) + 1):
    tipo[i] = []
for i in range(len(T)):
    tipo[T[i]].append(i)
grafo = {}
for i in range(N):
    grafo[i] = {'conex': {}}
for i in range(M):
    nodoA, nodoB, l = map(int, input().strip().split())
    grafo[nodoA]['conex'][nodoB] = l
    grafo[nodoB]['conex'][nodoA] = l
distancias = {}
for i in range(N):
    distancias[i] = prim(grafo, i)
salida = ""
for i in range(len(tipo)):
    salida = salida + str(minDist(tipo[i], distancias)) + ' '
print(salida.strip())