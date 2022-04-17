


def algoritmoVoraz(listaAsignaturas):
    listaTiempos = list()
    for i in range(len(listaAsignaturas)):
        if listaTiempos == []:
            listaTiempos.append(listaAsignaturas[i][1])
        else:
            listaTiempos.append(listaAsignaturas[i][1] + listaTiempos[i-1])
    return listaTiempos

entrada = input().strip().split()
N = int(entrada[0])
M = int(entrada[1])

listaAsignaturas = list()
listaTiempos = list()
for i in range(N):
    listaAsignaturas.append(list(map(int, input().strip().split())))
for i in range(M):
    listaTiempos.append(int(input()))
listaAsignaturas.sort(key = lambda x:x[1])

listaCalculos = algoritmoVoraz(listaAsignaturas.copy())

for i in range(M):
    j=0
    encontrado = False
    sumaTotal = 0
    while j < len(listaCalculos) and encontrado == False:
        sumaTotal += listaCalculos[j]
        if sumaTotal > listaTiempos[i]:
            print(j)
            encontrado=True
        elif sumaTotal == listaTiempos[i]:
            print(j+1)
        if j >= len(listaCalculos) and encontrado == False:
            print(len(listaCalculos))
        j+=1
