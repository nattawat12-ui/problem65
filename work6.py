#Shell sort 
list1 = []
def InputScore ():
    for i in range(int(input('How many students to input score: '))):
        list1.append(int(input(f'Score {i+1}: ')))

def showscore (arr):
    reversed_list = arr[::-1]
    last_three = reversed_list[:3]
    print('top 3 highest',shell_sort(list1[0:3]))
    print("top 3 lowest ",last_three)
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] < temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr
InputScore()
print(shell_sort(list1)) 
showscore(list1)
print(list1.count(int(input('How many this score: '))))
