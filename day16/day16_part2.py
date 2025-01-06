from collections import namedtuple


# read in grid
# path = "./day16/day16_test1.txt"
# path = "./day16/day16_test2.txt"
path = "./day16/day16_input.txt"

with open(path) as file: 
    lines = file.read().splitlines()
grid = [[c for c in l ] for l in lines]

# for row in grid:
#     print(row)

NORTH = (-1,0)
EAST = (0,1)
SOUTH = (1,0)
WEST = (0,-1)

class Node():
    def __init__(self,row, col, dir, dist, previous):
        self.row = row
        self.col = col
        self.dir = dir
        self.dist = dist
        self.previous_nodes = previous

class TileMap(): 
    def __init__(self, grid): 
        self.grid = grid
        start_node = self.find_start()
        self.found = {self.gen_key(start_node): start_node}
        self.visited = {}
        self.end_coor = self.find_end_coor()
        self.locations = []

    # creates a dictionary key from a node
    def gen_key(self, node):
        return (node.row, node.col, node.dir)

    def find_start(self):
        for row_ind, row in enumerate(self.grid):
            for col_ind, col in enumerate(row):
                if col == 'S': 
                    return Node(row_ind,col_ind, EAST, 0 , [])

    def find_end_coor(self):
        for row_ind, row in enumerate(self.grid):
            for col_ind, col in enumerate(row):
                if col == 'E': 
                    return (row_ind,col_ind)


    def run_rounds(self):
        while len(self.found) > 0:
            self.round()


    def round(self): 
        
        if len(self.found) > 0:
            # find the node with the shortest path
            key = min(self.found, key = lambda k: self.found[k].dist)
        else: 
            print("no more nodes in found list")
            return

        #check next node
        self.check_forward(key)
        self.check_turn(key, "left")
        self.check_turn(key, "right")

        # Move node to visited list
        self.visited[key] = self.found[key]
        del self.found[key]
        

    def check_forward(self, key):

        cur_node = self.found[key]
        new_node = Node(cur_node.row + cur_node.dir[0], cur_node.col + cur_node.dir[1], cur_node.dir, cur_node.dist + 1, [key] )
        new_key = self.gen_key(new_node)

        # if node visited, ignore
        if new_key in self.visited: 
            return

        tile = self.grid[new_node.row][new_node.col]
        # not a valid tile
        if tile == '#': 
            return

        # valid tile
        elif tile == '.' or tile == 'E': 
            
            if new_key in self.found:
                existing_node = self.found[new_key]
                #if new path is shorter, update path
                if new_node.dist < existing_node.dist: 
                    existing_node.dist = new_node.dist
                    existing_node.previous_nodes = [key]
                # if new path is equal record it as an additional route to the tile
                if new_node.dist == existing_node.dist:
                    existing_node.previous_nodes.append(key)

            else: 
                # add new_node to visited
                self.found[new_key] = new_node
            
    def check_turn(self,cur_key, rotation):
        cur_node = self.found[cur_key]

        if rotation == "left": 
            if cur_node.dir == NORTH: new_dir = WEST
            if cur_node.dir == WEST: new_dir = SOUTH
            if cur_node.dir == SOUTH: new_dir = EAST
            if cur_node.dir == EAST: new_dir = NORTH
        elif rotation == "right": 
            if cur_node.dir == NORTH: new_dir = EAST
            if cur_node.dir == EAST: new_dir = SOUTH
            if cur_node.dir == SOUTH: new_dir = WEST
            if cur_node.dir == WEST: new_dir = NORTH


        new_node = Node(cur_node.row, cur_node.col, new_dir, cur_node.dist + 1000, [cur_key])
        new_key = self.gen_key(new_node)

        if new_key in self.visited: 
            return

        if new_key in self.found:
            existing_node = self.found[new_key]
            #if new path is shorter, update path
            if new_node.dist < existing_node.dist: 
                existing_node.dist = new_node.dist
                existing_node.previous_nodes = [cur_key]
            # if new path is equal record it as an additional route to the tile
            if new_node.dist == existing_node.dist:
                existing_node.previous_nodes.append(cur_key)    
        else: 
            # add new_node to visited
            self.found[new_key] = new_node 

    def get_lowest_route(self):
        
        end_row, end_col = self.end_coor

        n = self.visited[(end_row, end_col, NORTH)].dist
        e = self.visited[(end_row, end_col, EAST)].dist
        s = self.visited[(end_row, end_col, SOUTH)].dist
        w = self.visited[(end_row, end_col, WEST)].dist

        min_dist = min(n,e,s,w)

        end_keys = []

        if min_dist == n: end_keys.append((end_row, end_col, NORTH))
        if min_dist == e: end_keys.append((end_row, end_col, EAST))
        if min_dist == s: end_keys.append((end_row, end_col, SOUTH))
        if min_dist == w: end_keys.append((end_row, end_col, WEST))
        
        return min_dist, end_keys
            
         

    def get_spots(self, end_keys):
        
        # Build locations
        for ek in end_keys:
            node = self.visited[ek]
            self.add_node(node)

        location_set = set()

        for l in self.locations:
            location_set.add((l.row, l.col))

        return len(location_set)

    # Adds current node to locations and recursivly calls on prior nodes
    def add_node(self, node):
        
        self.locations.append(node)
        for pn in node.previous_nodes:
            self.add_node(self.visited[pn])
        
  

tm = TileMap(grid)

tm.run_rounds()
min_dist, end_keys  = tm.get_lowest_route()
print("shortest route: ", min_dist)

print("number of spots: " , tm.get_spots(end_keys))

