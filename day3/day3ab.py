import numpy as np

class Claim:

    def parse(self, imp=""):
        '''Parsing these inputs is THE worst'''
        myparse = imp.replace(" ","").replace("@",":").replace("x",",").replace("#","")
        index, coords, dimensions = myparse.split(":")
        x, y = coords.split(",")
        return index, x, y, dimensions

    def __init__(self, imp=""):
        p = self.parse(imp)
        self.index = int(p[0])
        self.x = int(p[1])
        self.y = int(p[2])
        self.dimensions = p[3].split(",")
        self.horiz = self.x + int(self.dimensions[0])
        self.vert = self.y + int(self.dimensions[1])

    def __str__(self):
        return "Index: {}\nX-Coord: {}\nY-Coord: {}\nDimensions of sample: {}\nH: {}\nV: {}".format(self.index,self.x,self.y,self.dimensions,self.horiz,self.vert)

# FILE HANDLING

file = open("day3input.txt","r")
readme = file.read().splitlines()

# DECLARATIONS

patterns = []
winner = "Oops, something went wrong!"

# BUILDING THE HOLIDAY MATRIX

matrix = np.zeros((1000,1000))

# PROCESS THE FILE
# append each object to patterns list for part b
# olap slices the dimensions of the pattern
# if any element is > 0, replace element with -1
# if any element is not -1, replace element with object's index

for line in readme:
    p = Claim(line)
    patterns.append(p)
    olap = matrix[p.x:p.horiz,p.y:p.vert]
    olap[olap > 0] = -1
    olap[olap != -1] = p.index

# CHECK FOR THE ONE TRUE PATTERN
# loop through the list of objects
# slice the dimensions of the object's pattern again
# if all elements in the pattern are the index, we found the pattern

for c in patterns:
    check = matrix[c.x:c.horiz,c.y:c.vert]
    if np.count_nonzero(check != c.index) == 0:
        winner = c.index

# LOVELY HOLIDAY OUTPUT

print("Square inches of overlap: {}\nIndex with NO overlap at all: {}".format(np.count_nonzero(matrix == -1),winner))
