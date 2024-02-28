from Cube import *
from printCube import *
from time import perf_counter

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
        newState = applyMove(cubeState, m)
        moveStack.append(m)

        if solved(newState):return True

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
    totalTimeStart = perf_counter()

    while not condition:
        a = perf_counter()

        condition = dfs(cubeState, currentDepth, 0, moveStack, initialMoves)
        
        b = perf_counter()

        print(f"Depth {currentDepth}: Completed in {b-a} seconds ") 
        currentDepth += 1

    totalTimeEnd = perf_counter()

    solution = ' '.join(moveStack)

    print(f'Solution: {solution}')
    print(f'\nSolution found in {totalTimeEnd-totalTimeStart} seconds')

    return solution



