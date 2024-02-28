from idaStar import *
from Cube import *
from printCube import *

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
          'B', 'Y', 'Y', 'G', #front face
          'B', 'W', 'O', 'Y', #right face
          'G', 'Y', 'O', 'W', #back face
          'R', 'W', 'B', 'O', #left face
          'G', 'R', 'O', 'R', #up face
          'B', 'W', 'R', 'G']) #down face

printCube(cube, True)

idaStarSolution = idaStar(cube)
printMoveString(cube, idaStarSolution, True)

iterativeDeepeningSolution = iterativeDeepening(cube)

printMoveString(cube, idaStarSolution, True)

