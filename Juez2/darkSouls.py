# Busqueda Binaria
def BusquedaBinaria(A,ini,fin,x):
    mitad = (ini + fin) // 2
    if ini>fin:
        return mitad
    else:
        if x == A[mitad]:
            return mitad
        else:
            if x > A[mitad]:
                return BusquedaBinaria(A,mitad+1,fin,x)
            else:
                return BusquedaBinaria(A,ini,mitad-1,x)

# Coger los datos de la entrada
numEnemigos=int(input())
listaEnemigos = list(map(int, input().strip().split(" ")))
listaEnemigos.sort()
listaNiveles = list()
numNiveles = int(input())
for i in range(0, numNiveles):
    listaNiveles.append(int(input()))

#Sumar todos los valores
listaSumas = list()
for i in range(0,numEnemigos):
    if(i == 0):
        listaSumas.append(listaEnemigos[i])
    else:
        listaSumas.append(listaEnemigos[i]+listaSumas[i-1])

#Buscar que valor nos corresponde
for i in listaNiveles:
    if(i>=listaEnemigos[-1]):
        print(numEnemigos,listaSumas[-1])
    elif(i<listaEnemigos[0]):
        print(0,0)
    else:
        numTotal = BusquedaBinaria(listaEnemigos, 0, numEnemigos - 1, i)
        print(numTotal+1,listaSumas[numTotal])
