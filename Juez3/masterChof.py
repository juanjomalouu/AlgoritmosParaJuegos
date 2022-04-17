
def algoritmoVoraz(candidatos, numAlimsSuper, tamanoCesta):
    sol = []
    alimentosCogidos = 0
    sumaSol = 0
    while candidatos != [] and alimentosCogidos < tamanoCesta:
        seleccionado = candidatos[0]
        sol.append(seleccionado)
        sumaSol+=seleccionado[2]
        alimentosCogidos += seleccionado[1]
        candidatos.pop(0)
    return sol,sumaSol

if __name__ == "__main__":
    entrada = input().strip().split()
    numAlimentosSuper = int(entrada[0])
    tamanoCesta = int(entrada[1])
    listaAlimentos = list()
    for i in range(numAlimentosSuper):
        entrada = input().strip().split()
        listaAlimentos.append([entrada[0], int(entrada[1]), int(entrada[2]), int(entrada[2])/int(entrada[1])])
    listaAlimentos.sort(key = lambda x:x[3], reverse=True)

    listaSol,sumaSol = algoritmoVoraz(listaAlimentos, numAlimentosSuper, tamanoCesta)
    print('%.6f' %sumaSol)