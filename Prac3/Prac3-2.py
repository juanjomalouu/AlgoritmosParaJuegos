import numpy as np
#data =np.array(input().split())
#numData = [int (g) for g in data]

numData = np.random.randint(0,9,10)
#p y r son el inicio y el final del intervalo que quiero ordenar
#Se utilizan estos argumentos ya que este algoritmo consiste en
#Dividir el array y ordenarlo en tramos mas pequeños

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
print(mergesort(numData,0,len(numData)-1))