# This worked for the test case but not for the real thing - hyptohesis is that when a box is blocked by 
# 2 boxes it checks if the first one can move, then moves it before checking if the second one can move. 
# if the second one can't move then it shouldn't have moved the first.

# Need to have more extensive unit tests, so restructuring to allow unit test set up.

# path_map = "./day15/inputs/day15_input_map.txt"
# path_inst = "./day15/inputs/day15_input_inst.txt"

# path_map = "./day15/inputs/day15_test1_map.txt"
# path_inst = "./day15/inputs/day15_test1_inst.txt"

path_map = "./day15/inputs/day15_test2_map.txt"
path_inst = "./day15/inputs/day15_test2_inst.txt"

# path_map = "./day15/inputs/day15_part2_uptest_map.txt"
# path_inst = "./day15/inputs/day15_part2_uptest_inst.txt"

# path_map = "./day15/inputs/day15_test3_small_map.txt"
# path_inst = "./day15/inputs/day15_test3_small_inst.txt"


with open(path_map) as map_file:
    wh_map = map_file.read().splitlines()

wh_map = [[s for s in row] for row in wh_map]

large_map = []

for row in wh_map:
    new_row = []
    for tile in row: 
        if tile == '#': new_row += ['#', '#']
        if tile == 'O': new_row += ['[', ']']
        if tile == '.': new_row += ['.', '.']
        if tile == '@': new_row += ['@', '.']
    large_map.append(new_row)

def show_wh_map():
    for r in wh_map:
        row = "".join(r)
        print(row)

def show_large_map():
    for r in large_map:
        row = "".join(r)
        print(row)



with open(path_inst) as inst_file:
    inst = inst_file.read()
    inst = [s for row in inst for s in row if s != '\n']  # flatten inst + remove return

# print(inst)

class Coor:
    def __init__(self, pos):
         self.r = pos[0]
         self.c = pos[1]

    def next_pos(self, dir):
        if dir == '^': return Coor((self.r -1  , self.c))
        if dir == '>': return Coor((self.r , self.c + 1))
        if dir == 'v': return Coor((self.r + 1 , self.c))
        if dir == '<': return Coor((self.r , self.c-1))
        raise Exception("not a direction")
    
    def position(self): 
        return (self.r, self.c)
    
    def offset(self, r, c):
        return Coor((self.r + r, self.c + c))
    
    def value(self):
        return large_map[self.r][self.c]

start = [(row, col) for row in range(len(large_map)) for col in range(len(large_map[0])) if large_map[row][col] == '@'][0]

pos = Coor(start)

def can_robot_move(pos, dir):
    
    next_pos = pos.next_pos(dir)
    next_pos_value = next_pos.value()
    
    can_move = False

    if next_pos_value == '#': 
        pass

    elif next_pos_value == '.': 
        can_move =  True

    elif next_pos_value == '[':
        can_move = can_box_move(next_pos, dir)
    
    elif next_pos_value == ']':
        can_move = can_box_move(next_pos.offset(0,-1), dir)  # box position is one to the left

    if can_move:
        large_map[next_pos.r][next_pos.c] = '@'
        large_map[pos.r][pos.c] = '.'
        return True
    else:
        return False



def can_box_move(box_pos,dir):
    
    can_move = False

    if dir == '^':
        up_left = box_pos.offset(-1,0).value()
        up_right = box_pos.offset(-1,1).value()

        if up_left == '#' or up_right == '#': 
            can_move == False
        elif up_left == '.' and up_right == '.': 
            can_move = True
        elif up_left == ']' and up_right == '[':
            can_move = (can_box_move(box_pos.offset(-1,-1),dir) and 
                            can_box_move(box_pos.offset(-1,1),dir))
        elif up_left == ']':
            can_move = can_box_move(box_pos.offset(-1,-1) ,dir)
        elif up_left == '[':
            can_move = can_box_move(box_pos.offset(-1,0), dir)
        elif up_right == '[':
            can_move = can_box_move(box_pos.offset(-1,1) , dir) 

        if can_move:
            large_map[box_pos.r - 1][box_pos.c] = '['
            large_map[box_pos.r -1][box_pos.c + 1] = ']'
            large_map[box_pos.r][box_pos.c] = '.'
            large_map[box_pos.r][box_pos.c + 1] = '.'
            return True
        else: 
            return False
        
    if dir == '>':
        right = box_pos.offset(0,2).value()
        
        if right == '#': 
            can_move = False
        elif right == '.': 
            can_move = True
        elif right == '[':
            can_move = can_box_move(box_pos.offset(0,2), dir)

        if can_move:
            large_map[box_pos.r][box_pos.c] = '.'
            large_map[box_pos.r][box_pos.c + 1] = '['
            large_map[box_pos.r][box_pos.c + 2] = ']'
            return True
        else: 
            return False

    if dir == 'v':
        down_left = box_pos.offset(1,0).value()
        down_right = box_pos.offset(1,1).value()

        if down_left == '#' or down_right == '#': 
            can_move == False
        elif down_left == '.' and down_right == '.': 
            can_move = True
        elif down_left == ']' and down_right == '[':
            can_move = (can_box_move(box_pos.offset(1,-1),dir) and 
                            can_box_move(box_pos.offset(1,1),dir))
        elif down_left == ']':
            can_move = can_box_move(box_pos.offset(1,-1) ,dir)
        elif down_left == '[':
            can_move = can_box_move(box_pos.offset(1,0), dir)
        elif down_right == '[':
            can_move = can_box_move(box_pos.offset(1,1) , dir) 

        if can_move:
            large_map[box_pos.r + 1][box_pos.c] = '['
            large_map[box_pos.r + 1][box_pos.c + 1] = ']'
            large_map[box_pos.r][box_pos.c] = '.'
            large_map[box_pos.r][box_pos.c + 1] = '.'
            return True
        else: 
            return False

    if dir == '<':
        left = box_pos.offset(0,-1).value()
        
        if left == '#': 
            can_move = False
        elif left == '.': 
            can_move = True
        elif left == ']':
            can_move = can_box_move(box_pos.offset(0,-2), dir)

        if can_move:
            large_map[box_pos.r][box_pos.c + 1] = '.'
            large_map[box_pos.r][box_pos.c ] = ']'
            large_map[box_pos.r][box_pos.c -1 ] = '['
            return True
        else: 
            return False

print(pos.position())

show_wh_map()
show_large_map()
for i_ind, i in enumerate(inst):
    # print(f"i_ind: {i_ind}, instruction: {i}")
    if can_robot_move(pos,i):
        pos = pos.next_pos(i)
        # show_large_map()

show_large_map()
sum = 0 
for r_ind, r in enumerate(large_map):
    for c_ind, c in enumerate(r): 
        if c == '[':
            sum += r_ind * 100 + c_ind



print(sum)


