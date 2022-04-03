def inicializar():
    aristas = [[3, 4 ,3], [2, 6, 4], [3, 7, 5], [1, 7, 6], [1, 3, 1], [4, 5, 1], [1, 4, 2], [2, 5, 2], [2, 7, 7], [5, 7, 8], [4, 6, 9]]
    return aristas

def inicializarSol():
    return []

def inicializarCompConexas(N):
    compConexas = []
    for i in range(N):
        compConexas.append(i)
    return compConexas

def esSolucion(sol,N):
    return len(sol) == N-1

def seleccionar(candidatos):
    mejorId = 0
    for i in range(1,len(candidatos)):
        if candidatos[i][2] < candidatos[mejorId][2]:
            mejorId = i
    seleccionado = candidatos[mejorId][:]
    del candidatos[mejorId]
    return seleccionado, candidatos

def esFactible(seleccionado,compConexas):
    return compConexas[seleccionado[0]-1] != compConexas[seleccionado[1]-1]

def anyadir(sol,seleccionado):
    sol.append(seleccionado)
    return sol

def actualizarCompConexas(compConexas,seleccionado):
    origen = seleccionado[0]-1
    destino = seleccionado[1]-1
    ccOrigen = compConexas[origen]
    ccDestino = compConexas[destino]
    for i in range(len(compConexas)):
        if compConexas[i] == ccDestino:
            compConexas[i] = ccOrigen
    return compConexas

def Kruskal(candidatos,N):
    sol = inicializarSol()
    compConexas = inicializarCompConexas(N)
    while not esSolucion(sol,N) and candidatos !=[]:
        seleccionado, candidatos = seleccionar(candidatos)
        if esFactible(seleccionado,compConexas):
            sol = anyadir(sol,seleccionado)
            compConexas = actualizarCompConexas(compConexas,seleccionado)
    return sol

# Programa Principal:
candidatos = inicializar()
N = 7
sol = Kruskal(candidatos,N)
print(sol)