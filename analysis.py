from Cube import *
from idaStar import *
from iterativeDeepening import *
import numpy as np
import copy
import matplotlib.pyplot as plt



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

    for i in range(3):
        r = []
        table = tableDict[i]

        for j in range(100):
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

def getDepth(moveString):
    return(len(stringToMoves(moveString)))


def getSetDepths():
    depthResults = []

    for i in range(100):
        s = dataSet[i]
        depth = getDepth(idaStar(s, pruningTableDepth10)[0])
        depthResults.append(depth)

    with open('data/depths.npy', 'wb') as f:
        np.save(f, depthResults)


"""generate the scrambled cubes"""
#applySaveScramble()

"""Importing tables and Definitions"""
with open('data/pruningTableDepth8.pickle', 'rb') as file:
    pruningTableDepth8 = pickle.load(file)

with open('data/pruningTableDepth9.pickle', 'rb') as file:
    pruningTableDepth9 = pickle.load(file)

with open('data/pruningTableDepth10.pickle', 'rb') as file:
    pruningTableDepth10 = pickle.load(file)

dataSet = np.load('data/scrambleSet.npy')
tableDict = {0: pruningTableDepth8, 1: pruningTableDepth9, 2: pruningTableDepth10}


"""Get results and save to file"""

results = getIdaResults(tableDict, dataSet)


with open('data/idaResults.npy', 'wb') as f:
    np.save(f, results)

#idResults = getIdResults(dataSet)

"""with open('data/iterativeResults.npy', 'wb') as f:
    np.save(f, idResults)"""

"""Load results, print some stats"""
idaResults = np.load('data/idaResults.npy')
depths = np.load('data/depths.npy')
idResults = np.load('data/iterativeResults.npy')

print('Dataset Depths')
print(f"Mean: {np.mean(depths)}")
print(f"median: {np.median(depths)}")
print(f"min: {np.min(depths)}")
print(f"max: {np.max(depths)}")


print('\nIterative Deepening')
print(f"Mean: {np.mean(idResults)}")
print(f"median: {np.median(idResults)}")
print(f"min: {np.min(idResults)}")
print(f"max: {np.max(idResults)}")

plt.style.use('seaborn-v0_8-darkgrid')

bins = np.arange(6, depths.max() + 1.5) - 0.5
plt.hist(depths, bins, rwidth=0.5, ec = 'black', alpha = 0.85, linewidth = 0.8)
plt.title('Distribution of Depths')
plt.xlabel('Number of Moves to Solve')
plt.ylabel('Frequency')
plt.show()

plt.hist(idResults, rwidth=0.8, ec = 'black', alpha = 0.85, linewidth = 0.8, bins = np.arange(0, 251, 10) )
plt.title('Distribution of Solve Time for Iterative Deepening')
plt.xlabel('Time to solve (seconds)')
plt.ylabel('Frequency')
plt.show()

