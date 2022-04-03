

def kruskal(candidatos,N):
    sol =[]
    compConexas=[]
    while not len(sol) == N and candidatos !=[]:
        seleccionado = candidatos[0]
        if compConexas == []:
            compConexas.append(seleccionado[0])
            compConexas.append(seleccionado[1])
        else:
            if not seleccionado[0] in compConexas and not seleccionado[1] in compConexas:
                if not seleccionado[0] in compConexas:
                    compConexas.append(seleccionado[0])
                else:
                    compConexas.append(seleccionado[1])
                sol.append(seleccionado)
        candidatos.remove(seleccionado)
    return sol

entrada = list(map(int,input().strip().split()))
numUniv = entrada[0]
numCarre = entrada[1]
listaCarreteras = [0]*numCarre

for i in range(numCarre):
    listaCarreteras[i] = list(map(int,input().strip().split()))
print(listaCarreteras)
listaCarreteras.sort(key=lambda  x:x[2])
print(listaCarreteras)
suma=0
listaSol = kruskal(listaCarreteras,numUniv)
for i in range(len(listaSol)):
    suma+= listaSol[i][2]
print(suma)
