#List in a List

def two_d_list(players):
    for player in players:
        print("|{0:<12}|{1:<2} |{2:<}|".format(player[0], player[1], player[2]))
        
def width(players, column):
    width = 0
    for item in players:
        if len(item[column]) > length:
               length = len(item[column])
    return length


def all_widths(
#main program

players = [
    ["killmachine", 51 , 49],
    ["Baba", 5 , 99],
    ["haxor12", 72 , 30]]

two_d_list(players)
