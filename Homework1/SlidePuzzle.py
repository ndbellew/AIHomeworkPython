# AI Homework 1

# Author: Nathan Bellew

# Imports

from time import time as run_time
from collections import deque
from GenerateTestStates import genRandInit
from pprint import pprint
from SendToODS import ToODS

# Functions
def findBlank(node):
  for i in range(len(node)):
    for j in range(len(node[i])):
      if node[i][j] == 0:
        return i,j

def bds(initNode, goalNode):
  bfsNode, bfsPath = bfs(initNode, goalNode)
  dfsNode, dfsPath = dfs(initNode, goalNode, complexityLevel)
  intersection = set(map(tuple, bfsNode)) & set(map(tuple, dfsNode))
  if intersection:
    if len(dfsPath) < len(bfsPath):
      return dfsNode, dfsPath
    return bfsNode, bfsPath
  else:
    return None, ["start"]

def ids(initNode, goalNode):
  depth = 1
  while True:
    result, path = dfs(initNode, goalNode, depth)
    if result is not None:
      return result, path
    else:
      if depth <= complexityLevel:
        depth += 1
      else:
        return None

def dfs(initNode, goalNode, limit):
    discoveredNodes = deque([(initNode,["start"], 0)])  # treat this as a stack
    explored = list()  # Set to keep track of explored nodes
    while discoveredNodes:
        node, path, depth = discoveredNodes.pop()
        if node == goalNode:
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
  explored = set()
  while discoveredNodes:
    node, path = discoveredNodes.popleft()
    explor = tuple(map(tuple, node))
    if node == goalNode:
      return node, path
    explored.add(explor)
    successors = computeSuccessors(node)
    for successor in successors:
      successorNode, move = successor
      upNext = tuple(map(tuple, successorNode))
      if upNext not in explored and all(tuple(map(tuple, s)) != upNext for s, _ in discoveredNodes):
        newPath = path + [move]
        discoveredNodes.append((successorNode, newPath))
  return None, ["start"]

def computeSuccessors(node):
  n = 3
  successors = []
  blankRow, blankColumn = findBlank(node)
  moves = ['up', 'down', 'left', 'right']
  for move in moves:
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
    if 0 <= newRow < n and 0 <= newColumn < n:
      newState = [row[:] for row in node]  # Create a deep copy of the current state
      newState[blankRow][blankColumn] = node[newRow][newColumn]
      newState[newRow][newColumn] = 0
      successors.append((newState, move))
      # 1 is the cost associated with the move
  if not successors:
    return None
  else:
    return successors

def graphSearch(initNode, goalNode, typeSearch): # for now this is BFS
  # BFS, DFS, Iterative Deepening Search, Bidrectional Search
  match typeSearch:
    case "bfs":
      return bfs(initNode, goalNode)
    case "dfs":
      return dfs(initNode, goalNode, complexityLevel+1)
    case "ids":
      return ids(initNode, goalNode)
    case "bds":
      return bfs(initNode, goalNode)
    case _:
      return None
  return None

def nPuzzle(n, initState):
  goalNode = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
  algorithms = ["bfs", "dfs", "ids", "bds"]
  endTimes = dict()
  endTimes["problem"] = initState
  for a in algorithms:
    timeToStart = run_time()
    finalNode, path = graphSearch(initState, goalNode, a)
    timeToFinish = run_time()
    if finalNode == goalNode:
      endTimes[a] = f"{timeToFinish - timeToStart}"
      if "path" not in endTimes:
        endTimes["path"] = path
      elif endTimes["path"] > path:
        endTimes["path"] = path
    else:
      endTimes[a] = 1111111.111
  return endTimes

# Invoke
def run(initState):
  return nPuzzle(3, initState)

# Main
def main():
  timelist = list()
  global complexityLevel, maxComplexity
  maxComplexity = 20
  currentState = genRandInit(complexityLevel=0)
  for i in range(1,maxComplexity,4):
    complexityLevel = i
    currentState = genRandInit(complexityLevel=complexityLevel, currentState=currentState)
    timelist.append(run(currentState))
  return timelist

# Modularity
if __name__ == "__main__":
  timelist = main()
  # For Ali
  # Options for seeing answers
  # To print to command line
  pprint(timelist)
  # To create .ods file (similar to excel)
  ToODS(timelist, "SlidePuzzle.ods")





