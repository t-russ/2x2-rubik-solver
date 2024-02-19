import numpy as np

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
A 24 length array is used to store the state of the cube with each colour
being associated with a number

0: red
1: blue
2: orange
3: green
4: white
5: yellow

Moves are modelled as permutations. 
each value in the array displays where each index in the current state of the cube goes.
"""

moveMap = {F:0, U:1, R:2}

moves = np.array(
    [2, 0, 3, 1, 18, 5, 19, 7, 8, 9, 10, 11, 12, 20, 14, 21, 16, 17, 15, 13, 6, 4, 22, 23],
    [4, 5, 2, 3, 8, 9, 6, 7, 12, 13, 10, 11, 0, 1, 14, 15, 18, 16, 19, 17, 20, 21, 22, 23],
    [])