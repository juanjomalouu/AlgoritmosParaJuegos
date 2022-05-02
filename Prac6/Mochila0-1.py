import copy


def inicializarDatos():
    datos={}
    datos['N'] = 4
    datos['W'] = 8
    datos['Peso'] = [2,3,4,5]
    datos['Valor'] = [3,5,6,10]
    return datos

def inicializarSolucion(datos):
    solucion = {}
    solucion['Objetos'] = [0] *datos['N']
    solucion['Peso']=0
    solucion['Valor'] = 0
    return solucion

def esSolucion(solucion,datos):
    return solucion['Peso'] + min(datos['Peso']) > datos['W']

def esFactible(solucion, datos, i):
    return solucion['Peso'] + datos['Peso'][i] <= datos['W']

def mejor(sol1, sol2):
    if sol1['Valor'] > sol2['Valor']:
        mejor = copy.deepcopy(sol1)
    else:
        mejor = copy.deepcopy(sol2)
    return mejor

def asignar(solucion, i, datos):
    solucion['Objetos'][i] +=1
    solucion['Peso'] += datos['Peso'][i]
    solucion['Valor'] += datos['Valor'][i]
    return solucion

def borrar(solucion, i, datos):
    solucion['Objetos'][i]-=1
    solucion['Peso'] -= datos['Peso'][i]
    solucion['Valor'] -= datos['Valor'][i]
    return solucion

def mochilaVA(solucion, mejorSol, datos, k):
    if esSolucion(solucion, datos):
        mejorSol = mejor(mejorSol, solucion)
    else:
        for i in range(k, datos['N']):
            if esFactible(solucion, datos, i):
                solucion = asignar(solucion, i, datos)
                mejorSol = mochilaVA(solucion, mejorSol, datos, i)
                solucion = borrar (solucion, i, datos)
    return mejorSol

#Prog Ppal
datos = inicializarDatos()
solucion = inicializarSolucion(datos)
mejorSol = inicializarSolucion(datos)
mejorSol = mochilaVA(solucion, mejorSol, datos, 0)
print(mejorSol)