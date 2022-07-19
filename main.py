import math

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
    highScore = -math.inf
    optimalMove = None

    # if there is one open slot it is the optimal move
    if len(openSlots) == 1:
        openSlot = openSlots[0]
        board[openSlot[0]][openSlot[1]] = player
        if isWon(board) == 'o':
            board[openSlot[0]][openSlot[1]] = 0
            return(1, openSlot)
        if isWon(board) == 'x':
            board[openSlot[0]][openSlot[1]] = 0
            return(-1, openSlot)
        else:
            board[openSlot[0]][openSlot[1]] = 0
            return(0, openSlot)
    
    # otherwise loop through all the other slots and check them all
    for openSlot in openSlots:
        board[openSlot[0]][openSlot[1]] = player
        score, move = getOptimalMove(board, nextPlayer[player])
        board[openSlot[0]][openSlot[1]] = 0

        # we invert the score because it is for the other player
        # ie if a 1 is returned, this means the other guy will win, so we want it to show as a loss
        score *= -1
        if score > highScore:
            highScore = score
            optimalMove = move

    return highScore, optimalMove

def flatten(coords):
    return(coords[0])*3+1+coords[1]

def main():
    game = Game()

    player = 'x'
    while not isWon(game.board):
        
        if player == 'o':
            optimalMove = flatten(getOptimalMove(game.board.copy(), "o")[1])
            print("optimal move is:", optimalMove)
            game.step(optimalMove, player)
        
        if player == 'x':
            invalidChoice = True
            while invalidChoice:
                choice = int(input("Enter your choice (1-9): "))
                choiceRow, choiceCol = math.floor((choice-1)/3), (choice-1)%3
                print(choiceRow, choiceCol)
                if game.board[choiceRow][choiceCol]:
                   print("Invalid Choice")
                else:
                   invalidChoice = False
            game.step(choice, player)

        game.printBoard()

        if isWon(game.board):
            print("Winner is "+player+"!!")
        
        player = nextPlayer[player]


if __name__ == "__main__":
    main()