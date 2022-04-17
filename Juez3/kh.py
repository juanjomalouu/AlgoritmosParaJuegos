
def comprobarConexion(compConexas, seleccionado):
    anadido = False
    i=0
    borrado=False
    j = 0
    while not anadido and i < len(compConexas):
        j = i + 1
        if seleccionado[0] in compConexas[i]:
            while borrado == False and j < len(compConexas):
                if seleccionado[1] in compConexas[j]:
                    compConexas[i].extend(compConexas[j])
                    del compConexas[j]
                    borrado=True
                j += 1
            if borrado == False:
                compConexas[i].append(seleccionado[1])
            anadido = True
        elif seleccionado[1] in compConexas[i]:
            while borrado == False and j < len(compConexas):
                if seleccionado[0] in compConexas[j]:
                    compConexas[i].extend(compConexas[j])
                    del compConexas[j]
                    borrado = True
                j += 1
            if borrado == False:
                compConexas[i].append(seleccionado[0])
            anadido = True
        i+=1
    if anadido == False:
        compConexas.append([seleccionado[0],seleccionado[1]])

    return compConexas

def kruskal(candidatos,N):
    sol =[]
    compConexas=[]
    while not len(sol) == N-1 and candidatos !=[]:
        seleccionado = candidatos[0]
        if compConexas == []:
            compConexas.append([seleccionado[0],seleccionado[1]])
            sol.append(seleccionado)
        else:
            #Este if es el que falla
            estaDentro = False
            i=0
            while i < len(compConexas) and not estaDentro:
                if seleccionado[0] in compConexas[i] and seleccionado[1] in compConexas[i]:
                    estaDentro = True
                else:
                    compConexas = comprobarConexion(compConexas, seleccionado)
                    sol.append(seleccionado)
                i+=1
        candidatos.remove(seleccionado)
    return sol

entrada = list(map(int,input().strip().split()))
numUniv = entrada[0]
numCarre = entrada[1]
listaCarreteras = [0]*numCarre

for i in range(numCarre):
    listaCarreteras[i] = list(map(int,input().strip().split()))

listaCarreteras.sort(key=lambda x:x[2])
suma=0
listaSol = kruskal(listaCarreteras,numUniv)
for i in range(len(listaSol)):
    suma+= listaSol[i][2]
print(suma)
