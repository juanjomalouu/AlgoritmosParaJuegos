
def doraemonVA(listaObjetos, objetosCogidos, pesoActual, pesoMaximo, valorActual, mejorSolucion):
    if esSolucion(objetosCogidos):
        if valorActual < mejorSolucion:
            mejorSolucion = valorActual
    else:
        N = len(listaObjetos)
        for i in range(N):
            if esFactible(listaObjetos, i, pesoActual, pesoMaximo):
                valorActual += listaObjetos[i]["valor"]
                pesoActual += listaObjetos[objetosPorCoger[i]]["peso"]
                objetoCogido = objetosPorCoger[i]
                objetosPorCoger[i] = -1
                doraemonVA(listaObjetos, objetosPorCoger, pesoActual, pesoMaximo, valorActual, mejorSolucion)
                objetosPorCoger[i] = objetoCogido
    return mejorSolucion

def esSolucion(objetosCogidos):
    return -1 not in objetosCogidos

def esFactible(listaObjetos, objeto, pesoActual, pesoMaximo):
    return objeto != -1 and listaObjetos[objeto]["peso"]+pesoActual <= pesoMaximo

if __name__ == "__main__":
    N, M = list(map(int,input().strip().split()))
    listaObjetos = {}
    listaObjetosCogidos = list()
    for i in range(N):
        id, valor, peso = list(map(int, input().strip().split()))
        listaObjetos[id] = {}
        listaObjetos[id]["valor"] = valor
        listaObjetos[id]["peso"] = peso
        listaObjetosCogidos.append(id)
    print(listaObjetos)
    print(doraemonVA(listaObjetos, listaObjetosCogidos, 0, M, 0, float('inf')))
