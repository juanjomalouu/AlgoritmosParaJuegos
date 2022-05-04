
def sudokuVA(sudo, xIni, yIni):
    if xIni == len(sudo)-1 and yIni == len(sudo):
        esSol = True
    else:
        esSol = False
        if yIni == 9:
            xIni += 1
            yIni = 0
        if sudo[xIni][yIni] != 0:
            sudo, esSol = sudokuVA(sudo, xIni, yIni + 1)
        else:
            posiblesNums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            i = 0
            while not esSol and i < len(posiblesNums):
                if esFactible(sudo, xIni, yIni, posiblesNums[i]):
                    sudo[xIni][yIni] = posiblesNums[i]
                    sudo, esSol = sudokuVA(sudo, xIni, yIni + 1)
                i += 1
            if not esSol:
                sudo[xIni][yIni] = 0
    return sudo, esSol

def esFactible(sudo, xIni, yIni, num):
    return comprobarFilas(sudo, xIni, num) and comprobarColumnas(sudo, yIni, num) and comprobarCuadrado(sudo, xIni, yIni, num)

def comprobarFilas(sudo, xIni, num):
    i = 0
    colocarPieza = True
    while colocarPieza and i < len(sudo):
        if sudo[xIni][i] == num:
            colocarPieza = False
        i+=1
    return colocarPieza

def comprobarColumnas(sudo, yIni, num):
    i = 0
    colocarPieza = True
    while colocarPieza and i < len(sudo):
        if sudo[i][yIni] == num:
            colocarPieza = False
        i+=1
    return colocarPieza

def comprobarCuadrado(sudo, xIni, yIni, num):
    idCuadradoX = 3 * (xIni//3)
    idCuadradoY = 3 * (yIni//3)
    i = idCuadradoX
    colocarPieza = True
    while colocarPieza and i < idCuadradoX+3:
        j = idCuadradoY
        while colocarPieza and j < idCuadradoY+3:
            if sudo[i][j] == num:
                colocarPieza = False
            j+=1
        i+=1
    return colocarPieza

def imprimir(sudo):
    for i in range(len(sudo)):
        for j in range(len(sudo[0])):
            print(sudo[i][j], end=" ")
        print()
    print()
if __name__ == "__main__":
    tamanioSudoku = 9
    sudo = list()
    for i in range(tamanioSudoku):
        sudo.append(list(map(int,input().strip().split())))
    sudo, esSol = sudokuVA(sudo, 0, 0)
    imprimir(sudo)