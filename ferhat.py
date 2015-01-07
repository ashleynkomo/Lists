names = ["","","","","","","",""]

def output(names):
    count = 1
    for each in names:
        print("{0}. {1}".format(count,each))
        count = count + 1

names[0] = input("Please enter the name of the first student: ")
names[1] = input("Please enter the name of the second student: ")
names[2] = input("Please enter the name of the third student: ")
names[3] = input("Please enter the name of the fourth student: ")
names[4] = input("Please enter the name of the fifth student: ")
names[5] = input("Please enter the name of the sixth student: ")
names[6] = input("Please enter the name of the seventh student: ")
names[7] = input("Please enter the name of the eighth student: ")

output(names)

changed = int(input("Please select a student to edit: "))
changed = changed - 1

print()


names[changed] = input("Please enter the new name: ")

print()



output(names)
