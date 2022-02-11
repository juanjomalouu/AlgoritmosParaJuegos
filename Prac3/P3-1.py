import numpy as np
data =np.array(input().split())

numData = [int (g) for g in data]
def ordenacionInsercion(coleccion):
    for j in range(1, len(coleccion)):
        clave = coleccion[j]
        #Insertar la clave en la secuencia ordenada:
        i = j - 1
        while i >= 0 and coleccion[i] > clave:
            coleccion[i +1] = coleccion[i]
            i = i - 1
        coleccion[i +1] = clave
    return coleccion

print(ordenacionInsercion(numData))
