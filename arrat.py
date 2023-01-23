
import array as arr
def makeArray(n):
    print ("Array before insertion : ", end =" ")
    for i in range
    '''for i in range(n):
        arr.append(i)
    return arr'''
def insert_into_array(arr, index, element):
    arr.insert(index, element)
    return arr
def delete_from_array(arr, index):
    del arr[index]
    return arr
print(insert_into_array(makeArray(4),2,99))
print(delete_from_array(insert_into_array(makeArray(10),3,7),2))