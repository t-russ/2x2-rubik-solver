import Cube
from printCube import *

from time import perf_counter

"""Create a map that takes last move and returns list of acceptable next moves
   this removes basic redundant sequences of moves such as F2 F2, F F' etc."""

alias = {"F" : "id1", "F2" : "id1", "F'" : "id1",
            "U" : "id2", "U2" : "id2", "U'" : "id2",
            "R" : "id3", "R2" : "id3", "R'" : "id3"
            }

nextMoveMap = {"id1" : ["U", "U2", "U'", "R", "R2", "R'"],
         "id2" : ["F", "F2", "F'", "R", "R2", "R'"],
         "id3" : ["F", "F2", "F'", "U", "U2", "U'"]}

"""Exectues a depth first search with a give state and maximum depth of traversal
   doesn't actually contain the depth first search algorithm
def depthFirstSearch(cubeState, maxDepth):
    moveStack = []
    initialMoves = ["F", "F2", "F'", "U", "U2", "U'", "R", "R2", "R'"]
    dfs(cubeState, maxDepth, 0, moveStack, initialMoves)
    print(' '.join(moveStack))"""


"""The bread and butter of the depth first search. completed using recursive function
   used by iterative deepening function"""
def dfs(cubeState, maxDepth, depth, moveStack, nextMove):
    if depth >= maxDepth: return False
    depth +=1

    for m in nextMove:
        newState = Cube.applyMove(cubeState, m)
        moveStack.append(m)

        if Cube.solved(newState):return True

        if dfs(newState, maxDepth, depth, moveStack, nextMoveMap[alias[m]]):
            return True
        
        moveStack.pop()
            
    return False

"""Iterative deepening algorithm, works by calling the dfs recursive function with
    increasing depth each iteration"""
def iterativeDeepening(cubeState):
    moveStack = []
    initialMoves = ["F", "F2", "F'", "U", "U2", "U'", "R", "R2", "R'"]
    currentDepth = 1
    condition = False

    while not condition:
        a = perf_counter()

        condition = dfs(cubeState, currentDepth, 0, moveStack, initialMoves)
        
        b = perf_counter()

        print(f"Depth {currentDepth}: Completed in {b-a} seconds ") 
        currentDepth += 1

    print(' '.join(moveStack))

#iterativeDeepening(Cube.testcube)