#I got bored yesterday, so I made this.
#In general, it works pretty much the same. type in the direction you would "swipe" in.
#if a part of the list is 0, that means it's empty.

import random #uses random stuff, so i imported this

steps = [0,1,2,3] #this is used for later
starterN = 2 #number of 2's to spawn at the beginning
length = 4 #length of the x/y axis
board = [] #board list
pboard = [] #used to copy the board later

def createBoard():
    #creates a 4x4 list of 0's for board and pboard
    for i in range(0, length):
        board.append([0,0,0,0])
        pboard.append([0,0,0,0])

def startGame():
    #gets random positions for the starting numbers.
    for i in range(0, starterN):
        n1 = random.randint(0, length-1)
        n2 = random.randint(0, length-1)
        if board[n1][n2] == 2:
            #not really necessary, but just a check
            createBoard()
        else:
            board[n1][n2] = 2

def check2048():
    #checker that runs every time a move is made so that it responds when 2048 appears
    for i in range(0, length):
        for j in range(0, length):
            if board[i][j] == 2048:
                print "You've reached 2048! What a massive waste of time!"

#the next 4 methods are used for checking if there is any possiblity of movement.  
def checkAnyDown():
    for i in range(0, length):
        for j in range(0, length):
            #Finds valid blocks
            if board[i][j] != 0:
                #This keeps array index out of bounds errors from occuring
                if i == 3:
                    board[i][j] = board[i][j]
                #Checks if there is a 0 or the same number below.
                elif board[i+1][j] == board[i][j] or board[i+1][j] == 0:
                    return True
                else:
                    return False
            #Checks if the board is full or not
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
                
#After a move is made, the game spawns a new number, a 2 or 4, in a random blank spot     
def spawn1():
    #temp just keeps track of the blank spots
    temp = []
    for i in range(0, length):
        for j in range(0, length):
            if board[i][j] == 0:
                temp.append([i, j])
    #random number determines which temp var, which determines where the new number spawns
    n = random.randint(0, len(temp))
    for i in range(0, len(temp)):
        if i == n:
            board[(temp[n][0])][(temp[n][1])] = 2*random.randint(1,2)

#gets used later, stands for "Get Previous Board"
def getpBoard():
    for i in range(0, length):
        for j in range(0, length):
            pboard[i][j] = board[i][j]

#Updates user with current board
def showBoard():
    for i in range(0, length):
        print board[i]

#Allows the user to make a move
#Yes, there is probably a better way to do this, but it just checks if there is any movement possibility
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

#Allows input via raw input. once move is sent, it checks if it is the same board as 1 move prior. If so, it doesn't spawn a new number
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

#You lost the game. the program quits out.
def lose():
    print "You lose"
    board = []
    quit()

#The next 4 methods are when you send a valid move.
def down():
    for i in range(0, length):
        for j in range(0, length):
            #Excludes blanks from checker
            if board[i][j] != 0:
                #Avoids index out of bounds errors
                if i == 3:
                    board[i][j] = board[i][j]
                #If it is the same number below, add them, and remove the previous number
                elif board[i+1][j] == board[i][j]:
                    board[i+1][j] = board[i][j] + board[i+1][j]
                    board[i][j] = 0
                #If it is blank below, set the blank to the number, and remove the previous number
                elif board[i+1][j] == 0:
                    board[i+1][j] = board[i][j]
                    board[i][j] = 0
                    #Does it again to move it all the way down
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

#Starts the game by running commands
def start():
    createBoard()
    startGame()
    showBoard()
    nextMove()

#Welcome message and starting the program
print "Welcome to 2048! Get a block that says 2048 on it to win."
start()
