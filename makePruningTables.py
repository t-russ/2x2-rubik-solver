import Cube
import pickle
from time import perf_counter

def pruneDFS(cubeState, maxDepth, depth, nextMove, pruningTable):

    if depth > maxDepth: return False
    depth += 1

    for m in nextMove:
        newState = Cube.applyMove(cubeState, m)
        stateHash = Cube.stateToHash(cubeState)

        if stateHash in pruningTable:
            if pruningTable.get(stateHash) > depth -1:
                pruningTable[stateHash] = depth -1
        else:
            pruningTable[stateHash] = depth -1

        if Cube.solved(newState):return True
        nextMoveSet = Cube.nextMoveMap[Cube.alias[m]]

        pruneDFS(newState, maxDepth, depth, nextMoveSet, pruningTable)

    return True


def prune(maxDepth):
    solvedState = ( 0, 0, 0, 0,
                    1, 1, 1, 1,
                    2, 2, 2, 2,
                    3, 3, 3, 3,
                    4, 4, 4, 4,
                    5, 5, 5, 5)
    
    initialMoves = ["F", "F2", "F'", "U", "U2", "U'", "R", "R2", "R'"]
    pruningTable = {}

    print('Starting pruning')

    a = perf_counter()

    pruneDFS(solvedState, maxDepth, 0, initialMoves, pruningTable)
    
    b = perf_counter()

    print(f'done in {b-a} seconds')

    return(pruningTable)


"""This section begins the pruning process, depending on depth this takes a very long time as the implementation
is not the most efficent.  will overwrite the mentioned table"""

"""pruningTable = prune(5)

with open('data/pruningTableDepth5.pickle', 'wb') as file:
    pickle.dump(pruningTable, file, protocol=pickle.HIGHEST_PROTOCOL)
"""