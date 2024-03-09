<h1>Optimal Moves 2x2x2 Rubik's Cube Solver</h1>

<p>Python implementation of iterative deepening and IDA* graph search algorithms to generate least move solutions to the 2x2x2 Rubik's cube

Requirements:  `numpy`, `pickle`. </p>

<h2>Usage</h2>

<p>
Cube modelled in form:
  
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

Each facelet has a different indice with a 24 length list used to store the state of the cube.

DLB (down left back) corner is fixed so only moves F, F2, F', U, U2, U', R, R2, R' are needed

<h3>Move Notation:</h3>
Letter - denotes cube face. F = Front, R = Right, U = Up.

F - 90 degree clockwise turn of the front face.
F2 - 180 degree turn of front face.
F' - 90 degreee anti-clockwise turn of front face.

Same applies of U, R.


Choose a DLB corner, orient cube around this with Front Face being indices 0-3.
Enter into 'cube' array below and then call solving functions






  
</p>
