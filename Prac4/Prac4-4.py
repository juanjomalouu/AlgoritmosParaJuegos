def dibujar (A, ini, fin, x):
    for i in range(len(A)):
        if A[i] == ini:
            print("[",end="")
        print(A[i]," ",end="")
        if A[i]==fin:
            print("]",end="")
    print()

def BusquedaTernaria(A,ini,fin,x):
    dibujar(A,ini,fin,x)
    if ini > fin:
        return False
    else:
        tercio = (fin-ini)//3+ini
        if x == A[tercio]:
            return True
        else:
            if x < A[tercio]:
                return BusquedaTernaria(A,ini,tercio-1,x)
            else:
                tercio2 = (2*(fin-ini)//3)+ini
                if x == A[tercio2]:
                    return True
                else:
                    if x < A[tercio2]:
                        return BusquedaTernaria(A,tercio+1,tercio2-1,x)
                    else:
                        return BusquedaTernaria(A,tercio2+1,fin,x)
import random

coleccion = list(range(21))
numAle=random.randint(0,25)
print(numAle)
found = BusquedaTernaria(coleccion,0,len(coleccion)-1,numAle)
print(found)
