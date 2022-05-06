
def kruskal(candidatos, N):
    sol = []
    compConexas = []
    for i in range(N):
        compConexas.append(i+1)
    while not len(sol) == N-1 and candidatos !=[]:
        seleccionado = candidatos[0]
        del candidatos[0]
        if compConexas[seleccionado[0]] != compConexas[seleccionado[1]]:
            sol.append(seleccionado)
            compConexas = actualizarCompConexas(compConexas, seleccionado)
    return sol

def actualizarCompConexas(compConexas, seleccionado):
    origen = seleccionado[0]
    destino = seleccionado[1]
    ccOrigen = compConexas[origen]
    ccDestino = compConexas[destino]
    for i in range(len(compConexas)):
        if compConexas[i] == ccDestino:
            compConexas[i] = ccOrigen
    return  compConexas

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