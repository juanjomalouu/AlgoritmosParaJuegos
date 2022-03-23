num = int(input())
def addDigits (n):
    if n/10 == 0:
        return n%10
    else:
        return n%10 + addDigits(int(n/10))

print(addDigits(num))