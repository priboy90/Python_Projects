import os
import random
def FindBot(x,y,field):
    bot = [len(field)/2, len(field[0])/2]
    minimal = 9900
    for i in range(len(field)):
        for j in range(len(field[0])):
            if field[i][j] != 0 and (i != x or j != y):
                if minimal > min(abs(x - i), abs(y - j)):
                    minimal = min(abs(x - i), abs(y - j))
                    bot = [i, j]
    return bot

def GoToPoint(x, y, bX, bY):
    if(x == bX):
        if(y < bY):
            return "fire_down"
        else:
            return "fire_up"
    elif(y == bY):
        if(x > bX):
            return "fire_left"
        else:
            return "fire_right"

    if (abs(bY - y) < abs(bX - x)):
        if (y < bY):
            return "go_down"
        else:
            return "go_up"
    else:
        if (x > bX):
            return "go_left"
        else:
            return "go_right"

def make_choice(x,y,field):
    #bX, bY = FindBot(x,y,field)

    dataLine = ""
    with open('bots/djdjdfilfefegifjeofjeifjeoigjieojgeiorjgrijergjrierjgierge.n', 'r') as f:
        dataLine = f.readline()

    if dataLine != "":
        words = dataLine.split()
        return GoToPoint(x, y, int(words[0]), int(words[1]))

    os.mknod("bots/djdjdfilfefegifjeofjeifjeoigjieojgeiorjgrijergjrierjgierge.n")
    file = open('bots/djdjdfilfefegifjeofjeifjeoigjieojgeiorjgrijergjrierjgierge.n', 'w')
    bX, bY = FindBot(x, y, field)
    file.write(bX + " " + bY)

    return GoToPoint(x, y, bX, bY)

if __name__ == "__main__":
    make_choice(0, 0, [[0, 0, 0], [0, 0, 0], [0, 0, 0]])

'''
def make_choice(x,y,field):
    return "go_right"'''
'''return random.choice(["go_right","go_left","go_up","go_down",
                     "fire_right","fire_right","fire_right","fire_right"])'''
