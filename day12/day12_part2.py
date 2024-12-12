# Part 2
# Note, the trick here is to count corners not continuous sides, you must have the same number of sides as corners


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

def get_letter(coor): return grid[coor.r][coor.c]

def check_corners(coor, letter):
    corners = 0
    
    up = coor.up()
    right = coor.right()
    down = coor.down()
    left = coor.left()

    # get fences
    top_fence  = True if not is_inbounds(up) else True if get_letter(up) != letter else False
    right_fence = True if not is_inbounds(right) else True if get_letter(right) != letter else False
    bottom_fence = True if not is_inbounds(down) else True if get_letter(down) != letter else False
    left_fence = True if not is_inbounds(left) else True if get_letter(left) != letter else False


    # get outside corners
    if top_fence and right_fence: corners += 1
    if right_fence and bottom_fence: corners += 1
    if bottom_fence and left_fence: corners += 1
    if left_fence and top_fence: corners += 1

    # find inside corners

    # top right 
    if (is_inbounds(up) and get_letter(up) == letter and 
        is_inbounds(right) and get_letter(right) == letter and 
        get_letter(Coor(up.r, right.c)) != letter): 
        corners += 1
    # bottom right    
    if (is_inbounds(down) and get_letter(down) == letter and 
        is_inbounds(right) and get_letter(right) == letter and 
        get_letter(Coor(down.r, right.c)) != letter): 
        corners += 1
    # top left
    if (is_inbounds(up) and get_letter(up) == letter and 
        is_inbounds(left) and get_letter(left) == letter and 
        get_letter(Coor(up.r, left.c)) != letter): 
        corners += 1
    # bottom left
    if (is_inbounds(down) and get_letter(down) == letter and 
        is_inbounds(left) and get_letter(left) == letter and 
        get_letter(Coor(down.r, left.c)) != letter): 
        corners += 1

    return 1, corners


# Recursive function checks a square and returns a cumulative value for (area, perimeter)
def find_group(coor: Coor, letter):
    
    # check if this coor is out of bounds
    if not is_inbounds(coor): return (0,0)

    # Check if this grid matches the letter
    if get_letter(coor) != letter: return (0,0)

    # Check if this square has been visited before
    if visited_grid[coor.r][coor.c] == True: return (0,0)
    
    # Mark grid as visited
    visited_grid[coor.r][coor.c] = True 
    
    # get this square area and perimeter
    a, c = check_corners(coor, letter)
    
    # check up
    u_a, u_c = find_group(coor.up(), letter)
    # check right
    r_a, r_c = find_group(coor.right(), letter)
    # check down
    d_a, d_c = find_group(coor.down(), letter)
    # check left
    l_a, l_c = find_group(coor.left(), letter)

    area_sum = a + u_a + r_a + d_a + l_a
    corners_sum = c + u_c + r_c + d_c + l_c

    return area_sum, corners_sum

sum_price = 0 
for r, row in enumerate(grid):
    for c, l in enumerate(row): 
        # print(f"grid[{r}][{c}]: {l}")

        if not visited_grid[r][c]:
            
            area, corners = find_group(Coor(r,c), grid[r][c])
            print(f"file coor: {r+1},{c+1}, letter: {grid[r][c]}, area: {area}, corners: {corners}, price: {area * corners}")
            sum_price += area * corners

print(sum_price)









