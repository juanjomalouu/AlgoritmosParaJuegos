
def crearListaGrafo(listaCon, N):
    grafo = [] * N

    for i in range(N):
        listaInterior = [float('inf')] * N
        grafo.append(listaInterior)
    for i in range(len(listaCon)):
        grafo[listaCon[i][0]][listaCon[i][1]] = listaCon[i][2]
        grafo[listaCon[i][1]][listaCon[i][0]] = listaCon[i][2]
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

entrada = input().split()
N = int(entrada[0])
M = int(entrada[1])
listaTipos = list()
listaConexiones = list()
listaTipos = list(map(int,input().strip().split()))

for i in range(M):
    listaConexiones.append(list(map(int,input().strip().split())))
listaConexiones.sort(key=lambda x:x[0])

nodoInic=0
grafo = crearListaGrafo(listaConexiones, N)
listaDistancias = list()

for i in range(N):
    listaDistancias.append(Dijkstra(copy.deepcopy(grafo),i))

tipo = listaTipos[0]
distanciaMinima = [float('inf')] * N
for i in range(len(listaDistancias)):
    for j in range(len(listaDistancias)):
        if listaTipos[j] == listaTipos[i]:
            if distanciaMinima[listaTipos[j]] > listaDistancias[i][j]:
                distanciaMinima[listaTipos[j]] = listaDistancias[i][j]
