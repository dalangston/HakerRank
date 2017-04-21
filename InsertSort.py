def printLst(lst):
    for i in lst[:-1]:
        print(i,end=" ")
    print(lst[-1])

Length = int(input())
ar = [int(x) for x in input().split()]
pos = Length -2
Val = ar[-1]

while (pos >= 0) and (ar[pos] > Val):
    ar[pos + 1] = ar[pos]
    printLst(ar)
    pos -= 1
    
ar[pos + 1] = Val
printLst(ar)
