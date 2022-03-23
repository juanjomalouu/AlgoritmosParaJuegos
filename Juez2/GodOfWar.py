def BusquedaBinaria(A,ini,fin,x):
    mitad = (ini + fin) // 2
    if ini > fin:
        return mitad, False
    else:
        if x == A[mitad]:
            return mitad, True
        else:
            if x > A[mitad]:
                return BusquedaBinaria(A,mitad+1,fin,x)
            else:
                return BusquedaBinaria(A,ini,mitad-1,x)

numNiveles = int(input())
listaNiveles = list(map(int, input().strip().split(" ")))
listaNiveles.sort()
numNivelJugador = int(input())
listaNivelJugador = list(map(int,input().strip().split(" ")))

for i in listaNivelJugador:
    if i < listaNiveles[0]:
        print("X",listaNiveles[0])
    elif i == listaNiveles[0]:
        print("X", listaNiveles[1])
    elif i > listaNiveles[-1]:
        print(listaNiveles[-1],"X")
    elif i == listaNiveles[-1]:
        print(listaNiveles[-2],"X")
    else:
        indice = BusquedaBinaria(listaNiveles,0,numNiveles-1,i)
        if indice[1] == True:
            print(listaNiveles[indice[0]-1],listaNiveles[indice[0]+1])
        else:
            print(listaNiveles[indice[0]], listaNiveles[indice[0] + 1])


