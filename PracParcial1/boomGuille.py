def seleccionar(solucionActual, visitados):
    indSelec = 0
    min = inf
    for i in range(len(solucionActual)):
        if i not in visitados and min> solucionActual[i]:
            indSelec = i
            min = solucionActual[i]
    return indSelec

def actualizarSol(distanciasSolActual, indSeleccionado, distanciasNuevoNodo):
    for i in range(len(distanciasSolActual)):
        if distanciasSolActual[i]> distanciasSolActual[indSeleccionado]+distanciasNuevoNodo[i]:
            distanciasSolActual[i] = distanciasSolActual[indSeleccionado]+distanciasNuevoNodo[i]
    return distanciasSolActual


#programa principal
from math import inf
N, M = map(int,(input().strip().split(" ")))# numero de nodos, numero de conexiones
t = list(map(int,(input().strip().split(" "))))# tipos
conexiones = [] #Conexiones: Nodo1-Nodo2-Longitud
for i in range (M):
    C, D, L = map(int, (input().strip().split(" ")))
    conexiones.append([C, D, L])
visitados = []#Nodos que ya hemos visitado
noSeleccionados = []#Nodos que todavía no se han seleccionado
sol = []#lista de caminos mínimos entre tipos
vectoresDistancias = []
for i in range(N):
    noSeleccionados.append(i)
    vectoresDistancias.append([inf]*N)
    vectoresDistancias[i][i]=0
for i in range(M):
    vectoresDistancias[conexiones[i][0]][conexiones[i][1]]= conexiones[i][2]
    vectoresDistancias[conexiones[i][1]][conexiones[i][0]] = conexiones[i][2]
for i in range(N): #una iteración por cada nodo
    sol.append(vectoresDistancias[i][:])
    indNodoInic = i
    visitados.append(i)
    for j in range(N-1):
        seleccionado = seleccionar(sol[i][:], visitados)
        visitados.append(seleccionado)
        sol[i] = actualizarSol(sol[i][:], seleccionado, vectoresDistancias[seleccionado])

    visitados = []
solTipos = []
for i in range(len(t)):
    if t[i] not in solTipos:
        solTipos.append(t[i])

for i in range(len(solTipos)):
    minimo=inf
    for j in range(N):
        for k in range(N):
            if t[k]==i and t[j]==i and sol[j][k]<minimo and sol[j][k]!=0:
                minimo=sol[j][k]
    print(minimo, end=" ")