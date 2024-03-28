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

def getOptimResults(tableDict, dataSet):
    results = []

    for i in range(4):
        r = []
        table = tableDict[i]

        for j in range(100):
            s = dataSet[j]
            print(s)
            r.append(idaStarOptimised(s, table)[1])
        
        results.append(r)
    
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
with open('data/pruningTableDepth5.pickle', 'rb') as file:
    pruningTableDepth5 = pickle.load(file)

with open('data/pruningTableDepth6.pickle', 'rb') as file:
    pruningTableDepth6 = pickle.load(file)

with open('data/pruningTableDepth7.pickle', 'rb') as file:
    pruningTableDepth7 = pickle.load(file)

with open('data/pruningTableDepth8.pickle', 'rb') as file:
    pruningTableDepth8 = pickle.load(file)

with open('data/pruningTableDepth9.pickle', 'rb') as file:
    pruningTableDepth9 = pickle.load(file)

with open('data/pruningTableDepth10.pickle', 'rb') as file:
    pruningTableDepth10 = pickle.load(file)

dataSet = np.load('data/scrambleSet.npy')
idaDict = {0: pruningTableDepth8, 1: pruningTableDepth9, 2: pruningTableDepth10}

optimDict = {0: pruningTableDepth5, 1: pruningTableDepth6, 2: pruningTableDepth7, 3:pruningTableDepth8}
"""Get results and save to file"""

#results = getIdaResults(idaDict, dataSet)

"""
with open('data/idaResults.npy', 'wb') as f:
    np.save(f, results)"""

#idResults = getIdResults(dataSet)

"""with open('data/iterativeResults.npy', 'wb') as f:
    np.save(f, idResults)"""

"""optimResults = getOptimResults(optimDict, dataSet)

with open('data/optimResults.npy', 'wb') as f:
    np.save(f, optimResults)"""

    
"""-------Load results, print some stats-------"""
idaResults = np.load('data/idaResults.npy')
depths = np.load('data/depths.npy')
idResults = np.load('data/iterativeResults.npy')
optimResults = np.load('data/optimResults.npy')


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

for i in range(4):
    s = idaResults[i]
    print(f"\n IDA* Depth {i + 8}")
    print(f"Mean: {np.mean(s)}")
    print(f"median: {np.median(s)}")
    print(f"min: {np.min(s)}")
    print(f"max: {np.max(s)}")

for i in range(4):
    s = optimResults[i]
    print(f"\n IDA* Optimised Depth {i + 5}")
    print(f"Mean: {np.mean(s)}")
    print(f"median: {np.median(s)}")
    print(f"min: {np.min(s)}")
    print(f"max: {np.max(s)}")

"""------- Plotting -------"""
plt.style.use('seaborn-v0_8-darkgrid')

"""
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
"""

depth8 = np.concatenate((np.array([63.67]), idaResults[0])) 
depth9 = np.concatenate((np.array([388.15]), idaResults[1]))
depth10 = np.concatenate((np.array([2289.3]), idaResults[2]))
idset = np.concatenate((np.array([0.0]), idResults))

depth5 = np.concatenate((np.array([0.30220]), optimResults[0]))
depth6 = np.concatenate((np.array([1.833]), optimResults[1])) 
depth7 = np.concatenate((np.array([11.045]), optimResults[2]))
depth8optim = np.concatenate((np.array([63.67]), optimResults[3]))
idset = np.concatenate((np.array([0.0]), idResults))

d5cumsum = np.cumsum(depth5)
d6cumsum = np.cumsum(depth6)
d7cumsum = np.cumsum(depth7)
d8OPcumsum = np.cumsum(depth8optim)
d8cumsum = np.cumsum(depth8)
d9cumsum = np.cumsum(depth9)
d10cumsum = np.cumsum(depth10)
idcumsum = np.cumsum(idset)

x = range(0, 101)
#lt.plot(x, idcumsum, label = 'Iterative Deepening')

plt.plot(x, d8cumsum, label = 'IDA* Depth 8', linestyle = "--")
#plt.plot(x, d9cumsum, label = 'IDA* Depth 9', linestyle = "--")
#plt.plot(x, d10cumsum, label = 'IDA* Depth 10', linestyle = "--")

plt.plot(x, d5cumsum, label = 'IDA* Optimised Depth 5')
plt.plot(x, d6cumsum, label = 'IDA* Optimised Depth 6')
plt.plot(x, d7cumsum, label = 'IDA* Optimised Depth 7')
plt.plot(x, d8OPcumsum, label = 'IDA* Optimised Depth 8')

plt.xlabel('Number of Cubes Solved')
plt.ylabel('Time (s)')
plt.title("Cumulative Time to Prune + Solve")
plt.legend()
plt.show()

