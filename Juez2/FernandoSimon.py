info = input().split();
numCamas = list()
nombres = list()
umbral = list()

for i in range(0,int(info[0])):
    comunidadInfo = input().split()
    numCamas.append(int(comunidadInfo[0]))
    nombres.append(comunidadInfo[1])

for i in range(0,int(info[1])):
    umbral.append(int(input()))

for i in umbral:
    comunidadProxima = 0

    for j in range(0, int(info[0])):
        if numCamas[j] >= i:
            if comunidadProxima == 0:
                comunidadProxima=numCamas[j]
                index=j
            elif numCamas[j] < comunidadProxima:
                comunidadProxima = numCamas[j]
                index = j
    print(nombres[index])


