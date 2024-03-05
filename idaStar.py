from Cube import *
from iterativeDeepening import *
import pickle
import copy

"""Opens the pruning table from file"""
"""with open('pruningTable.pickle', 'rb') as file:
    pruningTable = pickle.load(file)"""


"""The parent function that executes the ida* search with varying depth
very similar to the iterative deepening implementation"""
def idaStar(cubeState, pruningTable):

    #definitions
    cubeStateNormalised = normaliseCube(copy.deepcopy(cubeState))
    intialHeuristic = pruningTable.get(stateToHash(cubeStateNormalised))

    if intialHeuristic is not None: maxDistance = intialHeuristic
    else: maxDistance = 11
    
    moveStack = []
    initialMoves = ["F", "F2", "F'", "U", "U2", "U'", "R", "R2", "R'"]
    currentDepth = 1
    condition = False
    totalTimeStart = perf_counter()

    #graph search
    while not condition:
        a = perf_counter()
        condition = idaDFS(cubeStateNormalised, maxDistance, currentDepth, 0, moveStack, initialMoves, pruningTable)
        b = perf_counter()

        print(f"Depth {currentDepth}: Completed in {b-a} seconds ") 

        currentDepth += 1

    totalTimeEnd = perf_counter()

    solution = ' '.join(moveStack)
    print(f'\nSolution:  {solution}')
    print(f'\nSolution found in {totalTimeEnd-totalTimeStart} seconds')

    return solution


"""The depth first search part of the ida* search. 
heuristic map prunes using 'continue' to skip branches"""
def idaDFS(cubeState, maxDistance, maxDepth, depth, moveStack, nextMove, pruningTable):

    if depth >= maxDepth: return False
    depth +=1

    for m in nextMove:
        newState = applyMove(cubeState, m)

        heuristic = pruningTable.get(stateToHash(newState))

        if heuristic is not None:
            if heuristic + depth > maxDistance:
                continue

        moveStack.append(m)

        if solved(newState):return True

        if idaDFS(newState, maxDistance, maxDepth, depth, moveStack, nextMoveMap[alias[m]], pruningTable):
            return True
        
        moveStack.pop()
            
    return False
