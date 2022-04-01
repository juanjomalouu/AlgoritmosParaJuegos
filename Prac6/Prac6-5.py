
def inicializarTupla(N):
    fila = [0] * N
    tupla = []
    for i in range(N):
        tupla.append(fila[:])
    return tupla

def esSolucion(tupla,k):
    return k == len(tupla)**2

def esta(tupla,f,num):
    estaNum = False
    i=0
    while not estaNum and i <= f:
        estaNum = num in tupla[i]
        i+=1
    return estaNum

def comprobarFila(tupla,f,c,num):
    N = len(tupla)
    CM = N*(N**2+1)/2
    if c == N-1:
        result = sum(tupla[f]) + num == CM
    else:
        result = sum(tupla[f]) + num < CM
    return result

def comprobarColumna(tupla,f,c,num):
    N=len(tupla)
    CM = N*(N**2+1)/2
    if f == N-1:
        result = suma(tupla,c) + num == CM
    else:
        result = suma(tupla,c) + num < CM
    return result

def sumaDiag1(tupla,f):
    suma=0
    for i in range(f):
        suma+= tupla[i][i]
    return suma

def sumaDiag2(tupla,f):
    N = len(tupla)
    suma = 0
    for i in range(f):
        suma += tupla[f][N-1-i]
    return suma

def comprobarDiag1(tupla,f,c,num):
    N = len(tupla)
    CM = N * (N ** 2 + 1) / 2
    if f == N - 1:
        result = sumaDiag1(tupla, f) + num == CM
    else:
        result = sumaDiag1(tupla, f) + num < CM
    return result

def comprobarDiag2(tupla,f,c,num):
    N = len(tupla)
    CM = N * (N ** 2 + 1) / 2
    if f == N - 1:
        result = sumaDiag2(tupla, f) + num == CM
    else:
        result = sumaDiag2(tupla, f) + num < CM
    return result

def esFactible(tupla,f,c,num):
    if esta(tupla,f,num):
        result = False
    else:
        result = comprobarFila(tupla,f,c,num)
        if result:
            result = comprobarColumna(tupla,f,c,num)
            if result:
                if f == c: #Diag ppal
                    result = comprobarDiag1(tupla,f,num)
                if result and f+c == len(tupla)-1: # diagSecundaria
                    result = comprobarDiag2(tupla,f,num)
    return result

def EncontrarCuadradoVA(tupla, k):
    if esSolucion(tupla, k):
        esSol= True
    else:
        esSol = False
        lado = len(tupla)
        num=1
        f = k//lado
        c=k%lado
        while not esSol and num <= lado**2:
            if esFactible(tupla,f,c,num):
                tupla[f][c]=num
                tupla, esSol = EncontrarCuadradoVA(tupla,k+1)
            num+=1
        if not esSol:
            tupla[f][c] = 0
    return tupla, esSol




def imprimir(tupla):
    for f in range(len(tupla)):
        for c in range(len(tupla)):
            print(tupla[f][c], end="\t")
        print()



#Programa Principal
N = 3
tupla = inicializarTupla(N)
tupla, esSol = EncontrarCuadradoVA(tupla, N)
if esSol:
    imprimir(tupla)
else:
    print('No se ha encontrado solución')










