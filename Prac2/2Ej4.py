num = int(input())
def addNatural (n):
    if n == 0:
        return n
    else:
        return n + addNatural(n-1)

print(addNatural(num))