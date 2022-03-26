
def inicializar():
    fila = [0]*9
    instancia = []
    for i in range(9):
        instancia.append(fila[:])
    instancia[0][1] = 6
    instancia[0][3] = 1
    instancia[0][5] = 4
    instancia[0][7] = 5
    instancia[1][2] = 8
    instancia[1][3] = 3
    instancia[1][5] = 5
    instancia[1][6] = 6
    instancia[2][0] = 2
    instancia[2][8] = 1
    instancia[3][0] = 8
    instancia[3][3] = 4
    instancia[3][5] = 7
    instancia[3][8] = 6
    instancia[4][2] = 6
    instancia[4][6] = 3
    instancia[5][0] = 7
    instancia[5][3] = 9
    instancia[5][5] = 1
    instancia[5][8] = 4
    instancia[6][0] = 5
    instancia[6][8] = 2
    instancia[7][2] = 7
    instancia[7][3] = 2
    instancia[7][5] = 6
    instancia[7][6] = 9
    instancia[8][1] = 4
    instancia[8][3] = 5
    instancia[8][5] = 8
    instancia[8][7] = 7
    return instancia

def imprimir(sudoku):
    for f in range(len(sudoku)):
        for c in range(len(sudoku[0])):
            print(sudoku[f][c],end=' ')
        print()
    print()

def indexToCoord(i,length):
    f=i//length
    c=i%length
    return f,c

def esSolucion(sudoku,i):
    return i >= len(sudoku)**2

def esFactible(sudoku,f,c,num):
    filaOk = comprobarFila(sudoku, f, c, num)
    colOk = comprobarColumna(sudoku, f, c, num)
    bloqueOk = comprobarBloque(sudoku, f, c, num)

    return filaOk and colOk and bloqueOk

def comprobarColumna(sudoku,c,num):
    colOk = True
    i = 0
    while colOk and i < len(sudoku):
        colOk = sudoku[i][c] != num
        i+=1
    return colOk

def comprobarBloque(sudoku,f,c,num):
    bloqueOk = True
    iniF = 3*(f//3)
    iniC = 3*(c//3)
    i = iniF
    while bloqueOk and i < iniF + 3:
        j = iniC
        while bloqueOk and j < iniC + 3:
            bloqueOk =

def solverSudokuVA(sudoku,i):
    if esSolucion(sudoku,i):
        esSol = True
    else:
        esSol = False
        f,c = indexToCoord(i)
        if sudoku[f][c] != 0:
            sudoku, esSol = solverSudokuVA(sudoku, i+1)
        else:
            num = 1
            while not esSol and num <= 9:
                if esFactible(sudoku, f,c,num):
                    sudoku[f][c] = num
                    sudoku, esSol = solverSudokuVA(sudoku, i +1)
                num += 1
            if not esSol:
                sudoku[f][c] = 0

    return sudoku, esSol

sudoku = inicializar()
imprimir(sudoku)
i = 0
sudoku, esSol = solverSudokuVA(sudoku,i)
if esSol:
    imprimir(sudoku)
else:
    print('Este sudoku está mal hecho')