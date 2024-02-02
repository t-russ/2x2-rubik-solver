#Solved set of faces for testing

Sfront = ['r', 'r', 'r',
         'r', 'r', 'r',
         'r', 'r', 'r']

Sback =  ['o', 'o', 'o',
         'o', 'o', 'o',
         'o', 'o', 'o']

Sup =    ['w', 'w', 'w',
         'w', 'w', 'w',
         'w', 'w', 'w']

Sdown =  ['y', 'y', 'y',
         'y', 'y', 'y',
         'y', 'y', 'y']

Sleft =  ['g', 'g', 'g',
         'g', 'g', 'g',
         'g', 'g', 'g']

Sright = ['b', 'b', 'b',
         'b', 'b', 'b',
         'b', 'b', 'b']



class Cube:
    def __init__(self, front, back, up, down, left, right):
            self.front = front  #red 
            self.back = back    #orange
            self.up = up        #white
            self.down = down    #yellow
            self.left = left    #green
            self.right = right  #blue
            self.faceList = [front, back, up, down, left, right]
            self.colours = ['r', 'o', 'w', 'y', 'g', 'b']

    def validation(self):
        counterList = []
        colourCounts = []

        for x in self.faceList:
            counterList.append({item: x.count(item) for item in x})

        for i in self.colours:
            sum = 0

            for x in counterList:
                if x.get(i) is not None:
                    sum += x.get(i)

            colourCounts.append(sum)

        print(colourCounts)


testCube = Cube(Sfront, Sback, Sup, Sdown, Sleft, Sright)

testCube.validation()


