def BusquedaBinaria(A,ini,fin,x):
    if ini>fin:
        return -1
    else:
        mitad=(ini+fin)//2
        if x == A[mitad]:
            return x
        else:
            if x > A[mitad]:
                return BusquedaBinaria(A,mitad+1,fin,x)
            else:
                return BusquedaBinaria(A,ini,mitad-1,x)

numEnemigos=int(input())

listaEnemigos = list(map(int, input().strip().split(" ")))
listaEnemigos.sort()


listaNiveles = list()

numNiveles = int(input())

for i in range(0, numNiveles):
    listaNiveles.append(int(input()))

listaRespuesta = list()

for i in listaNiveles:
    numFinal = listaEnemigos[numEnemigos-1]
    if(i<numFinal):
        listaRespuesta.append(BusquedaBinaria(listaEnemigos, 0, numEnemigos-1, i))
    else:
        listaRespuesta.append(numFinal)



for i in listaRespuesta:
    print(i,"", end="")
    suma=0
    for j in range(0,i):
        suma+=listaEnemigos[j]
    print(suma)