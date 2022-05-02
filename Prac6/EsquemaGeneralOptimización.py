def VueltaAtras(tupla, k, mejorSol, datos):
    if EsSolucion(tupla):
        mejorSol = mejor(tupla, mejorSol)
    else:
        conjElem = inicializarElementos(datos)
        while conjElem != []:
            [elem, conjElem] = siguiente(conjElem)
            if EsFactible(tupla,elem):
                tupla = asignar(tupla, elem)
                mejorSol = VueltaAtras(tupla, k+1, mejorSol, datos)
                tupla = borrar(tupla,elem)
    return mejorSol 