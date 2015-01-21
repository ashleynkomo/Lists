#Ashley Nkomo
#Cypher code

Type = input("Would you like to cypher or decypher? ")
if Type == "decypher":
    Type = 1
else:
    Type = 2


def char(message):
    counter = 0
    for character in message:
        char_cypher = message[counter]
        counter +=1
        cypher(char_cypher, Type)
 

def cypher(char_cypher, Type):
    ASCII = ord(char_cypher)
    if Type == 1:
        if ASCII != 32:
            ASCII = ASCII - 3
        else:
            ASCII == ASCII
        text_changed = chr(ASCII)
        text_changed.split()
    else:        
        if ASCII != 32:
            ASCII = ASCII + 3
        else:
            ASCII == ASCII
        text_changed = chr(ASCII)
        text_changed.split()
             
    print(text_changed, end = "")
 

#main program 
message = input("Please input a message to cypher or decypher: ")
char(message)
