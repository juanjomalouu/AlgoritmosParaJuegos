
def algoritmoVoraz(comida, coste):
    costeActual = 0
    alimentosCogidos = list()
    valorTotal = 0
    while len(comida) != 0 and costeActual < coste:
        costeActual += comida[0][1]
        valorTotal += comida[0][2]
        comida.pop(0)
    return valorTotal

#PPal
if __name__ == "__main__":
    N, C = list(map(int,input().strip().split()))
    listaAlimentos = list()
    for i in range(N):
        infoComida = input().strip().split()
        nombre = infoComida[0]
        tamanio = int(infoComida[1])
        valor = int(infoComida[2])
        beneficio = valor/tamanio
        listaAlimentos.append([nombre,tamanio,valor, beneficio])

    print(listaAlimentos)
    listaAlimentos.sort(key= lambda x: x[3], reverse=True)

    print(algoritmoVoraz(listaAlimentos, C))