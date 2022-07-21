import math

nextPlayer = {
    'x': 'o',
    "o": 'x'
}

maximizing = {
    'x': False,
    "o": True
}

points = {
    'x': -1,
    'o': 1
}

# returns false, or the player who won
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

def isTied(board):
    if len(getOpenSlots(board)) == 0:
        return True
    return False

def getOpenSlots(board):
    openSlots = []
    for i in range(3):
        for j in range(3):
            if not board[i][j]:
                openSlots.append((i,j))
    return openSlots

def minimax(board, player, depth):
    
    if isWon(board):
        winner = isWon(board)
        return points[winner]
    if isTied(board):
        return 0
    
    openSlots = getOpenSlots(board)
    isMaximizing = maximizing[player]
    highScore = None
    optimalMove = None

    if isMaximizing:
        highScore = -math.inf
    else:
        highScore = math.inf

    # loop through all the other slots and check them all
    for openSlot in openSlots:
        board[openSlot[0]][openSlot[1]] = player
        score = minimax(board, nextPlayer[player], depth + 1)
        board[openSlot[0]][openSlot[1]] = ''

        if (isMaximizing and score > highScore) or ((not isMaximizing) and score < highScore):
            highScore = score
            optimalMove = openSlot

    if depth == 0:
        return optimalMove
    else:
        return highScore


def main():
    
    board = [['','',''],['','',''],['','','']]

    player = 'o'
    while True:

        if player == 'o':
            optimalMove = minimax(board, "o", 0)
            board[optimalMove[0]][optimalMove[1]] = 'o'

        if player == 'x':
            invalidChoice = True
            while invalidChoice:
                choice = int(input("Enter your choice (1-9): "))
                choiceRow, choiceCol = math.floor((choice-1)/3), (choice-1)%3
                if board[choiceRow][choiceCol]:
                   print("Invalid Choice")
                else:
                   invalidChoice = False
            board[choiceRow][choiceCol] = player

        for i in board: print(i)

        if isWon(board):
            print("Winner is "+player+"!!")
            return
        if isTied(board):
            print('Tie game!')
            return

        player = nextPlayer[player]


if __name__ == "__main__":
    main()