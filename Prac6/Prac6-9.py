def esSolucion(W,M,sol,k):
    suma = 0
    for i in range(k+1):
        suma+= sol[i] * W[i]
    return suma==M

def esFactible(W, M, sol, k):
    suma = 0
    for i in range(k + 1):
        suma += sol[i] * W[i]
    return suma <= M

def vueltaAtrasSubConjuntos(W,M,sol,k):
    if esSolucion(W,M,sol,k):
        print(sol)
    else:
        if k < len(sol)-1:
            k = k +1
            vueltaAtrasSubConjuntos(W,M,sol,k)
            if esFactible(W,M,sol,k):
                sol[k] = 1
                vueltaAtrasSubConjuntos(W, M, sol, k)
                sol[k] = 0

listaConjuntosSolucion = list()

if __name__== '__main__':
    conjunto = list(map(int, input().strip().split()))
    sumaFinal = int(input())
    sol = [0] * len(conjunto)
    vueltaAtrasSubConjuntos(conjunto, sumaFinal, sol, -1)

