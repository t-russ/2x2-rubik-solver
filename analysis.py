from Cube import *
from idaStar import *
from iterativeDeepening import *
import numpy as np
import random
import copy

moveSet = ["F", "F2", "F'", "U", "U2", "U'", "R", "R2", "R'"]

solvedState = np.array([
          'R', 'R', 'R', 'R',
          'B', 'B', 'B', 'B',
          'O', 'O', 'O', 'O',
          'G', 'G', 'G', 'G',
          'W', 'W', 'W', 'W',
          'Y', 'Y', 'Y', 'Y'])

"""creates an array of 100 random moves, used to generate random cube states"""
def scrambler():
    scrambledMoves = []
    for i in range(100):
        scrambledMoves.append(random.choice(moveSet))

    return(scrambledMoves)


"""Calls scrambler 100 times and applies each move set, then saves to numpy array file"""
def applySaveScramble():
    dataSet = []
    for i in range(100):
        scrambleString = ' '.join(scrambler())
        tempState = applyMoveString(copy.deepcopy(solvedState), scrambleString)
        dataSet.append(tempState)

    with open('scrambleSet.npy', 'wb') as f:
        np.save(f, dataSet)

"""generate the scrambled cubes"""
#applySaveScramble()

dataSet = np.load('scrambleSet.npy')



for i in range(100):
    pass