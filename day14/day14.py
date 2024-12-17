import re

path = "./day14/day14_input.txt"
# path = "./day14/day14_test.txt"

with open(path) as file:
    lines = file.read().splitlines()

# print(lines)

num_x = 101
num_y = 103
num_iter = 100

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


    def in_quad(self):
        if self.px in range(0, num_x // 2) and self.py in range(0, num_y //2 ): return 1
        if self.px in range(num_x - num_x // 2 , num_x) and self.py in range(0, num_y //2 ): return 2
        if self.px in range(0, num_x //2) and self.py in range (num_y - num_y //2, num_y ): return 3
        if self.px in range(num_x - num_x // 2 , num_x) and self.py in range (num_y - num_y //2, num_y ): return 4
        

states =[]
for l in lines:
    tup = re.findall(regex, l)[0]
    state = State(int(tup[0]), int(tup[1]), int(tup[2]), int(tup[3]), num_x, num_y)
    states.append(state)

for i in range(num_iter):
    for s in states:
        s.update()




counts = [1,0,0,0,0]  # add counts[0] to avoid quad 0 being false
for s in states: 
    # s.print_state()
    if s.quad:
        counts[s.quad] +=1 
    
sf = 1 
for c in counts:
    sf = sf * c

print(sf)





