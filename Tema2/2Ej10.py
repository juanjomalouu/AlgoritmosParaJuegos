n1 = int(input())
m1= int(input())

def combinaciones (n,m):
    val = 0
    if n == m or m == 0:
        val = 1
    else:
        val += combinaciones(n-1,m)
        val += combinaciones(n-1,m-1)
    return val


print(combinaciones(n1,m1))