n2 = input()

def recCadena(n):
    if(len(n)!=0):
        print(n[len(n)-1],end="")
        n = n[:-1]
        recCadena(n)

recCadena(n2)