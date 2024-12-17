import re
import time
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

num_iter = 100000000

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
        self.quad = self.in_quad()

    def print_state(self):
        print(f"px: {self.px}, py: {self.py}, quad: {self.quad}")


    # def in_quad(self):
    #     if self.px in range(0, num_x // 2) and self.py in range(0, num_y //2 ): return 1
    #     if self.px in range(num_x - num_x // 2 , num_x) and self.py in range(0, num_y //2 ): return 2
    #     if self.px in range(0, num_x //2) and self.py in range (num_y - num_y //2, num_y ): return 3
    #     if self.px in range(num_x - num_x // 2 , num_x) and self.py in range (num_y - num_y //2, num_y ): return 4
        
        # faster
    def in_quad(self):
        if self.px <= num_x // 2 and self.py <= num_y //2: return 1
        if self.px > num_x // 2 and self.py <= num_y //2: return 2
        if self.px <= num_x // 2 and self.py > num_y //2: return 3
        return 4

def print_grid():
    img = Image.new('RGB', (num_x, num_y), 'white')
    pix = img.load()
    for s in states:
        pix[s.px,s.py] = (0,255,0)
    img.show()

def get_sf():
    counts = [1,1,1,1,1]  # add counts[0] to avoid quad 0 being false
    for s in states: 
        # s.print_state()
        if s.quad:
            counts[s.quad] +=1 
    
    sf = 1 
    for c in counts:
        sf = sf * c
    
    return sf 

states =[]
for l in lines[:100]:
    tup = re.findall(regex, l)[0]
    state = State(int(tup[0]), int(tup[1]), int(tup[2]), int(tup[3]), num_x, num_y)
    states.append(state)

lowest = 10000000000000000000

tic = time.time()
for i in range(num_iter):
    
    if not i % 1000000: 
        toc = time.time()
        print(f"iter: {i}, time: {toc - tic}")
        tic = toc

    for s in states:
        s.update()

    sf = get_sf()
    if sf < lowest:
        lowest = sf 
        print(f"lower sf: iter: {i}, sf: {sf}")
        print_grid()    







