import random

steps = [0,1,2,3]
starterN = 2
length = 4
board = []
pboard = []

def createBoard():
    for i in range(0, length):
        board.append([0,0,0,0])
        pboard.append([0,0,0,0])

def startGame():
    for i in range(0, starterN):
        n1 = random.randint(0, length-1)
        n2 = random.randint(0, length-1)
        if board[n1][n2] == 2:
            createBoard()
        else:
            board[n1][n2] = 2

def check2048():
    for i in range(0, length):
        for j in range(0, length):
            if board[i][j] == 2048:
                print "You've reached 2048! What a massive waste of time!"

def checkAnyDown():
    for i in range(0, length):
        for j in range(0, length):
            if board[i][j] != 0:
                if i == 3:
                    board[i][j] = board[i][j]
                elif board[i+1][j] == board[i][j] or board[i+1][j] == 0:
                    return True
                else:
                    return False
            elif board[i][j] == 0:
                return True
            else:
                return False

def checkAnyUp():
    for i in reversed(steps):
        for j in reversed(steps):
            if board[i][j] != 0:
                if i == 0:
                    board[i][j] = board[i][j]
                elif board[i-1][j] == board[i][j] or board[i-1][j] == 0:
                    return True
                else:
                    return False
            elif board[i][j] == 0:
                return True
            else:
                return False

def checkAnyRight():
    for i in range(0, length):
        for j in range(0, length):
            if board[i][j] != 0:
                if j == 3:
                    board[i][j] = board[i][j]
                elif board[i][j+1] == board[i][j] or board[i][j+1] == 0:
                    return True
                else:
                    return False
            elif board[i][j] == 0:
                return True
            else:
                return False

def checkAnyLeft():
    for i in reversed(steps):
        for j in reversed(steps):
            if board[i][j] != 0:
                if j == 0:
                    board[i][j] = board[i][j]
                elif board[i][j-1] == board[i][j] or board[i][j-1] == 0:
                    return True
                else:
                    return False
            elif board[i][j] == 0:
                return True
            else:
                return False
                
                
def spawn1():
    temp = []
    for i in range(0, length):
        for j in range(0, length):
            if board[i][j] == 0:
                temp.append([i, j])
    n = random.randint(0, len(temp))
    for i in range(0, len(temp)):
        if i == n:
            board[(temp[n][0])][(temp[n][1])] = 2*random.randint(1,2)
            
def getpBoard():
    for i in range(0, length):
        for j in range(0, length):
            pboard[i][j] = board[i][j]

def showBoard():
    for i in range(0, length):
        print board[i]

def nextMove():
    check2048()
    if checkAnyUp() == False:
        if checkAnyDown() == False:
            if checkAnyLeft() == False:
                if checkAnyRight() == False:
                    lose()
                else:
                    nextMoveAlg()
            else:
                nextMoveAlg()
        else:
            nextMoveAlg()
    else:
        nextMoveAlg()

def nextMoveAlg():
    getpBoard()
    move = raw_input(":")
    if move == "down":
        down()
        if board != pboard:
            spawn1()
        showBoard()
        nextMove()
    elif move == "up":
        up()
        if board != pboard:
            spawn1()
        showBoard()
        nextMove()
    elif move == "right":
        right()
        if board != pboard:
            spawn1()
        showBoard()
        nextMove()
    elif move == "left":
        left()
        if board != pboard:
            spawn1()
        showBoard()
        nextMove()
    else:
        print "bad command"
        nextMove()

def getTemp():
    for i in range(0, length):
        temp.append([0,0,0,0])
    for i in range(0, length):
        for j in range(0, length):
            temp[i][j] = board[i][j]

def lose():
    print "You lose"
    board = []
    quit()

def down():
    for i in range(0, length):
        for j in range(0, length):
            if board[i][j] != 0:
                if i == 3:
                    board[i][j] = board[i][j]
                elif board[i+1][j] == board[i][j]:
                    board[i+1][j] = board[i][j] + board[i+1][j]
                    board[i][j] = 0
                elif board[i+1][j] == 0:
                    board[i+1][j] = board[i][j]
                    board[i][j] = 0
                    down()

def up():
    for i in reversed(steps):
        for j in reversed(steps):
            if board[i][j] != 0:
                if i == 0:
                    board[i][j] = board[i][j]
                elif board[i-1][j] == board[i][j]:
                    board[i-1][j] = board[i][j] + board[i-1][j]
                    board[i][j] = 0
                elif board[i-1][j] == 0:
                    print "did 3"
                    board[i-1][j] = board[i][j]
                    board[i][j] = 0
                    up()

def right():
    for i in range(0, length):
        for j in range(0, length):
            if board[i][j] != 0:
                if j == 3:
                    board[i][j] = board[i][j]
                elif board[i][j+1] == board[i][j]:
                    board[i][j+1] = board[i][j] + board[i][j+1]
                    board[i][j] = 0
                elif board[i][j+1] == 0:
                    board[i][j+1] = board[i][j]
                    board[i][j] = 0
                    right()
def left():
    for i in reversed(steps):
        for j in reversed(steps):
            if board[i][j] != 0:
                if j == 0:
                    board[i][j] = board[i][j]
                elif board[i][j-1] == board[i][j]:
                    board[i][j-1] = board[i][j] + board[i][j-1]
                    board[i][j] = 0
                elif board[i][j-1] == 0:
                    board[i][j-1] = board[i][j]
                    board[i][j] = 0
                    left()

def start():
    createBoard()
    startGame()
    showBoard()
    nextMove()

print "Welcome to 2048! Get a block that says 2048 on it to win."
start()
