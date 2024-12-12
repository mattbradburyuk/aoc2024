
path = "./day12/day12_input.txt"
# path = "./day12/day12_test.txt"
# path = "./day12/day12_OX_test.txt"
# path = "./day12/day12_ABCDE_test.txt"

with open(path) as file:
    lines = file.read().splitlines()

grid = [[s for s in l ] for l in lines]

num_rows = len(grid)
num_cols = len(grid[0])

visited_grid = [[False for c in range(num_cols)] for r in range(num_rows)]

class Coor:
    def __init__(self, r, c):
        self.r = r
        self.c = c

    def up(self): return Coor(self.r - 1, self.c)
    def right(self): return Coor(self.r, self.c + 1)
    def down(self): return Coor(self.r + 1, self.c)
    def left(self): return Coor(self.r, self.c - 1)


def is_inbounds(coor):
    return (
        coor.r >= 0 and
        coor.r < num_rows and
        coor.c >= 0 and
        coor.c < num_cols
    )


def check_square(coor, letter):
    adj_letters = 0 
    # check up
    if coor.r - 1 >= 0: 
        if grid[coor.r -1][coor.c] == letter: adj_letters += 1
    # check right
    if coor.c + 1 < num_cols:
        if grid[coor.r][coor.c + 1] == letter: adj_letters += 1
    # check down
    if coor.r + 1 < num_rows:
        if grid[coor.r + 1][coor.c] == letter: adj_letters += 1
    # check left
    if coor.c - 1 >= 0:
        if grid[coor.r][coor.c - 1] == letter: adj_letters += 1 

    return 1, 4 - adj_letters

# Recursive function checks a square and returns a cumulative value for (area, perimeter)
def find_group(coor: Coor, letter):
    
    # check if this coor is out of bounds
    if not is_inbounds(coor): return (0,0)

    # Check if this grid matches the letter
    if grid[coor.r][coor.c] != letter: return (0,0)

    # Check if this square has been visited before
    if visited_grid[coor.r][coor.c] == True: return (0,0)
    
    # Mark grid as visited
    visited_grid[coor.r][coor.c] = True 
    
    # get this square area and perimeter
    a, p = check_square(coor, letter)
    
    # check up
    u_a, u_p = find_group(coor.up(), letter)
    # check right
    r_a, r_p = find_group(coor.right(), letter)
    # check down
    d_a, d_p = find_group(coor.down(), letter)
    # check left
    l_a, l_p = find_group(coor.left(), letter)

    area_sum = a + u_a + r_a + d_a + l_a
    perimeter_sum = p + u_p + r_p + d_p + l_p

    return area_sum, perimeter_sum

sum_price = 0 
for r, row in enumerate(grid):
    for c, l in enumerate(row): 
        # print(f"grid[{r}][{c}]: {l}")

        if not visited_grid[r][c]:
            
            area, perimeter = find_group(Coor(r,c), grid[r][c])
            print(f"file coor: {r+1},{c+1}, letter: {grid[r][c]}, area: {area}, perimeter: {perimeter}, price: {area * perimeter}")
            sum_price += area* perimeter

print(sum_price)











