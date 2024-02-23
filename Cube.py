import numpy as np
import re
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
#maps moves to indices within the moves array
moveMap = {'F':0, 'F2':1, "F'":2, 'U':3, 'U2':4, "U'":5, 'R':6, 'R2':7, "R'":8}

#permutations of the cube F2, F' etc created by applying permutation 2 or 3 times to [1, 2, ... , 23]
moves = np.array([
    [2, 0, 3, 1, 18, 5, 19, 7, 8, 9, 10, 11, 12, 20, 14, 21, 16, 17, 15, 13, 6, 4, 22, 23],
    [3, 2, 1, 0, 15, 5, 13, 7, 8, 9, 10, 11, 12, 6, 14, 4, 16, 17, 21, 20, 19, 18, 22, 23],
    [1, 3, 0, 2, 21, 5, 20, 7, 8, 9, 10, 11, 12, 19, 14, 18, 16, 17, 4, 6, 13, 15, 22, 23],
    [4, 5, 2, 3, 8, 9, 6, 7, 12, 13, 10, 11, 0, 1, 14, 15, 18, 16, 19, 17, 20, 21, 22, 23],
    [8, 9, 2, 3, 12, 13, 6, 7, 0, 1, 10, 11, 4, 5, 14, 15, 19, 18, 17, 16, 20, 21, 22, 23],
    [12, 13, 2, 3, 0, 1, 6, 7, 4, 5, 10, 11, 8, 9, 14, 15, 17, 19, 16, 18, 20, 21, 22, 23],
    [0, 21, 2, 23, 6, 4, 7, 5, 19, 9, 17, 11, 12, 13, 14, 15, 16, 1, 18, 3, 20, 10, 22, 8],
    [0, 10, 2, 8, 7, 6, 5, 4, 3, 9, 1, 11, 12, 13, 14, 15, 16, 21, 18, 23, 20, 17, 22, 19],
    [0, 17, 2, 19, 5, 7, 4, 6, 23, 9, 21, 11, 12, 13, 14, 15, 16, 10, 18, 8, 20, 1, 22, 3]])

#define regular expression pattern to find moves from a given string
cubeStringRegex = re.compile(r"[FURfur][2']?")


#Maps characters to their Ansi escape sequence, allows for colour printing in terminal
colourMap = {'R' : '\033[31mR\033[0m',
             'O' : '\033[38;5;208mO\033[0m',
             'B' : '\033[38;5;12mB\033[0m',
             'G' : '\033[38;5;10mG\033[0m',
             'W' : '\033[38;5;15mW\033[0m',
             'Y' : '\033[38;5;11mY\033[0m'}


"""Converts a string of moves to a list of moves.
   Seperation done by applying regular expression.
   example: "F F2 F'" -> ["F", "F2", "F'"]  """
def stringToMoves(moveString):
    moveList = cubeStringRegex.findall(moveString)
    return moveList


"""Applys permutation to cubes current state"""
def applyMove(cubeState, m):
     indice = moveMap.get(m)
     cubeState = [cubeState[i] for i in moves[indice]]
     return cubeState


"""Applys a string such as "F F' U2" to the cube.
   Useful for scrambling and testing """
def applyMoveString(cubeState, moveString):
     moveList = stringToMoves(moveString)
     for i in moveList:
          cubeState = applyMove(cubeState, i)
     return cubeState


"""Checks whether the cube is in a solved state.
   Iterates over all faces and compares values"""
def solved(cubeState):
     for i in range(6):
          if any([cubeState[i*4] != cubeState[i*4 + j] for j in range(4)]):
               return False
     return True


"""prints cube, has option for printing in colour.
   colouring = True uses colour printing.

   !!!must be printing in terminal to work!!!

   Do not use if printing to output tab in vscode/codium"""
def printCube(cubeState, colouring):
     if colouring:
          withC = np.vectorize(colourMap.get)(cubeState)
     else:
          withC = cubeState
     cubePrint = '''
        ----
       |{16}  {17}|
       |{18}  {19}|
 ----   ----   ----   ---- 
|{12}  {13}| |{0}  {1}| |{4}  {5}| |{8}  {9}|
|{14}  {15}| |{2}  {3}| |{6}  {7}| |{10}  {11}|
 ----   ----   ----   ----
       |{20}  {21}|
       |{22}  {23}|
        ----
            '''
     print(cubePrint.format(*withC))




testcubeSolved = np.array([
          'R', 'R', 'R', 'R',
          'B', 'B', 'B', 'B',
          'O', 'O', 'O', 'O',
          'G', 'G', 'G', 'G',
          'W', 'W', 'W', 'W',
          'Y', 'Y', 'Y', 'Y'])

testcube = np.array([
          'B', 'O', 'R', 'Y',
          'W', 'W', 'O', 'G',
          'O', 'Y', 'W', 'Y',
          'B', 'O', 'G', 'B',
          'R', 'G', 'Y', 'B',
          'W', 'G', 'R', 'R'])

testcube2 = np.array([
          'B', 'G', 'W', 'O',
          'R', 'G', 'G', 'Y',
          'W', 'G', 'R', 'W',
          'Y', 'O', 'B', 'B',
          'R', 'O', 'Y', 'W',
          'O', 'Y', 'R', 'B'])

SolveStringOptimal = "U F2 U F U2 R U' R F2"

solvestring = "F U F U F U2 F U2 R U2 R F2 R2"

printCube(testcube, True)
print(solved(testcube))

solvedstate = applyMoveString(testcube, solvestring)

printCube(solvedstate, True)
print(solved(solvedstate))