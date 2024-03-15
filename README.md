<h1>Optimal Moves 2x2x2 Rubik's Cube Solver</h1>

<p>Python implementation of iterative deepening and IDA* graph search algorithms to generate least move solutions to the 2x2x2 Rubik's cube

Requirements:  `numpy`, `pickle`. </p>

<h2>Usage</h2>

<p>
<b>Cube modelled in form:</b>
  
```
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
```

Each cubie face has a different index within a 24-length array that stores the cube's state.

</p>
<h3>Move Notation:</h3>
<p>
Letter - denotes cube face: F = Front, R = Right, U = Up.

F - 90 degree clockwise turn of the front face.

F2 - 180 degree turn of front face.

F' - 90 degreee anti-clockwise turn of front face.

The same applies to U, R.
For more information on cube notation - https://ruwix.com/the-rubiks-cube/notation/
</p>

<h3>Generating Solutions:</h3>
<p>
DLB (down left back) corner is fixed, so only moves F, F2, F', U, U2, U', R, R2, and R' are needed.
  
Choose a DLB corner and get faces from this. 
Orientation must be preserved, with respect to the front face, to ensure a solution is found.
If done correctly, the front face will have index 0-3 within the cube array.

In `main.py` enter cube state into `cube` and call solve functions. 
Two different solvers are available: `iterativeDeepening` and `idaStar`. Both take the cube state as their first parameter.

Both solvers have two returns:

1. The move string that solves the cube
2. Time to solve in seconds.

For IDA* solver (`idaStar`), a pruning table must be chosen as the second parameter; 4 tables of different depths are available, 
or the user can generate a table of chosen depth using `prune(n)`, where n is the desired depth.

Note that `iterativeDeepening` is considerably slower than `idaStar` when using high-depth pruning tables.

</p>
