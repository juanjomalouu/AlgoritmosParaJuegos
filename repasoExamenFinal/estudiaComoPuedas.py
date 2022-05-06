import copy

def tiempoVoraz(datos):
    asignaturasInfo = list()
    for i in range(len(datos)):
        if len(asignaturasInfo) == 0:
            asignaturasInfo.append(datos[0][1])
        else:
            asignaturasInfo.append(datos[0][1] + asignaturasInfo[-1])
        datos.pop(0)
    return asignaturasInfo

def tiempoVorazSolo(datos):
    asignaturasInfo = list()
    for i in range(len(datos)):
        if len(asignaturasInfo) == 0:
            asignaturasInfo.append(datos[0])
        else:
            asignaturasInfo.append(datos[0] + asignaturasInfo[-1])
        datos.pop(0)
    return asignaturasInfo

def sumar (lista):
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    return suma

def calcularCantidad(tiempos, hora):
    i = 0
    encontrado = False
    sol = 0
    while i < len(tiempos) and not encontrado:
        if tiempos[i] > hora:
            encontrado = True
            sol = i
        i+=1
    if not encontrado:
        sol = len(tiempos)
    return sol

if __name__ == "__main__":
    N, M = list(map(int,input().strip().split()))
    datos = list()
    horas = list()
    for i in range(N):
        datos.append(list(map(int,input().strip().split())))
    datos.sort(key=lambda x:x[1])
    for i in range(M):
        horas.append(int(input()))

    for i in range(M):
        listaTiemposFinales = tiempoVoraz(copy.deepcopy(datos))
        tiempos = tiempoVorazSolo(listaTiemposFinales)
        print(calcularCantidad(tiempos, horas[i]))
