#  attempt 3 looks for horizontal lines in the grid of each iteration.
# the answer is one more than the iter, because the grids[0] is populated after 1 second.


import re
import numpy as np
from PIL import Image

path = "./day14/day14_input.txt"
num_x = 101
num_y = 103


# path = "./day14/day14_test.txt"
# num_x = 11
# num_y = 7


with open(path) as file:
    lines = file.read().splitlines()

# print(lines)


num_iter = num_x * num_y * 2

regex = r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)"

class State:
    def __init__(self, px, py, vx, vy, num_x, num_y):
        self.px = px
        self.py = py
        self.vx = vx
        self.vy = vy
        self.num_x = num_x
        self.num_y = num_y
    

    def update(self): 
        self.px = (self.px + self.vx ) % num_x
        self.py = (self.py + self.vy ) % num_y

    def print_state(self):
        print(f"px: {self.px}, py: {self.py}")


def print_grid(grid):
    grid = grid * 255
    img = Image.fromarray(grid)
    img.show()


states =[]
for l in lines:
    tup = re.findall(regex, l)[0]
    state = State(int(tup[0]), int(tup[1]), int(tup[2]), int(tup[3]), num_x, num_y)
    states.append(state)


grids = np.zeros((num_iter, num_y, num_x))
for i in range(num_iter):
    for s in states:
        s.update()
        grids[i][s.py][s.px] += 1


# look for horzontal lines
filter = np.ones(10) 

for g_ind, g in enumerate(grids):
    for y in range (num_y): 
        for x in range (0, num_x - filter.size): 
            slice = g[y ,  x: x + filter.size]
            score = np.sum(slice * filter)
            if score >= filter.size:
                print(f"iter: {g_ind}, x: {x}, y: {y}")
                print_grid(g)
                break


print(filter.size)

