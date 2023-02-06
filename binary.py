def binarySerch(alist , item):
    first = 0
    last = len(alist)-1
    found = False
    a = 0
    while first<=last and not found:
        midpoint = (first+last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
        a+=1
    
    return found,a
testlist = [17,20,26,31,44,54,55,65,77,93]
print(binarySerch(testlist,55))