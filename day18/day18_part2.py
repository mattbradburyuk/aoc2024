
# path = './day18/day18_test.txt'
path = './day18/day18_input.txt'

with open(path) as file: 
    inst_strs = file.read().splitlines()


inst =  [(int(x[0]), int(x[1])) for x in [s.split(',') for s in inst_strs]]
# print(inst)

UP = (-1,0)
RIGHT = (0,1)
DOWN = (1,0)
LEFT = (0,-1)

class Grid():

    def __init__(self, inst, dim):
        self.inst = inst
        self.dim = dim

    def generate_grid(self, steps):

        grid = [['.' for c in range(self.dim)] for row in range(self.dim)] 
        
        for ind in range(steps):
            c, r = self.inst[ind]
            grid[r][c] = '#'

        self.grid = grid
    

    def print_grid(self):
        for r in self.grid:
            print(''.join(r))


    def check_node(self, grid, cur_key, dir, found, visited):
        new_key = (cur_key[0] + dir[0], cur_key[1] + dir[1])
        
        # check if new key visited

        if new_key in visited: return

        # check if new_key out of bounds
        if new_key[0] < 0 or new_key[0] >= self.dim or new_key[1] < 0 or new_key[1] >= self.dim: 
            return
        elif grid[new_key[0]][new_key[1]] == '#':
            return
        elif grid[new_key[0]][new_key[1]] == '.':
            # check if key already exists
            if new_key in found: 
                found[new_key] = (min(found[new_key][0],found[cur_key][0]+1),found[cur_key][1])
            else:
                found[new_key] = (found[cur_key][0]+1, (cur_key))


    def shortest_path(self, grid, start, end):
        
        visited = {}
        found = {start: (0, None)}

        while found:

            min_key = min(found, key= lambda k: found[k][0])
            
            self.check_node(grid, min_key, UP, found, visited)
            self.check_node(grid, min_key, RIGHT, found, visited)
            self.check_node(grid, min_key, DOWN, found, visited)
            self.check_node(grid, min_key, LEFT, found, visited)
        
            # Move node to visited list
            visited[min_key] = found[min_key]
            del found[min_key]
            # mark as visited on grid
            grid[min_key[0]][min_key[1]] = 'O'


        if end in visited: 
            # print(f"shortest path: {visited[end][0]}")
            return True
        else: 
            return False



for i in range(2860, len(inst)):
    print(f"index: {i}")

    grid = Grid(inst, 71)
    grid.generate_grid(i)
    # grid.print_grid()
    
    clear = grid.shortest_path(grid.grid, (0,0),(70,70))
    grid.print_grid()
    
    if not clear: 
        print(f"blocked at index: {i}, inst[i]: {inst[i]}")
        break

# output: blocked at index: 2862, inst[i]: (70, 31)

# actually an off by one error, it was the previous instruction 60,46