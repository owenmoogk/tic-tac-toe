import math

from sqlalchemy import false, true

nextPlayer = {
    'x': 'o',
    "o": 'x'
}

class Game():

    def __init__(self):
        self.board = [[0,0,0],[0,0,0],[0,0,0]]

    def step(self, choice, turn):
        choice -= 1
        choiceRow, choiceCol = math.floor(choice/3), choice%3

        self.board[choiceRow][choiceCol] = turn

    def printBoard(self):
        for i in range(3):
            print(self.board[i])

def tied(board):
    openSlots = getOpenSlots(board)
    for openSlot in openSlots:
        if board[openSlot[0]][openSlot[1]] == 0:
            return False
    return True

def trapSet(board, player):
    openSlots = getOpenSlots(board)
    sum = 0
    for openSlot in openSlots:
        board[openSlot[0]][openSlot[1]] = player
        if isWon(board):
            sum += 1
        board[openSlot[0]][openSlot[1]] = 0 
    if sum >= 2:
        return True
    return False

def isWon(board):

    def checkPattern(input):
        if input:
            return input
        else:
            return False
    
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            return checkPattern(board[i][0])
        if board[0][i] == board[1][i] == board[2][i]:
            return checkPattern(board[0][i])
    if board[0][0] == board[1][1] == board[2][2]:
        return checkPattern(board[0][0])
    if board[2][0] == board[1][1] == board[0][2]:
        return checkPattern(board[1][1])
    return False

def getOpenSlots(board):
    openSlots = []
    for i in range(3):
        for j in range(3):
            if not board[i][j]:
                openSlots.append((i,j))
    return openSlots

def getOptimalMove(board, player):

    openSlots = getOpenSlots(board)

    # if there is one open slot it is the optimal move
    if len(openSlots) == 1:
        return(openSlots[0])

    if len(openSlots) == 8 and board[1][1] == 0:
        return(1,1)
    
    # if we can win then we should
    for openSlot in openSlots:
        board[openSlot[0]][openSlot[1]] = player
        if isWon(board):
            return openSlot
        board[openSlot[0]][openSlot[1]] = 0

    # if they can win then we block
    for openSlot in openSlots:
        board[openSlot[0]][openSlot[1]] = nextPlayer[player]
        if isWon(board):
            return openSlot
        board[openSlot[0]][openSlot[1]] = 0


    # if they can set a trap (two possible new wins in one move) then we should block
    for openSlot in openSlots:
        board[openSlot[0]][openSlot[1]] = nextPlayer[player]
        if trapSet(board, nextPlayer[player]):
            return openSlot
        board[openSlot[0]][openSlot[1]] = 0

    # else move randomly
    return openSlots[0]

def flatten(coords):
    return(coords[0])*3+1+coords[1]

def main():
    game = Game()

    player = 'x'
    while not isWon(game.board):
        
        if player == 'o':
            optimalMove = flatten(getOptimalMove(game.board.copy(), "o"))
            print("optimal move is:", optimalMove)
            game.step(optimalMove, player)
        
        if player == 'x':
            invalidChoice = True
            while invalidChoice:
                choice = int(input("Enter your choice (1-9): "))
                choiceRow, choiceCol = math.floor((choice-1)/3), (choice-1)%3
                if game.board[choiceRow][choiceCol]:
                   print("Invalid Choice!")
                else:
                   invalidChoice = False
            game.step(choice, player)

        game.printBoard()

        if isWon(game.board):
            print("Winner is "+player+"!!")
        if tied(game.board):
            print("The game is a tie!")
            return
        
        player = nextPlayer[player]


if __name__ == "__main__":
    main()