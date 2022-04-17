
def actualizarCompConexas(compConexas, seleccionado):
    origen = seleccionado[0]
    destino = seleccionado[1]
    ccOrigen = compConexas[origen]
    ccDestino = compConexas[destino]
    for i in range(len(compConexas)):
        if ccOrigen == compConexas[i]:
            compConexas[i] = ccDestino
    return compConexas

def kruskal(candidatos,N):
    sol = []
    compConexas = []
    for i in range(N):
        compConexas.append(i+1)
    while len(sol) <=N and candidatos != []:
        seleccionado = candidatos[0]
        candidatos.pop(0)
        if compConexas[seleccionado[0]] != compConexas[seleccionado[1]]:
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
