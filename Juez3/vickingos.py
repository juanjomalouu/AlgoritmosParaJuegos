infoInicial = input().split()
numSeries =int(infoInicial[0])
tiempoDisponible = int(infoInicial[1])

listaBeneficios = list()
listaNombresSeries = list()
listaNotasSeries = list()
listaDuracionSeries = list()

for i in range(0,numSeries):
    infoSerie = input().split()
    listaNombresSeries.append(infoSerie[0])
    listaNotasSeries.append(int(infoSerie[1]))
    listaDuracionSeries.append(int(infoSerie[2]))
    listaBeneficios.append(int(infoSerie[1])/int(infoSerie[2]))

listaCandidatos=listaNombresSeries[:]

def mochilaVoraz(candidatos, tiempoDisponible):
    sol = list()
    puntuacionTotal=0
    while tiempoDisponible>0 and len(candidatos)>0:
        seleccionadoId = mejorCandidato(candidatos)
        sol.append(seleccionadoId)
        if tiempoDisponible > listaDuracionSeries[seleccionadoId]:
            tiempoDisponible -= listaDuracionSeries[seleccionadoId]
            puntuacionTotal += listaNotasSeries[seleccionadoId]
        else:
            puntuacionTotal += listaNotasSeries[seleccionadoId] * tiempoDisponible//100
            tiempoDisponible = 0
    return sol, puntuacionTotal

def mejorCandidato(candidatos):
    idCandidato = 0
    beneficioMayor = listaBeneficios[0]
    for i in range(0,len(candidatos)):
        if listaBeneficios[i]>beneficioMayor:
            beneficioMayor = listaBeneficios[i]
            idCandidato = i
    del listaBeneficios[i]
    del candidatos[i]
    return idCandidato



listaSeleccionados, puntuacionTotal = mochilaVoraz(listaCandidatos, tiempoDisponible)

listaSeleccionados.sort()
for i in listaSeleccionados:
    print(listaNombresSeries[i])
print(puntuacionTotal)



