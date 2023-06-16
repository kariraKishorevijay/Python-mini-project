# tick toe game
board=['-','-','-',
       '-','-','-',
       '-','-','-']
currPlayer="x"
winner=None
gameRunning=True

#code for printing board
def printBoard(board):
    print(board[0]+"|"+board[1]+"|"+board[2])
    print("-"*10)
    print(board[3]+"|"+board[4]+"|"+board[5])
    print("-"*10)
    print(board[6]+"|"+board[7]+"|"+board[8])
    print("-"*10)

#taking input 
def playerInput(board):
    while True:
        if currPlayer=="x":
            inp=int(input(f"enter a position 1-9\033[1;34m player(x)\033[0;0m:" ))
        else:
            inp=int(input(f"enter a position 1-9\033[1;31m player(0)\033[0;0m:"))
        if inp>=1 and inp<=9 and board[inp-1]=='-':
            board[inp-1]=currPlayer
            break
        else:
            if currPlayer=="x":
                print("try again")
            else:
                print("try again")
        printBoard(board)

#check for winner or tie
def checkHor(board):
    global winner
    if(board[0]==board[1]==board[2] and board[0]!="-") or(board[3]==board[4]==board[5] and board[3]!="-") or (board[7]==board[8]==board[6] and board[6]!="-"):
        winner=currPlayer
        return True
def checkVer(board):
    global winner
    if(board[0]==board[3]==board[6] and board[0]!="-") or (board[1]==board[4]==board[7] and board[1]!="-") or (board[2]==board[8]==board[5] and board[2]!="-"):
        winner=currPlayer
        return True
def checkDiag(board):
    global winner
    if(board[0]==board[4]==board[5] and board[0]!="-") or(board[2]==board[4]==board[6] and board[2]!="-"):
        winner=currPlayer
        return True
def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("its a tie")
        gameRunning=False
def checkWin():
    if checkDiag(board) or checkHor(board) or checkVer(board):
        print("the winner is  ",winner)

#switching the player
def switchPlayer():
    global currPlayer
    if currPlayer=="x":
        currPlayer="o"
    else:
        currPlayer="x"

while gameRunning:
    printBoard(board)
    if winner!=None:
        break
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
