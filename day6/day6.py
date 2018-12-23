from collections import defaultdict

# Setup A: Parse the data

file = open("day6input.txt", "r")
readme = file.read().splitlines()

coords = list()

for line in readme:
    c = line.split(", ")
    coords.append((int(c[0]),int(c[1])))

print("Coordinates Processed")

# Setup B: Define the Manhattan distance function

def manhattan(p1,p2):
    ''' Manhattan distance: The absolute value of (x1 - x2) + (y1-y2) '''
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

# Step 1: Find the borders of The Box

x_left = min([x[0] for x in coords])
x_right = max([x[0] for x in coords])
y_top = min([y[1] for y in coords])
y_bottom = max([y[1] for y in coords])

box = {
    "x" : range(x_left,x_right+1),
    "y" : range(y_top,y_bottom+1)
    }

print("Box Defined")

# Step 2: Eliminate all the coordinates sitting on The Box's borders

infinite = set()
print("Plucking out those nasty infinite coordinates in the test set")

for point in coords:
    if point[0] == x_left or point[0] == x_right or point[1] == y_top or point[1] == y_bottom:
        infinite.add(point)

# Step 3: Work through The Grid point by point

dist = dict() # part one
area = defaultdict(int) # part one
dist_to_all = dict() # part two
safe = 0 # part two

print("Working through ALL THE POINTS... patience please!")

for x in range(0, x_right+1):
    for y in range(0, y_bottom+1):
        dist[(x,y)] = min([(manhattan(point, (x,y)),point) for point in coords])
        dist_to_all[(x,y)] = sum([manhattan(point, (x,y)) for point in coords])
        if x not in box["x"] or y not in box['y']: # part one
            infinite.add((x,y))
        if dist_to_all[(x,y)] < 10000: # part two
            safe += 1

# Step 4: Count up the areas for points not in the infinite point set

print("Counting the areas")

for grid_coord, point in dist.items():
    if grid_coord not in infinite:
        area[point[1]] += 1

# Step 5: SOLUTIONS

# Part One Answer (with provided day6input.txt): 5187
print(f"Part One: {max((val, key) for key, val in area.items())}")
# Part Two Answer (with provided day6input.txt): 34829
print(f"Part Two: {safe}")
