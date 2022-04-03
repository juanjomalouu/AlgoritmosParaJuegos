
def algoritmoDijkstra2(listaConexiones,tipo,nodo):
    i=0
    costeMin = 0
    vectDistancias = list(list())
    while listaConexiones[i][0] == nodo:
        if len(vectDistancias)==0:
            listaAux = list()
            listaAux.append(nodo)
            listaAux.append(listaConexiones[i][2])
            vectDistancias.append(listaAux)
        else:
            if listaConexiones[i][2] < vectDistancias[nodo][1]:
                vectDistancias[nodo][listaConexiones[i][1]]= listaConexiones[i][2]
        i+=1
    return vectDistancias

def sacarNodoMenor(listaConexiones,nodo):
    listaDistanciasNodos = [nodo,float('inf')]
    for i in range(len(listaConexiones)):
        if listaConexiones[i][0] == nodo or listaConexiones[i][1] == nodo:
            if listaConexiones[i][0] == nodo:
                if listaDistanciasNodos[1] > listaConexiones[i][2]:
                    listaDistanciasNodos[0] = listaConexiones[i][1]
                    listaDistanciasNodos[1] = listaConexiones[i][2]
            elif listaConexiones[i][1] == nodo:
                if listaDistanciasNodos[1] > listaConexiones[i][2]:
                    listaDistanciasNodos[0] = listaConexiones[i][0]
                    listaDistanciasNodos[1] = listaConexiones[i][2]
    return listaDistanciasNodos

def sacarListaDistanciasNodos(listaConexiones, nodoId,N):
    listaDistancias = [0]*N
    noSeleccionados = list()
    for i in range(N):
        noSeleccionados.append(i)
        listaDistancias[i] = [i,float('inf')]

    while len(noSeleccionados) != 0:
        for i in range(len(listaConexiones)):
            if listaConexiones[i][0] == nodoId or listaConexiones[i][1] == nodoId:
                if listaConexiones[i][0] == nodoId:
                    if listaConexiones[i][0] in noSeleccionados:
                        listaDistancias[i] = [listaConexiones[i][1],listaConexiones[i][2]]
                        noSeleccionados.remove(listaConexiones[i][1])


                else:
                    listaDistancias[i] = [listaConexiones[i][0],listaConexiones[i][2]]
                    noSeleccionados.remove(listaConexiones[i][0])
    return listaDistancias



def sacarListaTotalDistanciasNodos(listaConexiones,N):
    listaDistanciasNodos = []*N
    for i in range(N):
        listaDistanciasNodos[i] = sacarListaDistanciasNodos(listaConexiones,i,N)
    print(listaDistanciasNodos)




def algoritmoVoraz(listaConexiones, listaTipos):
    listaSolucion = list()
    nodoId = 0
    listaDistanciasNodo = [] * N
    sol=0
    while nodoId < len(listaConexiones):
        tipoActual = listaTipos[0]
        listaDistanciasNodo[nodoId] = sacarNodoMenor(listaConexiones,nodoId)












entrada = input().split()
N = int(entrada[0])
M = int(entrada[1])
listaTipos = list()
listaConexiones = list()
listaTipos = list(map(int,input().strip().split()))

for i in range(M):
    listaConexiones.append(list(map(int,input().strip().split())))
listaConexiones.sort(key=lambda x:x[0])

sacarListaTotalDistanciasNodos(listaConexiones,N)