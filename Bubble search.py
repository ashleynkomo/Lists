#Bubble Sort

def Bubble_Sort(List):
    sort = False
    n = len(List)
    while  sort == False:
        sort = True
        for person in range (0,n-1):
            if List[person] > List[person + 1]:
                temp = List[person]
                List[person] = List[person + 1]
                List[person + 1] = temp
                sort = False
    print(List)
            


#main program
List = ["John", "James", "Billy", "Ashley","Hulk Hogan","Billy Joel","Sharkeisha"]
Bubble_Sort(List)    
