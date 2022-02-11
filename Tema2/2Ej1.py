num = int(input("Introduse un numero :D"))
def digitsNumber(n):
    if int(n/10) == 0:
        return 1
    else:
        return 1 + digitsNumber(n/10)

print(digitsNumber(num))