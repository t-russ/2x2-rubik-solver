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

    with open('data/scrambleSet.npy', 'wb') as f:
        np.save(f, dataSet)


"""This iterates through different pruning tables getting results from 100 scrambled cubes"""
def getIdaResults(tableDict, dataSet):
    results = []

    for i in range(4):
        r = []
        table = tableDict[i]

        for j in range(2):
            s = dataSet[j]
            print(s)
            r.append(idaStar(s, table)[1])
        
        results.append(r)
    
    return results

def getIdResults(dataSet):
    results = []
    for i in range(100):
        s = dataSet[i]
        results.append(iterativeDeepening(s)[1])
    
    return results

"""generate the scrambled cubes"""
#applySaveScramble()

"""Importing tables and Definitions"""
with open('data/pruningTableDepth8.pickle', 'rb') as file:
    pruningTableDepth8 = pickle.load(file)

with open('data/pruningTableDepth9.pickle', 'rb') as file:
    pruningTableDepth9 = pickle.load(file)

with open('data/pruningTableDepth10.pickle', 'rb') as file:
    pruningTableDepth10 = pickle.load(file)

with open('data/pruningTableDepth11.pickle', 'rb') as file:
    pruningTableDepth11 = pickle.load(file)

dataSet = np.load('data/scrambleSet.npy')
tableDict = {0: pruningTableDepth8, 1: pruningTableDepth9, 2: pruningTableDepth10, 3: pruningTableDepth11}


"""Get results and save to file"""
#results = getIdaResults(tableDict, dataSet)


"""with open('data/idaResults.npy', 'wb') as f:
    np.save(f, results)"""

idResults = getIdResults(dataSet)

with open('data/iterativeResults.npy', 'wb') as f:
    np.save(f, idResults)

print('Done')

#idaResults = np.load('data/idaResults.npy')

