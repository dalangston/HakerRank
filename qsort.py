#!/usr/local/bin/python3
    
def qsort(ar, start = 0, end = -1):
    if len(ar) <= 1:
        return ar
    
    if end == -1:
        end = len(ar) -1
    
    pivot = ar[end]
    left = start
    right = end
  
    while left < right:
        while ar[left] < pivot and left < right:
            left += 1
        while ar[right] > pivot and right > left:
            right -= 1
    
        if left == right:
            qsort(ar, start, right - 1)
            qsort(ar, right + 1, end)
        else:
            tmp = ar[right]
            ar[right] = ar[left]
            ar[left] = tmp
      
    return ar


def printList(lst):
    for i in lst[:-1]:
        print(i,end=" ")
    print(lst[-1])

def makeList(listSize = 20, uBound = 100):
    from random import randint
    return [randint(1, uBound) for x in range(listSize)]
  
