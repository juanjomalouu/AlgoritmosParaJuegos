import copy

def doraemonVA(solucion, mejorSol, datos, k):
    if esSolucion(solucion, datos):
        if not esMultiplo(solucion, datos):
            mejorSol = mejor(solucion,mejorSol)
    else:
        for i in range(k, datos['N']):
            if esFactible(solucion, datos, i):
                solucion = asignar(solucion, i,datos)
                mejorSol = doraemonVA(solucion, mejorSol, datos, i)
                solucion = borrar(solucion, i, datos)
    return mejorSol

def mejor(sol1, sol2):
    if sol1['valor'] > sol2['valor']:
        mejor = copy.deepcopy(sol1)
    else:
        mejor = copy.deepcopy(sol2)
    return mejor

def esFactible(solucion, datos, i):
    return solucion['peso'] + datos['peso'][i] <= datos['W'] and solucion['objetos'][i] == 0

def esMultiplo(sol, datos):
    suma = 0
    for i in range(datos['N']):
        if sol['objetos'][i] == 1:
            suma += datos['id'][i]
    return suma % 5 == 0

def esSolucion(solucion,datos):
    return solucion['peso'] + min(datos['peso']) > datos['W']

def asignar(solucion, i,datos):
    solucion['objetos'][i] += 1
    solucion['peso'] += datos['peso'][i]
    solucion['valor'] += datos['valor'][i]
    return solucion

def borrar(solucion, i, datos):
    solucion['objetos'][i] -= 1
    solucion['peso'] -= datos['peso'][i]
    solucion['valor'] -= datos['valor'][i]
    return solucion

if __name__ == "__main__":
    N, M = list(map(int,input().strip().split()))
    datos = {}
    listaObjetosCogidos = list()
    datos = {}
    datos['N'] = N
    datos['W'] = M

    datos["id"] = list()
    datos["valor"] = list()
    datos["peso"] = list()
    for i in range(N):
        id, valor, peso = list(map(int, input().strip().split()))
        datos['id'].append(id)
        datos["valor"].append(valor)
        datos["peso"].append(peso)


    solucion = {}
    solucion['objetos'] = [0] * N
    solucion['peso'] = 0
    solucion['valor'] = 0

    mejorSol = {}
    mejorSol['objetos'] = [0] * N
    mejorSol['peso'] = 0
    mejorSol['valor'] = 0

    mejorSol = doraemonVA(solucion, mejorSol, datos, 0)
    print(mejorSol["valor"])

