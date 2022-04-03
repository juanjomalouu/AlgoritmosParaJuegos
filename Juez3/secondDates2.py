
def seleccionarMenor():
    indiceMenor = 0
    for i in range(len(listaEdades)):
        if len(listaEdades) != 1:
            if listaEdades[indiceMenor]>listaEdades[i]:
                indiceMenor = i
    retornar = listaNombres[indiceMenor]
    del listaEdades[indiceMenor]
    del listaNombres[indiceMenor]
    return retornar

def algoritmoVoraz(listaNombres, listaEdades, K):
    solucionJovenes = list()
    diffFinal = len(listaEdades) - K
    tamanioGrupoJovenes = diffFinal
    tamanioGrupoMayores = K
    i = 0
    if diffFinal > K:
        tamanioGrupoJovenes = K
        tamanioGrupoMayores = diffFinal
    while len(listaNombres) != 0 and i < tamanioGrupoJovenes:
        menor = seleccionarMenor()
        if menor not in solucionJovenes:
            solucionJovenes.append(listaNombres[menor])
    print()
    while len(listaNombres) != 0 and i < tamanioGrupoJovenes:



















listaNombres = list()
listaEdades = list()
inp = input().split()
N = int(inp[0])
K = int(inp[1])

for i in range(N):
    entrada = input().split()
    listaNombres.append(entrada[0])
    listaEdades.append(entrada[1])

algoritmoVoraz(listaNombres, listaEdades, K)
