import numpy as np
from Cube import applyMoveString, stringToMoves, applyMove

#Maps characters to their Ansi escape sequence, allows for colour printing in terminal
colourMap = {'R' : '\033[31mR\033[0m',
             'O' : '\033[38;5;208mO\033[0m',
             'B' : '\033[38;5;12mB\033[0m',
             'G' : '\033[38;5;10mG\033[0m',
             'W' : '\033[38;5;15mW\033[0m',
             'Y' : '\033[38;5;11mY\033[0m'}



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



def printMoveString(cubeState, moveString, colouring):
     moveArr = stringToMoves(moveString)
     print("\n--------------- STARTING STEP-BY-STEP PRINTING ---------------")
     print("Initial State:")
     printCube(cubeState, colouring)
     n = 1
     for i in moveArr:
          cubeState = applyMove(cubeState, i)
          print(f"Move {n}: Applying Move {i} ")
          printCube(cubeState, colouring)
          n+=1
