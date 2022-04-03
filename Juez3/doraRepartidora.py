N = int(input())
listaC = list()

def algoritmoRepartir(lista):
    lista = sorted(lista,key=lambda x:x[1])
    sumaSolucion = 0
    listaSolucion = list()
    for i in range(len(lista)):
        if listaSolucion ==[]:
            listaSolucion.append(lista[i][1])
        else:
            listaSolucion.append(lista[i][1]+listaSolucion[i-1])
        sumaSolucion+=listaSolucion[-1]
    print(sumaSolucion)



for i in range(N):
    listaC.append(list(map(int,input().strip().split())))
algoritmoRepartir(listaC.copy())




