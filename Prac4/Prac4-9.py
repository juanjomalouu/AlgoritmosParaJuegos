
from random import randint
tamanio = int(input())

def GenerateRandomList(A,n):
    for i in range(n):
        k = randint(-20,20)
        A.append(k)
    return A

def maxConsecutiveArray(A,minIndex,maxIndex):
    
    if(minIndex==maxIndex)
        return A[minIndex]
    else

n = int(input())
A = list()
A = GenerateRandomList(A,n)
print(maxConsecutiveArray(A,0,len(A)-1))