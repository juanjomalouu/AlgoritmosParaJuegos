def dibujar (A, ini, fin):
    for i in range(len(A)):
        if A[i] == ini:
            print("[",end="")
        print(A[i]," ",end="")
        if A[i]==fin:
            print("]",end="")
    print()

def BusquedaBinaria(A,ini,fin,x):
    encontrado=False
    noEncontrado=True
    while encontrado==False and noEncontrado==True:
        dibujar(A, ini, fin)
        if ini>fin:
            noEncontrado=False
        else:
            mitad=(ini+fin)//2
            if x == A[mitad]:
                encontrado= True
            else:
                if x > A[mitad]:
                    ini=mitad+1
                else:
                    fin=mitad-1
    return encontrado

coleccion = list(range(20))
found = BusquedaBinaria(coleccion,0,len(coleccion)-1,16)
print(found)
