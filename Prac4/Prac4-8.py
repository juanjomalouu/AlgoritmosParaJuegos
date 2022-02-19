x=int(input())
a=int(input())

def calculoPotencia(x,a):
    if a==1:

        return x
    elif a==0:
        return 1
    elif a%2==0:
        aux =calculoPotencia(x,a//2)
        return aux * aux
    else:
        return x*calculoPotencia(x,a-1)



print(calculoPotencia(x,a))