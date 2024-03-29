"""
References: 
layout inspired by https://github.com/MeepMoop/py222/tree/master
solver inspired by: https://github.com/lukapopijac/pocket-cube-optimal-solver
"""
from idaStar import *
from Cube import *
from printCube import *
from makePruningTables import prune

#importing of pruning tables
with open('data/pruningTableDepth7.pickle', 'rb') as file:
    pruningTableDepth7 = pickle.load(file)

with open('data/pruningTableDepth8.pickle', 'rb') as file:
    pruningTableDepth8 = pickle.load(file)

with open('data/pruningTableDepth9.pickle', 'rb') as file:
    pruningTableDepth9 = pickle.load(file)

#Some more tables available
"""with open('data/pruningTableDepth10.pickle', 'rb') as file:
    pruningTableDepth10 = pickle.load(file)

with open('data/pruningTableDepth11.pickle', 'rb') as file:
    pruningTableDepth11 = pickle.load(file)"""


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

Each cubie face has a different indice
A 24 length array is used to store the state of the cube.

DLB (down left back) corner is fixed so only moves F, F2, F', U, U2, U', R, R2, R' are needed

Move Notation:
Letter - denotes cube face. F = Front, R = Right, U = Up.

F - 90 degree clockwise turn of the front face.
F2 - 180 degree turn of front face.
F' - 90 degreee anti-clockwise turn of front face.

Same applies of U, R.

Choose a DLB (Down Left Back) corner, orient cube using net shown above, with Front Face being indices 0-3.
Enter into 'cube' array below and then call solving functions
"""

"""---------- Cube Input -----------"""

"""!!!INPUT YOUR CUBE HERE!!!"""
cube = np.array([
        #front face
        'G', 'Y',
        'B', 'B',
        #right face
        'R', 'B',
        'W', 'G',
        #back face
        'Y', 'W',
        'O', 'R',
        #left face
        'R', 'Y',
        'G', 'R', 
        #up face  
        'B', 'O',
        'O', 'G', 
        #down face
        'Y', 'O',
        'W', 'W' ]) 



""""!!! OR GENERATE A RANDOM CUBE !!!"""
#cube = randomCube()

"""Sample solved cube array"""
solvedCube = np.array([
          'R', 'R', 'R', 'R',
          'B', 'B', 'B', 'B',
          'O', 'O', 'O', 'O',
          'G', 'G', 'G', 'G',
          'W', 'W', 'W', 'W',
          'Y', 'Y', 'Y', 'Y'])


"""generate a pruning table of chosen depth, depths 7-11 are supplied.
    Table definitions at top of file."""
#pruningTable = prune(5)


"""Prints cube supplied in first parameter, second parameter dictates colour printing
!!!Set second parameter, colouring, to False if not printing in terminal!!!"""
printCube(cube, True)


"""-------------------- Solvers --------------------"""

"""Iterative Deepening Solution, use second return to get solve time"""
#iterativeDeepeningSolution = iterativeDeepening(cube)[0]


"""ida* solution, pruning table must be chosen for this, use second return to get solve time
    Note that if your solution is taking a very long time with this solver, it will be due to 
    a misinput cube"""
#idaStarSolution = idaStar(cube, pruningTableDepth9)[0]


"""ida* solution, using the optimisation as laid out in the report."""
idaOptimisedSolution = idaStarOptimised(cube, pruningTableDepth8)[0]


"""Prints solution applied to cube state move by move"""
#printMoveString(cube, idaOptimisedSolution, True)
