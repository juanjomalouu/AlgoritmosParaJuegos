capturas = int(input())
id = []
punt = []
for peces in range(0, capturas):
    info = input().split()
    id.append(int(info[0]))
    punt.append(int(info[1]))

#Buscamos mayor puntuación
if punt[0]>punt[1]:
    mayorId = id[0]
    mayorPunt = punt[0]
    mayorId2 = id[1]
    mayorPunt2 = punt[1]
else:
    mayorId2 = id[0]
    mayorPunt2 = punt[0]
    mayorId = id[1]
    mayorPunt = punt[1]

for i in range(2, capturas):
    if punt[i] > mayorPunt:
        mayorId2 = mayorId
        mayorPunt2 = mayorPunt
        mayorId = id[i]
        mayorPunt = punt[i]
    elif punt[i] > mayorPunt2:
        mayorId2 = id[i]
        mayorPunt2 = punt[i]


puntuacionFinal = mayorPunt+mayorPunt2
print(mayorId, mayorId2, puntuacionFinal)