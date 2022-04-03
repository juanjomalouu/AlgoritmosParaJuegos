def algoritmoVoraz(listaDatos, riesgo):
    listaDatos.sort(key = lambda x:x[1], reverse=True)
    suma = 0
    i = 0
    while suma < riesgo and i < len(listaDatos):
        suma += listaDatos[i][2]
        print(listaDatos[i][0],end=" ")
        i += 1

entrada = input().strip().split()
N = int(entrada[0])
M = int(entrada[1])
listaDatos = list()

for i in range(N):
    listaAux = list()
    entrada = input().strip().split(' ')
    listaAux.append(entrada[0])
    listaAux.append(int(entrada[2])/int(entrada[1]))
    listaAux.append(int(entrada[1]))
    listaDatos.append(listaAux)

algoritmoVoraz(listaDatos,M)