import numpy as np

def inicializarLaberinto():
    laberinto = np.zeros([10,10])
    paredes = np.array([[0,2],[0,7],[1,0],[1,2],[1,5],[1,6],[1,8],[2,6],
                       [2,8],[3,1],[3,4],[3,5],[3,6],[4,2],[4,3],[4,7],
                       [5,5],[5,7],[6,0],[6,3],[6,4],[6,7],[6,9],[7,1],
                       [7,2],[7,8],[7,9],[8,2],[8,4],[8,5]])
    laberinto[paredes[:,0], paredes[:,1]] = np.inf
    return laberinto

def salirDelLaberinto(laberinto,f,c,k):
    if f == np.size(laberinto,0)-1 and  c== np.size(laberinto,1)-1:
        esSol = True
    else:
        esSol = False
        mov = np.array([[1,0],[0,1],[-1,0],[0,-1]])
        i = 0
        while not esSol and i < np.size(mov,0):
            if esFactible(laberinto, f+mov[i,0],c+mov[i,1]):
                laberinto[f+mov[i,0],c+mov[i,1]] = k
                [laberinto, esSol] = \
                    salirDelLaberinto(laberinto, f+mov[i,0], c+mov[i,1], k+1)
                if not esSol:
                    laberinto[f+mov[i,0], c+mov[i,1]] = 0
            i+=1
    return [laberinto, esSol]

def esFactible(lab, f,c):
    return f>= 0 and f < np.size(lab, 0) \
           and c>= 0 and c < np.size(lab,1) and lab[f][c] == 0

#Prog ppal:
lab = inicializarLaberinto()

Xini = 0
Yini = 0
paso = 1

lab[Xini, Yini] = paso
[lab, esSol] = salirDelLaberinto(lab, Xini, Yini, paso+1)
if esSol:
    print(lab)
else:
    print('No se ha encontrado la salida del laberinto')