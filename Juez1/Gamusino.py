info = input().split()
n = int(info[0])
d = info[2]
s = info[1]

numSpaces = n
numStars = 1
for i in range(0,n):
    print(''.join(char * numSpaces for char in d)+''.join(char * numStars for char in s)+''.join((char * numSpaces for char in d)))
    numSpaces-=1
    numStars+=2
