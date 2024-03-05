from idaStar import *
from Cube import *
from printCube import *
from makePruningTables import prune

"""
Cube modelled in form:
       _____
      |16 17|
      |18 19|
 _____ _____ _____ _____ 
|12 13|00 01|04 05|08 09|
|14 15|02 03|06 07|10 11|
 ‾‾‾‾‾ ‾‾‾‾‾ ‾‾‾‾‾ ‾‾‾‾‾  
      |20 21|
      |22 23|
       ‾‾‾‾‾

Each facelet has a different indice
A 24 length array is used to store the state of the cube.

Moves are modelled as permutations. 
each value in the array displays where each index in the current state of the cube is moved.

DLB (down left back corner) is fixed, this means that the only moves needed to solve are F U R.
This is done since this allows for every cube to be moved without moving our fixed corner.
"""

solvedCube = np.array([
          'R', 'R', 'R', 'R',
          'B', 'B', 'B', 'B',
          'O', 'O', 'O', 'O',
          'G', 'G', 'G', 'G',
          'W', 'W', 'W', 'W',
          'Y', 'Y', 'Y', 'Y'])

cube = np.array([
          'G', 'Y', 'B', 'B', #front face
          'R', 'B', 'W', 'G', #right face
          'Y', 'W', 'O', 'R', #back face
          'R', 'Y', 'G', 'R', #left face
          'B', 'O', 'O', 'G', #up face
          'Y', 'O', 'W', 'W']) #down face

printCube(cube, True)

with open('pruningTable.pickle', 'rb') as file:
    pruningTable = pickle.load(file)

idaStarSolution = idaStar(cube, pruningTable)
print('\nPruning Table Depth 6')
pruningTableDepth6 = prune(6)
idaStarSolution6 = idaStar(cube, pruningTableDepth6)
print('\nPruning Table Depth 7')
pruningTableDepth7 = prune(7)
idaStarSolution7 = idaStar(cube, pruningTableDepth7)
print('\nPruning Table Depth 8')
pruningTableDepth8 = prune(8)
idaStarSolution8 = idaStar(cube, pruningTableDepth8)
print('\nNormal solution')
iterativeDeepening(cube)


#printMoveString(cube, idaStarSolution, True)

#iterativeDeepeningSolution = iterativeDeepening(cube)

#printMoveString(cube, idaStarSolution, True)

