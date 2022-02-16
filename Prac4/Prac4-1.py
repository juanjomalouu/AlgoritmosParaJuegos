def dibujar (A, ini, fin, x):
    for i in range(len(A)):
        if A[i] == ini:
            print("[",end="")
        print(A[i]," ",end="")
        if A[i]==fin:
            print("]",end="")
    print()

def BusquedaBinaria(A,ini,fin,x):
    dibujar(A,ini,fin,x)
    if ini>fin:
        return False
    else:
        mitad=(ini+fin)//2
        if x == A[mitad]:
            return True
        else:
            if x > A[mitad]:
                return BusquedaBinaria(A,mitad+1,fin,x)
            else:
                return BusquedaBinaria(A,ini,mitad-1,x)

coleccion = list(range(20))
found = BusquedaBinaria(coleccion,0,len(coleccion)-1,0)
print(found)
