# Queen Puzzle

# Author: Nathan Bellew

# Imports





from time import time as run_time
from collections import deque
from GenerateTestStates import genQueens
from SendToODS import ToODS
from pprint import pprint
# Functions

def isGoalNode(node):
    n = len(node)
    # Orthogonals
    for row in range(n):
        if sum(node[row]) != 1:
            return False
    for col in range(n):
        if sum(node[row][col] for row in range(n)) != 1:
            return False
    # Diagonals
    for d in range(-n + 1, n):
        if sum(node[i][i + d] for i in range(max(0, -d), min(n, n - d)) if 0 <= i + d < n) > 1:
            return False
        if sum(node[i][n - 1 - i + d] for i in range(max(0, d), min(n, n + d)) if 0 <= n - 1 - i + d < n) > 1:
            return False
    return True

def bds(initNode, goalNode):
  bfsNode, bfsPath = bfs(initNode, goalNode)
  dfsNode, dfsPath = dfs(initNode, goalNode, complexityLevel)
  if dfsNode and bfsNode: #intersection or two solutions found for each piece.
    if len(dfsPath) < len(bfsPath):
      return dfsNode, dfsPath
    return bfsNode, bfsPath
  else:
    return None, ["start"]

def ids(initNode, goalNode):
  depth = 0
  while True:
    result, path = dfs(initNode, goalNode, depth)
    if result is not None:
      return result, path
    else:
      depth += 1

def dfs(initNode, goalNode, limit):
    discoveredNodes = deque([(initNode,["start"], 0)])  # treat this as a stack
    explored = list()  # Set to keep track of explored nodes
    while discoveredNodes:
        node, path, depth = discoveredNodes.pop()
        if goalNode(node):
            return node,path  # Return the goal node
        if depth < limit:
            if node not in explored:
              explored.append(node)
            successors = computeSuccessors(node)
            for successor in successors:
              successorNode, move = successor
              upNext = tuple(map(tuple, successorNode))
              if upNext not in explored and all(tuple(map(tuple, s)) != upNext for s,_,_ in discoveredNodes):
                newPath = path + [move]
                discoveredNodes.append((successorNode, newPath, depth + 1))  # Append the successor and its depth to the stack
    return None, ["start"]

def bfs(initNode, goalNode):
  discoveredNodes = deque([(initNode, ["start"])])
  explored        = list()
  while discoveredNodes:
    node, path = list(discoveredNodes.popleft())
    explor = tuple(map(tuple, node))
    if goalNode(node):
      return node, path
    explored.append(explor)
    successors = computeSuccessors(node)
    for successor in successors:
      successorNode, move = successor
      upNext = tuple(map(tuple, successorNode))
      if upNext not in explored and all(tuple(map(tuple, s)) != upNext for s, _ in discoveredNodes):
          newPath = path + [move]
          discoveredNodes.append((successorNode, newPath))
  return None, ['start']


def moveToString(from_row, from_col, to_row, to_col, n):
    def colLabel(col):
        result = ""
        while col >= 0:
            result = chr((col % 26) + 65) + result
            col = col // 26 - 1
        return result
    def rowLabel(row):
        return str(row + 1)
    return f"{colLabel(from_col)}{rowLabel(from_row)} to {colLabel(to_col)}{rowLabel(to_row)}"

def isValidMove(fromRow, fromCol, toRow, toCol, node): # Check if move is legal in chess
    def isOrthogonal():
        if fromRow == toRow or fromCol == toCol:
            return True
    def isDiagonal():
        if abs(fromRow - toRow) == abs(fromCol - toCol):
            return True
    def getPoints():# returns whether the queen passes through another queen to get to point (which would fail)
        points = list()
        rowDirection = 1 if toRow > fromRow else -1 if toRow < fromRow else 0
        colDirection = 1 if toCol > fromCol else -1 if toCol < fromCol else 0
        steps = max(abs(toRow - fromRow), abs(toCol - fromCol))
        for step in range(1, steps):
            intermediateRow = fromRow + step * rowDirection
            intermediateCol = fromCol + step * colDirection
            points.append((intermediateRow, intermediateCol))
        return points
    if isOrthogonal() or isDiagonal():
        pts = getPoints()
        for x,y in pts:
            if node[x][y] == 1:
                return False
        return True


def computeSuccessors(node):
    successors = []
    successor = [list(r) for r in node]
    n = len(node)
    for row in range(n):
        for col in range(n):
            if node[row][col] == 1:  # Find a queen
                for nextRow in range(n):
                    for nextCol in range(n):
                        if successor[nextRow][nextCol] != 1 and isValidMove(row, col, nextRow, nextCol, node):  # Ensure it's a new position
                            successor[row][col] = 0  # Remove queen from current position
                            successor[nextRow][nextCol] = 1  # Place queen in new position
                            move = moveToString(row, col, nextRow, nextCol, n)  # Generate move string
                            if not any(successor == s for s, _ in successors):  # Check for unique state
                                successors.append((successor, move))
                            successor = [list(r) for r in node]
    return successors

def graphSearch(initNode, goalNode, typeSearch):
    match typeSearch:
        case "bfs":
            return bfs(initNode, goalNode)
        case "dfs":
             return dfs(initNode, goalNode, complexityLevel )
        case "ids":
            return ids(initNode, goalNode)
        case "bds":
            return bds(initNode, goalNode)
        case _:
            return None
    return None

def nPuzzle(n, initState):
    algorithms = ["bfs", "dfs", "ids", "bds"]
    endTimes = dict()
    endTimes["problem"] = initState
    for algorithm in algorithms:
        timeToStart = run_time()
        finalNode, path = graphSearch(initState, isGoalNode, algorithm)
        timeToFinish = run_time()
        if finalNode:
            endTimes[algorithm] = timeToFinish - timeToStart
            endTimes["path"] = path
        else:
            endTimes[algorithm] = 111111.11111
    return endTimes

# Main
def main():
    n = 4
    initStates = genQueens()
    timelist = list()
    global complexityLevel
    complexityLevel = 23 # Guess of total valid Goal states
    for initState in initStates:
        timelist.append(nPuzzle(n, initState))
    return timelist

# Modularity
if __name__ == "__main__":
    timelist = main()
    # For Ali
    # Options for seeing answers
    # To print to command line
    pprint(timelist)
    # To create .ods file (similar to excel)
    ToODS(timelist, "QueenPuzzle.ods")