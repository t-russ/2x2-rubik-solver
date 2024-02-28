import Cube
import iterativeDeepening
import numpy as np
import pickle
from time import perf_counter

pruningTable = {}



def pruneDFS(cubeState, maxDepth, depth, nextMove):

    if depth > maxDepth: return False
    depth += 1

    for m in nextMove:
        newState = Cube.applyMove(cubeState, m)
        stateHash = stateToHash(cubeState)

        if stateHash in pruningTable:
            if pruningTable.get(stateHash) > depth -1:
                pruningTable[stateHash] = depth -1
        else:
            pruningTable[stateHash] = depth -1

        if Cube.solved(newState):return True
        nextMoveSet = Cube.nextMoveMap[Cube.alias[m]]

        pruneDFS(newState, maxDepth, depth, nextMoveSet)

    return True


def prune(maxDepth):
    solvedState = ( 0, 0, 0, 0,
                    1, 1, 1, 1,
                    2, 2, 2, 2,
                    3, 3, 3, 3,
                    4, 4, 4, 4,
                    5, 5, 5, 5)
    
    initialMoves = ["F", "F2", "F'", "U", "U2", "U'", "R", "R2", "R'"]

    pruneDFS(solvedState, maxDepth, 0, initialMoves)





"""This section begins the pruning process, this takes a very long time as the implementation
is not the most efficent. open file is commented off as running this will overwrite
the current pruning table"""

print('Starting pruning')

a = perf_counter()
#prune(11)
b = perf_counter()

print(f'done in {b-a} seconds')

print(len(pruningTable))

"""with open('pruningTable.pickle', 'wb') as file:
    pickle.dump(pruningTable, file, protocol=pickle.HIGHEST_PROTOCOL)"""

