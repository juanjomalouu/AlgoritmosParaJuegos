num = int(input())
def addSum (n):
    if n == 1:
        return 1
    else:
        return 1/n + addSum(n-1)

print(addSum(num))