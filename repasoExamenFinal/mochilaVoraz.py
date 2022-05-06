
def mochilaVoraz(infoCartas, pesoMaximo):
    pesoActual = 0
    valorActual = 0
    i = 0
    while infoCartas != [] and pesoActual < pesoMaximo:
        cartaCogida = infoCartas.pop(0)
        pesoActual += cartaCogida[1]
        valorActual += cartaCogida[2]
        print(cartaCogida[0], end=" ")
    return valorActual, pesoActual


if __name__ == "__main__":
    N, M = list(map(int,input().strip().split()))
    infoCartas = list()
    for i in range(N):
        C, R, B = input().strip().split()
        beneficio = int(B)/int(R)
        infoCartas.append([C, int(R), int(B), beneficio])
    print(infoCartas)
    infoCartas.sort(key=lambda x:x[3], reverse=True)

    valor, peso = mochilaVoraz(infoCartas, M)
