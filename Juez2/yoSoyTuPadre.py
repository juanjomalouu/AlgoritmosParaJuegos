N = int(input())
identificadoresFamiliares = list()
for i in range(0, N):
    identificadoresFamiliares.append(list(map(int, input().strip().split(" "))))

M = int(input())
consultas = list()
for i in range(0, M):
    consultas.append(int(input()))



def consultarNivel(consulta, familiarIndex, indice):
    suma = 0
    if consulta == familiarIndex[0]:
        suma = 1
    elif len(familiarIndex) == 1:
        suma = -1
    else:
        for i in range(1, len(familiarIndex)):
            indice += i
            suma = consultarNivel(consulta, identificadoresFamiliares[indice], indice)
            suma+=1
        suma+=1
    return suma

for i in consultas:
    print(consultarNivel(i,identificadoresFamiliares[0],0))

