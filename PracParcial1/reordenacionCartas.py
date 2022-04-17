
def mergeSort(lista, ini, fin):
    if fin>ini:
        mitad = (ini+fin)//2
        mergeSort(lista, ini, mitad)
        mergeSort(lista, mitad+1, fin)
        merge(lista, ini, mitad, fin)
    return lista

def merge(lista, ini,mitad,fin):
    n1 = mitad - ini +1
    n2 = fin-mitad
    aux1 = [0] * (n1+1)
    aux2 = [0] * (n2+1)
    for i in range(n1):
        aux1[i] = lista[ini+i]
    for j in range(n2):
        aux2[j] = lista[mitad+1+j]
    aux1[n1] = float('inf')
    aux2[n2] = float('inf')
    i = 0
    j = 0
    for k in range(ini,fin+1):
        if aux1[i] <= aux2[j]:
            lista[k] = aux1[i]
            i+=1
        else:
            lista[k] = aux2[j]
            j+=1
    return lista



if __name__ == "__main__":
    N = int(input())
    listaCartas = list(map(int,input().strip().split()))

    listaCartas = mergeSort(listaCartas, 0, N-1)
    print(listaCartas)