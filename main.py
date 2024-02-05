from cubeClass import *
import numpy as np
import copy


#Solved set of faces for testing

Sfront = [['r', 'r', 'r'],
         ['t', 'r', 'r'],
         ['r', 'r', 'r']]

Sback =  [['o', 'o', 'o'],
         ['o', 'o', 'o'],
         ['o', 'o', 'f']]

Sup =    [['l', 'w', 'w'],
         ['w', 'w', 'w'],
         ['w', 'w', 'w']]

Sdown =  [['y', 'y', 'y'],
         ['y', 'y', 'y'],
         ['y', 'y', 'y']]

Sleft =  [['g', 'g', 'g'],
         ['g', 'g', 'g'],
         ['g', 'g', 'g']]

Sright = [['b', 'b', 'b'],
         ['b', 'b', 'b'],
         ['b', 'b', 'b']]


testCube = Cube(Sfront, Sback, Sup, Sdown, Sleft, Sright)
"""testCube.R()
testCube.F()
testCube.D()
testCube.U()"""
testCube.L()
#testCube.B()
testCube.printCube()  

#testCube.validation()


x  =  np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
