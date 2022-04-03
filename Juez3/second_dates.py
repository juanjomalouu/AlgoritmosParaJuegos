
def seleccionarMenor():
    indiceMenor = 0
    for i in range(1,len(listaEdades)):
        if len(listaEdades) != 1:
            if listaEdades[indiceMenor]>listaEdades[i]:
                indiceMenor = i
    print(listaNombres[indiceMenor],end=" ")
    del listaEdades[indiceMenor]
    del listaNombres[indiceMenor]

def ordenacionListas(K):
    diffFinal = len(listaEdades)-K
    tamanioGrupoJovenes = diffFinal
    if diffFinal > K:
        tamanioGrupoJovenes = K
    i = 0
    while len(listaEdades) != 0 and i < tamanioGrupoJovenes:
        seleccionarMenor()
        i+=1
    print()
    while len(listaEdades) != 0:
        seleccionarMenor()

def ordenarListas(listaInfo):
    listaInfo = sorted(listaInfo, key = lambda x:x[1])
    diffFinal = len(listaInfo)-K
    tamanioGrupoJovenes = diffFinal
    if diffFinal > K:
        tamanioGrupoJovenes = K
    i = 0
    while len(listaEdades) != 0 and i < tamanioGrupoJovenes:
        print(listaInfo[i][0],end=" ")
        i+=1
    print()
    while len(listaEdades) != 0 and i < len(listaInfo):
        print(listaInfo[i][0],end=" ")
        i+=1

listaInformacion = list()
inp = input().split()
N = int(inp[0])
K = int(inp[1])

for i in range(N):
    listaEdades = list()
    entrada = input().split()
    listaEdades.append(entrada[0])
    listaEdades.append(int(entrada[1]))
    listaInformacion.append(listaEdades)
ordenarListas(listaInformacion)

