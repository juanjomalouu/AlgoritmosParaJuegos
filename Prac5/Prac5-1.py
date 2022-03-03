
def ordenar(coleccion):



def planTareasVoraz(datos):
    solucion = []
    datos = ordenar(datos)
    i = 0
    while i < len(datos):
        solucion.append(datos[i][0])
        i+=1
    return solucion


datos = [[1,5], [2,10], [3,3]]
print(datos)

plan = planTareasVoraz(datos)
print(plan)