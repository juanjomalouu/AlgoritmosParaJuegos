num = int(input())
numColumna=0
numColumnaInicial=0

for i in range(1, num+1):
    if numColumnaInicial==numColumna:
        print(str(i+1))
        numColumna=0
        numColumnaInicial += 1
    else:
        numColumna+=1
        print(str(i+1), end=" ")
