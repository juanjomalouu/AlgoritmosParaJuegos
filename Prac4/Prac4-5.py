import random
n = 21
coleccion = list(range(21))
coleccion=[-6,1,32,31,332,3335]
coleccion = [-3, -2, 0,1 ,3,5,6,8]
print(coleccion)


def searchIndex(numData, minIndex, maxIndex):
    index = (maxIndex+minIndex)//2
    if minIndex>maxIndex:
        return False
    if index == numData[index]:
        print(index)
        return True
    elif index < numData[index]:
        return searchIndex(numData,minIndex,index-1)
    else:
        return searchIndex(numData,index+1,maxIndex)

print(searchIndex(coleccion,0,len(coleccion)-1))
