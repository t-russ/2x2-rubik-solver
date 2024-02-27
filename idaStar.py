import Cube
from pruningTables import normaliseCube, stateToHash
from Solvers import *
import pickle

with open('pruningTable.pickle', 'rb') as file:
    pruningTable = pickle.load(file)


def idaStar(cubeState):
    cubeState = normaliseCube(cubeState)
    maxDistance = pruningTable.get(stateToHash(cubeState))
    moveStack = []
    initialMoves = ["F", "F2", "F'", "U", "U2", "U'", "R", "R2", "R'"]
    currentDepth = 1
    condition = False

    while not condition:
        a = perf_counter()
        condition = idaDFS(cubeState, maxDistance, currentDepth, 0, moveStack, initialMoves)
        b = perf_counter()

        print(f"Depth {currentDepth}: Completed in {b-a} seconds ") 

        currentDepth += 1


    print(' '.join(moveStack))


def idaDFS(cubeState, maxDistance, maxDepth, depth, moveStack, nextMove):

    if depth >= maxDepth: return False
    depth +=1

    for m in nextMove:
        dfs.counter += 1
        newState = Cube.applyMove(cubeState, m)

        if pruningTable.get(stateToHash(newState)) + depth > maxDistance:
            continue

        moveStack.append(m)

        if Cube.solved(newState):return True

        if idaDFS(newState, maxDistance, maxDepth, depth, moveStack, nextMoveMap[alias[m]]):
            return True
        
        moveStack.pop()
            
    return False


#F R move
twomovetest = np.array([
          'R', 'B', 'R', 'Y',
          'W', 'W', 'B', 'B',
          'G', 'O', 'W', 'O',
          'G', 'Y', 'G', 'Y',
          'W', 'R', 'G', 'R',
          'B', 'O', 'Y', 'O'])

#print(pruningTable.get(stateToHash(normaliseCube(twomovetest))))
idaDFS.counter = 0
idaStar(twomovetest)