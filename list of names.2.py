#Ashley Nkomo
#Lists Revision Exercise 1

names = []
maxLenghtList = 6

while len(names) < maxLenghtList:
    name = input("Please enter a name to add to the list: ")
    names.append(name)
    print(names)
    
print("")

print("Please enter the range for the selection you want")
one = int(input(":"))
two = int(input(":"))

print("")

selection = names[one:two]
print(selection)
