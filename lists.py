#Ashley Nkomo
#Lists R&R
#11/12/14

name = ["","","","","","","",""]

def output(name):
    count = 1
    for blahh in name:
        print("{0}. {1}".format(count,blahh))
        count = count + 1

name[0] = input("Please enter the name of the first student: ")
name[1] = input("Please enter the name of the second student: ")
name[2] = input("Please enter the name of the third student: ")
name[3] = input("Please enter the name of the fourth student: ")
name[4] = input("Please enter the name of the fifth student: ")
name[5] = input("Please enter the name of the sixth student: ")
name[6] = input("Please enter the name of the seventh student: ")
name[7] = input("Please enter the name of the eighth student: ")

output(name)

name.insert(int(input("Please enter the student to edit: ")),(input("Please enter their new name: ")))

output(name)


