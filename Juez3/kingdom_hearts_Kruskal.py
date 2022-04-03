
def seleccionar(candidatos):
    mejorId=0
    for i in range(1,len(candidatos)):
        if candidatos[i][2] < candidatos[mejorId][2]:
            mejorId = i
    seleccionado = candidatos[mejorId][:]
    del candidatos[mejorId]
    return seleccionado,candidatos

def actualizarCompConexas(compConexas, seleccionado):
    origen = seleccionado[0]-1
    destino = seleccionado[1] -1
    ccOrigen = compConexas[origen]
    ccDestino = compConexas[destino]
    for i in range(len(compConexas)):
        if compConexas[i] == ccDestino:
            compConexas[i] = ccOrigen
    return compConexas

def kruskal(candidatos,N):
    sol = []
    compConexas = []
    for i in range(N):
        compConexas.append(i)
    while not len(sol) == N-1 and candidatos !=[]:
        seleccionado, candidatos = seleccionar(candidatos)
        if compConexas[seleccionado[0]-1] != compConexas[seleccionado[1]-1]:
            sol.append(seleccionado)
            compConexas = actualizarCompConexas(compConexas, seleccionado)
    return sol

entrada = list(map(int,input().strip().split()))
numUniv = entrada[0]
numCarre = entrada[1]
listaCarreteras = [0]*numCarre

for i in range(numCarre):
    listaCarreteras[i] = list(map(int,input().strip().split()))

listaCarreteras.sort(key = lambda x:x[2])
suma=0
listaSol = kruskal(listaCarreteras,numUniv)
for i in range(len(listaSol)):
    suma+= listaSol[i][2]
print(suma)
