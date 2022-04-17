
def algoritmoVoraz(candidatos, numActividades):
    sol = []
    horasDeSeleccionados = list()
    while candidatos != [] and len(sol) != numActividades:
        seleccionado = candidatos[0]
        if seleccionado[2] not in horasDeSeleccionados:
            sol.append(seleccionado)
            horasDeSeleccionados.append(seleccionado[2])
        candidatos.pop(0)
    return sol

if __name__ == "__main__":
    entrada = list(map(int,input().strip().split()))
    numActividades = entrada[0]
    horasTotales = entrada[1]
    beneficioMaximo = entrada[2]

    listaActividades = list()
    for i in range(numActividades):
        entrada = list(input().strip().split())
        listaActividades.append([entrada[0],int(entrada[1]),int(entrada[2])])

    listaActividades.sort(key = lambda x:x[1], reverse = True)

    listaSeleccionados = algoritmoVoraz(listaActividades, horasTotales)
    sumaBeneficio = 0
    for i in range(len(listaSeleccionados)):
        print(listaSeleccionados[i][0])
        sumaBeneficio+=listaSeleccionados[i][1]
    if sumaBeneficio >= beneficioMaximo:
        print(":)")
    else:
        print(":(")

