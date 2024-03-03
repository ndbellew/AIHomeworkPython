# Queen Puzzle

# Author: Nathan Bellew

# Imports
from pprint import pprint
from time import time as run_time
from collections import deque
from SendToODS import ToODS

# Functions
def printSuccessors(node):
    for i in node:
        pprint(i)
    return "xD"

def bds(initNode, goalNode):
  bfsNode, bfsPath = bfs(initNode, goalNode)
  dfsNode, dfsPath = dfs(initNode, goalNode, complexityLevel)

  if dfsNode == bfsNode: #intersection
    if len(dfsPath) < len(bfsPath):
      return dfsNode, dfsPath
    return bfsNode, bfsPath
  else:
    return None, ["start"]
    raise NoPathFoundError("BDS no path found")

def ids(initNode, goalNode):
  depth = 0
  while True:
    result, path = dfs(initNode, goalNode, depth)
    if result is not None:
      return result, path
    else:
      depth += 1
      if depth % 5 == 0:
        print(f"Depth: {depth}\nResult: {result}\nComplexity Level: {complexityLevel}")
  raise NoPathFoundError("IDS could not find any path")

def dfs(initNode, goalNode, limit):
    discoveredNodes = deque([(initNode,["start"], 0)])  # treat this as a stack
    explored = list()  # Set to keep track of explored nodes
    while discoveredNodes:
        node, path, depth = discoveredNodes.pop()
        if node == goalNode:
            return node,path  # Return the goal node
        elif depth % 5 == 0:
          print(f"Depth: {depth}\nnode: {node}")
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
    # print(discoveredNodes)
    node, path = list(discoveredNodes.popleft())
    explor = tuple(map(tuple, node))
    # print(node)
    if node == goalNode:
      return node, path
    explored.append(explor)

    successors = computeSuccessors(node)
    for successor in successors:
      successorNode, move = successor
      upNext = tuple(map(tuple, successorNode))
      if upNext not in explored and all(tuple(map(tuple, s)) != upNext for s, _ in discoveredNodes):
          newPath = path + [move]
          discoveredNodes.append((successorNode, newPath))

  raise NoPathFoundError("No path found")


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


def computeSuccessors(node):
    successors = []
    successor = [list(r) for r in node]
    n = len(node)

    for row in range(n):
        for col in range(n):
            if node[row][col] == 1:  # Find a queen
                for nextRow in range(n):
                    for nextCol in range(n):

                        if successor[nextRow][nextCol] != 1:  # Ensure it's a new position
                              # Copy the board
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
            try:
                return bfs(initNode, goalNode)
            except NoPathFoundError as noPath:
                print("BFS No Path Found")
        case "dfs":
            try:
                return dfs(initNode, goalNode, complexityLevel )
            except(NoPathFoundError) as noPath:
                print("DFS No Path Found")
        case "ids":
            try:
                return ids(initNode, goalNode)
            except(NoPathFoundError) as noPath:
                print("IDS No Path Found")
        case "bds":
            try:
                return bds(initNode, goalNode)
            except(NoPathFoundError) as noPath:
                print("BDS No Path Found")
        case _:
            return None
    return None


def nPuzzle(n, initState):
    goalNode = [[0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 1, 0, 0]]
    endTimes = dict()
    endTimes["problem"] = initState
    # Breadth-First Search
    timeToStart = run_time()
    finalNode, path = graphSearch(initState, goalNode, "bfs")
    timeToFinish = run_time()
    print(finalNode)
    if finalNode == goalNode:
        endTimes["bfs"] = timeToFinish - timeToStart
        endTimes["path"] = path
    else:
        endTimes["bfs"] = 111111.11111
    # Depth First Search asdf
    timeToStart = run_time()
    finalNode, path = graphSearch(initState, goalNode, "dfs")
    timeToFinish = run_time()
    if finalNode == goalNode:
      endTimes["dfs"] = f"{timeToFinish - timeToStart}"
      if len(path) < len(endTimes["path"]):
          endTimes["path"] = path
    #  print(f"DFS Time: {endTimes["dfs"]}")
    else:
      endTimes["dfs"] = 11111.11111
         # Iterative Deepening Search
    timeToStart = run_time()
    finalNode, path = graphSearch(initState, goalNode, "ids")
    timeToFinish = run_time()
    if finalNode == goalNode:
      endTimes["ids"] = f"{timeToFinish - timeToStart}"
      if len(path) < len(endTimes["path"]):
          endTimes["path"] = path
     # print(f"IDS Time: {endTimes["ids"]}")
    else:
      endTimes["ids"] = 11111.11111
         # Bidirectional Search
    timeToStart = run_time()
    finalNode, path = graphSearch(initState, goalNode, "bds")
    timeToFinish = run_time()
    if finalNode == goalNode:
      endTimes["bds"] = f"{timeToFinish - timeToStart}"
      if len(path) < len(endTimes["path"]):
          endTimes["path"] = path
     # print(f"BDS Time: {endTimes["bds"]}")
    else:
      endTimes["bds"] = 11111.11111
    return endTimes
# Invoke
# def run(initState):
#   # print(initState)
#   return nPuzzle(3, initState)

# Main
def main():
    n = 4
    initState = [[1,1,1,1],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    timelist = list()
    global complexityLevel, maxComplexity
    complexityLevel = 6
    maxComplexity = 20
    # for i in range(0, maxComplexity, 1):
    #     print(i)
    #     complexityLevel += 1
    timelist.append(nPuzzle(n, initState))
    #     # Modify current state, making it more complex.
    return timelist

# Test/Debug
from test import test_successors as ts
def test():
    startState, expectedSuccessors = ts.start_state, ts.expected_successors
    successors = computeSuccessors(startState)

    try:
        assert successors == expectedSuccessors, "Test failed: Unexpected successors."
    except AssertionError:
        temp = list()
        print(successors)
        print(expectedSuccessors)
        for n in successors:
            if n not in temp:
                temp.append(n)
        for i in temp:
            print("found a failure")
            printSuccessors(i)
            print("\n")

# Errors
class NoPathFoundError(Exception):
  pass

# Modularity
if __name__ == "__main__":
    timelist = main()
    print(timelist)
    ToODS(timelist, name="queensoutput.ods")
    #test()