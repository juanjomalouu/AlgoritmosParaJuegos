import time

import numpy as np
import time as tm


def mergesort(A, p, r):
    if p<r:
        q = (p+r)//2
        mergesort(A, p, q)
        mergesort(A, q+1, r)
        merge(A,p,q,r)
    return A

#Merge combina todos los arrays que han sido ordenados
def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = np.empty(n1+1)
    R = np.empty(n2+1)
    for i in range(n1):
        L[i] = A[p + i]
    for j in range(n2):
        R[j] = A[q + 1 + j]
    L[n1] = np.inf
    R[n2] = np.inf
    i = 0
    j = 0
    for k in range(p,r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i+=1
        else:
            A[k] = R[j]
            j+=1
    return A

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

MIN = 0
MAX = 1000
STEP = 100

tipo = int(input("Pulsa 1 para insercion directa, 2 para mergesort, 3 numpysort(insercion), 4 numpysort(mergesort)\n"))
while(MIN <= MAX):
    MIN+=STEP
    numData = np.random.randint(0,100,MIN)
    clock = time.perf_counter()
    if tipo == 1:
        ordenacionInsercion(numData)
        clock = time.perf_counter()-clock
        print(len(numData),clock)
    elif tipo == 2:
        mergesort(numData, 0, len(numData)-1)
        clock = time.perf_counter() - clock
        print(len(numData), clock)
    elif tipo ==3:
        np.sort(numData)
        clock = time.perf_counter() - clock
        print(len(numData), clock)
    elif tipo ==4:
        numData.sort(kind='mergesort')
        clock = time.perf_counter() - clock
        print(len(numData),'{:f}'.format(clock))

