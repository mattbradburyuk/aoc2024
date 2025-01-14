

# path = "./day25/day25_test.txt"
path = "./day25/day25_input.txt"

with open(path)as file:
     grids = file.read().split("\n\n")


def parse_lock(grid):
    lock = [0,0,0,0,0]
    lines = grid.splitlines()
    for line_ind, line in enumerate(lines):
        for cha_ind, cha in enumerate(line):
            if cha == '#':
                lock[cha_ind] = line_ind
    return lock


def parse_key(grid): 
    key = [0,0,0,0,0]
    lines = grid.splitlines()
    lines = lines[::-1]
    for line_ind, line in enumerate(lines):
        for cha_ind, cha in enumerate(line):
            if cha == '#':
                key[cha_ind] = line_ind
    return key


keys = []
locks = []
for g in grids:
    if g[0] == '#': 
        locks.append(parse_lock(g)) 
    else:
        keys.append(parse_key(g))
     
count = 0
for lock in locks:
    for key in keys: 
        summed = list(map(lambda l,k: l+k, lock, key))
        if all(x <= 5 for x in summed):
            count +=1

print(count)





