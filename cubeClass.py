import numpy as np
import copy

class Cube:
    def __init__(self, front, back, up, down, left, right):
            self.front = np.array(front)  #red 
            self.back = np.array(back)    #orange
            self.up = np.array(up)        #white
            self.down = np.array(down)    #yellow
            self.left = np.array(left)    #green
            self.right = np.array(right)  #blue
            self.faceList = [front, back, up, down, left, right]
            self.colours = ['r', 'o', 'w', 'y', 'g', 'b']

    def validation(self):
        #not finished
        counterList = []
        colourCounts = []

        #create dictionary of count of characters in each cube face
        for x in self.faceList:
            counterList.append({item: x.count(item) for item in x})

        #iterate through each face and count the amount of each colour
        #number of each colour stored in colourCounts
        for i in self.colours:
            sum = 0

            for x in counterList:
                if x.get(i) is not None:
                    sum += x.get(i)

            colourCounts.append(sum)

        print(colourCounts)

    def printCube(self):
        """printTemplate = "{} {} {} \n{} {} {}\n{} {} {}\n {} {} {}"
        print(*[f"{self.up[i][j]}" for i in range(3) for j in range(3)])
        print(printTemplate.format(*[f"{self.up[i][j]}" for i in range(3) for j in range(3)]))"""

        for j in range(3):
            print('       ', *self.up[j, :])
        for j in range(3):
            print(*self.left[j, :], ' ', *self.front[j, :], ' ', *self.right[j, :], ' ', *self.back[j, :])
        for j in range(3):
            print('       ', *self.down[j, :])        
            
    def F(self):
        #isolate one face as our placeholder, then swap subsequent values
        downSwap = copy.deepcopy(self.down[0, :])

        #start with placeholder face swap then work around
        self.down[0, :] = self.right[:, 0]
        self.right[:, 0] = self.up[2, :]
        self.up[2, :] = self.left[:, 2]
        self.left[:, 2] = downSwap

        #finally rotate face
        self.front = np.rot90(self.front, 3)


    def U(self):
        frontSwap = copy.deepcopy(self.front[0, :])

        self.front[0, :] =  self.right[0, :]
        self.right[0, :] = self.back[0, :]
        self.back[0, :] = self.left[0, :]
        self.left[0, :] = frontSwap


        self.up = np.rot90(self.up, 3)

    def D(self):
        backSwap = copy.deepcopy(self.back[2, :])

        self.back[2, :] = self.right[2, :]
        self.right[2, :] = self.front[2, :]
        self.front[2, :] = self.left[2, :]
        self.left[2, :] = backSwap

        self.down = np.rot90(self.down, 3)

    def B(self):
        downSwap = copy.deepcopy(self.down[2, :])

        self.down[2, :] = self.left[:, 0]
        self.left[:, 0] = self.up[0, :][::-1]
        self.up[0, :] = self.right[:, 2]
        self.right[:, 2] = downSwap[::-1]

        self.back = np.rot90(self.back, 3)

    def L(self):

        downSwap = copy.deepcopy(self.down[:, 0])

        self.down[:, 0] = self.front[:, 0]
        self.front[:, 0] = self.up[:, 0]
        self.up[:, 0] = self.back[:, 2][::-1]
        self.back[:, 2] = downSwap[::-1]

        self.left = np.rot90(self.left, 3)

    def R(self):

        downSwap = copy.deepcopy(self.down[:, 2])

        self.down[:, 2] = self.back[:, 0][::-1]
        self.back[:, 0] = self.up[:, 2][::-1]
        self.up[:, 2] = self.front[:, 2]
        self.front[:, 2] = downSwap

        self.right = np.rot90(self.right, 3)
    



