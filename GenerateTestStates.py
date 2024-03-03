from random import shuffle, choice


def genRandInit(complexityLevel=0, currentState=list()):
    goal_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]  # Goal state

    # Apply a series of random legal moves to the goal state to create the initial state
    if not currentState:
        currentState = [row[:] for row in goal_state]  # Deep copy of the goal state
    MovedState = [row[:] for row in currentState]
    for _ in range(complexityLevel):
        while MovedState == currentState or MovedState == goal_state:
            blankRow, blankColumn = findBlankPosition(currentState)
            possible_moves = []
            if blankRow > 0:
                possible_moves.append('up')
            if blankRow < 2:
                possible_moves.append('down')
            if blankColumn > 0:
                possible_moves.append('left')
            if blankColumn < 2:
                possible_moves.append('right')

            random_move = choice(possible_moves)
            MovedState = Move(currentState, random_move)
            # print(MovedState)
            # print(f"Moved State\nCurrentState: {currentState}\n")
        currentState = MovedState

    return currentState

def findBlankPosition(node):
    for i in range(len(node)):
        for j in range(len(node[i])):
            if node[i][j] == 0:
                return i, j


def Move(node, move):
    blankRow, blankColumn = findBlankPosition(node)
    newRow, newColumn = blankRow, blankColumn

    match move:
        case 'up':
            newRow -= 1
        case 'down':
            newRow += 1
        case 'left':
            newColumn -= 1
        case 'right':
            newColumn += 1

    if 0 <= newRow < len(node) and 0 <= newColumn < len(node[0]):
        newState = [row[:] for row in node]  # Create a deep copy of the current state
        newState[blankRow][blankColumn] = node[newRow][newColumn]
        newState[newRow][newColumn] = 0
        return newState

    raise(Exception("Invalid Move"))