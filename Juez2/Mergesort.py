
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
    L = [0]*(n1+1)
    R = [0]*(n2+1)
    for i in range(n1):
        L[i] = A[p + i]
    for j in range(n2):
        R[j] = A[q + 1 + j]
    L[n1] = float('inf')
    R[n2] = float('inf')
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

N = int(input())
numData = list(map(int, input().strip().split(" ")))
mergesort(numData,0,N-1)
for i in numData:
    print(i,"" ,end="")


    def mergeSort(lista, ini, fin):
        if ini < fin:
            mitad = (ini + fin) // 2
            mergeSort(lista, ini, mitad)
            mergeSort(lista, mitad + 1, fin)
            lista = merge(lista, ini, mitad, fin)
        return lista


    def merge(A, ini, mitad, fin):
        n1 = mitad - ini + 1
        n2 = fin - mitad
        L = [0] * (n1 + 1)
        R = [0] * (n2 + 1)
        for i in range(n1):
            L[i] = A[ini + i]
        for j in range(n2):
            R[j] = A[mitad + 1 + j]
        L[n1] = float('inf')
        R[n2] = float('inf')
        i = 0
        j = 0
        for k in range(ini, fin + 1):
            if R[j] < 0 and L[i] >= 0 and R[j] != float('inf'):
                A[k] = R[j]
                j += 1
            elif L[i] != float('inf'):
                A[k] = L[i]
                i += 1
        return A



def mergeSort(lista, ini, fin):
    if fin > ini:
        mitad = (fin+ini)//2
        mergeSort(lista, ini, mitad)
        mergeSort(lista, mitad+1, fin)
        lista = merge(lista, ini,mitad,fin)
    return lista

def merge(lista, ini, mitad, fin):
    n1 = mitad-ini +1
    n2 = fin - mitad
    aux1 = [0] * (n1+1)
    aux2 = [0] * (n2+1)
    for i in range(n1):
        aux1[i] = lista[ini+i]
    for j in range(n2):
        aux2[j] = lista[mitad+1+j]
    i = 0
    j = 0
    aux1[n1] = float('inf')
    aux2[n2] = float('inf')
    for k in range(ini,fin+1):
        if aux2[j] < 0 and aux1[i] >= 0 and aux2[j] != float('inf'):
            lista[k] = aux2[j]
            j+=1
        elif aux1[i] != float('inf'):
            lista[k] = aux1[i]
            i+=1
    return lista
