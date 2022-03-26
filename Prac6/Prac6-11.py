

def inicializarSol(N):
    return [0]*N

def imprimir(sol,datos):
    print('Conjunto A:', end='')
    for i in range(len(datos)):
        if sol[i] ==1:
            print(datos[i],end='\t')
    print()
    print('Conjunto B:', end='')
    for i in range(len(datos)):
        if sol[i] == -1:
            print(datos[i], end='\t')
    print()

def esSolucion(datos, sol, indice):
    if indice < len(sol):
        return False
    else:
        suma = 0
        for i in range(len(datos)):
            suma += datos[i]*sol[i]
        return suma == 0

def dividirVA(datos,sol,indice):
    if esSolucion(datos,sol,indice):
        esSol = True
    else:
        esSol = False
        if indice < len(sol):
            if esFactible(sol, datos, indice, 1):
                sol[indice] = 1
                sol, esSol = dividirVA(datos, sol, indice+1)
            if not esSol:
                if esFactible(sol, datos, indice, -1):
                    sol[indice] = -1
                    sol, esSol = dividirVA(datos, sol, indice + 1)
    return sol, esSol

def esFactible(sol,datos,indice,valor):
    semisuma = sum(datos)
    sumaConj = 0
    for i in range(indice):
        if sol[i] == valor:
            sumaConj += datos[i]
    return sumaConj + datos[indice] <= semisuma

if __name__ == '__main__':
    conjNums = list(map(int, input().strip().split()))
    sol = inicializarSol(len(conjNums))
    indice = 0
    sol, esSol = dividirVA(conjNums,sol,indice)
    if esSol:
        imprimir(sol,conjNums)
    else:
        print("No se ha llegado a una solucion valida xD")