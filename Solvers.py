import Cube

"""Create a map that takes last move and returns list of acceptable next moves
   this removes basic redundant sequences of moves such as F2 F2, F F' etc."""

alias = {"F" : "id1", "F2" : "id1", "F'" : "id1",
            "U" : "id2", "U2" : "id2", "U'" : "id2",
            "R" : "id3", "R2" : "id3", "R'" : "id3"
            }

nextMoveMap = {"id1" : ["U", "U2", "U'", "R", "R2", "R'"],
         "id2" : ["F", "F2", "F'", "R", "R2", "R'"],
         "id3" : ["F", "F2", "F'", "U", "U2", "U'"]}



def depthFirstSearch(cubeState, maxDepth):
    moveStack = []
    initialMoves = ["F", "F2", "F'", "U", "U2", "U'", "R", "R2", "R'"]
    dfsRecursive(cubeState, maxDepth, 0, moveStack, initialMoves)
    print(' '.join(moveStack))

def dfsRecursive(cubeState, maxDepth, depth, moveStack, nextMove):
    for m in nextMove:
        nextState = Cube.applyMove(cubeState, m)
        moveStack.append(m)
        depth += 1

        if Cube.solved(nextState):return True
        if depth >= maxDepth: return False

        if dfsRecursive(nextState, maxDepth, depth, moveStack, nextMoveMap[alias[m]]):
            return True
        depth -= 1
        moveStack.pop()
            
    
    return False

depthFirstSearch(Cube.testcube, 15)

            
