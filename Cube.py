import numpy as np
import re
""" References: https://stackoverflow.com/questions/6098250/in-place-way-to-apply-a-permutation-to-a-list-inverse-of-sorting-by-key"""

#maps moves to indices within the moves array
moveMap = {'F':0, 'F2':1, "F'":2, 'U':3, 'U2':4, "U'":5, 'R':6, 'R2':7, "R'":8}

#permutations of the cube. F2, F' etc created by applying permutation 2 or 3 times to [1, 2, ... , 23]
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


"""Create a map that takes last move and returns list of acceptable next moves
   this removes basic redundant sequences of moves such as F2 F2, F F' etc."""

alias = {"F" : "id1", "F2" : "id1", "F'" : "id1",
            "U" : "id2", "U2" : "id2", "U'" : "id2",
            "R" : "id3", "R2" : "id3", "R'" : "id3"
            }

nextMoveMap = {"id1" : ["U", "U2", "U'", "R", "R2", "R'"],
         "id2" : ["F", "F2", "F'", "R", "R2", "R'"],
         "id3" : ["F", "F2", "F'", "U", "U2", "U'"]}



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


"""Normalise Cube is used to convert colour cube into numbered cube by face, this is needed
by ida* algorithm to work. This is due to there being no fixed colour for each face of the cube"""
def normaliseCube(cubeState):
    oppositeFaceMap = {'R':'O', 'O':'R', 'B':'G', 'G':'B', 'W':'Y', 'Y':'W'}

    downColour = cubeState[22]
    leftColour = cubeState[14]
    backColour = cubeState[11]
    frontColour = oppositeFaceMap.get(backColour)
    rightColour = oppositeFaceMap.get(leftColour)
    upColour = oppositeFaceMap.get(downColour)

    cubeState[cubeState == frontColour] = 0
    cubeState[cubeState == rightColour] = 1
    cubeState[cubeState == backColour] = 2
    cubeState[cubeState == leftColour] = 3
    cubeState[cubeState == upColour] = 4
    cubeState[cubeState == downColour] = 5

    cubeState = [eval(i) for i in cubeState]

    return cubeState


"""Converts cubeState into a hash, tuple used as cannot hash mutable objects"""
def stateToHash(cubeState):
    return hash(tuple(cubeState))




