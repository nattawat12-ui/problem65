scores = {}
def InputScore(name):
        score=int(input(f"Enter the score for {name}: "))
        scores[name] = score
            
        
def searcScore(name):
    if name in scores:
        print(f"The score of {name} is {scores[name]} point ")
    else:
        print(f"name is not found in data")
def CountData():
    print(f"The number of student in the score is {len(scores)}")
def ShowScore():
    sortedScore = sorted(scores.items(),key=lambda x: x[1])
    for name, score in sortedScore:
        print(f"{name}: {score}")
num = 0
while num != 5:
    num = int(input('Enter choice:'))
    if num == 1:
        repeat = 'Y'
        while repeat=="Y" :
                name = str(input("Enter the name "))
                InputScore(name)
                break
        repeate = input('Enter Y for repeate program: ')
        
    if num == 2:
        name = str(input("Enter the name "))
        searcScore(name)
        
    if num==3:
        CountData()
        
    if num==4:
        ShowScore()
        

'''
while True:
    name = input("Enter the name of the student :")
    if not name:
        break
    InputScore(name)
name = input("Enter serching the score:")
searcScore(name)

CountData()
ShowScore()'''
