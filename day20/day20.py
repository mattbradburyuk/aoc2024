from collections import Counter


path = "./day20/day20_input.txt"
# path = "./day20/day20_test.txt"

with open(path) as file: 
    lines = file.read().splitlines()

grid = [[i for i in row] for row in lines]    # this may not be necessary

start = [(r,c) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == 'S'][0]
end = [(r,c) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == 'E'][0]

# print(f"start coor: {start}, end coor: {end}")

# STEP 1 - mark up the secs from start on the grid

UP = (-1,0)
RIGHT = (0,1)
DOWN = (1,0)
LEFT = (0,-1)

def next_pos(cur, dir):
    return (cur[0]+ dir[0], cur[1]+ dir[1])

def in_bounds(grid, pos):
    return (pos[0] >= 0 and
            pos[1] >= 0 and
            pos[0] < len(grid) and
            pos[1] < len(grid[0]))

def grid_value(grid, pos):
    return grid[pos[0]][pos[1]]

def set_grid_value(grid, pos, value):
    grid[pos[0]][pos[1]] = value

pos = start
secs = 0
set_grid_value(grid, pos, secs)

loop = True
while loop:
    secs += 1
    # Find next position
    up = next_pos(pos, UP)
    right = next_pos(pos, RIGHT)
    down = next_pos(pos, DOWN)
    left = next_pos(pos, LEFT)

    if in_bounds(grid, up) and (grid_value(grid, up) == '.' or grid_value(grid, up) == 'E'): pos = up
    if in_bounds(grid, right) and (grid_value(grid, right) == '.' or grid_value(grid, right) == 'E'): pos = right
    if in_bounds(grid, down) and (grid_value(grid, down) == '.' or grid_value(grid, down) == 'E'): pos = down
    if in_bounds(grid, left) and (grid_value(grid, left) == '.' or grid_value(grid, left) == 'E'): pos = left  
        
    if grid_value(grid, pos) == 'E': 
        loop = False
    set_grid_value(grid, pos, secs)


# STEP 2 - Identify short cuts

UP2 = (-2,0)
RIGHT2 = (0,2)
DOWN2 = (2,0)
LEFT2 = (0,-2)

cheats = []

def check_for_shortcut(grid, pos, dir):
    np = next_pos(pos, dir)
    if in_bounds(grid, np) and isinstance(grid_value(grid, np),int):
        short_cut = grid_value(grid, np) - grid_value(grid, pos) - 2
        if (short_cut > 0):
            cheats.append(short_cut)
    
for ind_row, row in enumerate(grid):
    for ind_col, tile in enumerate(row):
        if isinstance(tile, int):
            check_for_shortcut(grid, (ind_row, ind_col), UP2)    
            check_for_shortcut(grid, (ind_row, ind_col), RIGHT2) 
            check_for_shortcut(grid, (ind_row, ind_col), DOWN2) 
            check_for_shortcut(grid, (ind_row, ind_col), LEFT2)     

counts = Counter(cheats)

threshold = 100

over_threshold = sum(value for key, value in counts.items() if key >= threshold ) 

print(over_threshold)