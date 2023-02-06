def selectionSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionMax = 0
        for location in range(1,fillslot+1):
            if alist[location]< alist[positionMax]:
                positionMax = location
        temp = alist[fillslot]
        alist[fillslot] = alist[positionMax]
        alist[positionMax] = temp
        
        
alist= [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)