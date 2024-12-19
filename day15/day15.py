

# path_map = "./day15/inputs/day15_input_map.txt"
# path_inst = "./day15/day15_input_inst.txt"

path_map = "./day15/inputs/day15_test1_map.txt"
path_inst = "./day15/inputs/day15_test1_inst.txt"

# path_map = "./day15/inputs/day15_test2_map.txt"
# path_inst = "./day15/inputs/day15_test2_inst.txt"

with open(path_map) as map_file:
    wh_map = map_file.read().splitlines()

wh_map = [[s for s in row] for row in wh_map]

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
    
    def value(self):
        return wh_map[self.r][self.c]

start = [(row, col) for row in range(len(wh_map)) for col in range(len(wh_map[0])) if wh_map[row][col] == '@'][0]

pos = Coor(start)


def show_wh_map():
    for r in wh_map:
        print(r)

def can_i_move(sym, pos, dir):
    
    next_pos = pos.next_pos(dir)
    next_pos_value = next_pos.value()

    if next_pos_value == '#': 
        return False

    if next_pos_value == '.':
        wh_map[next_pos.r][next_pos.c] = sym
        wh_map[pos.r][pos.c] = '.'
        return True
    
    if next_pos_value == 'O':
        if can_i_move('O', next_pos ,dir):
            wh_map[next_pos.r][next_pos.c] = sym
            wh_map[pos.r][pos.c] = '.'
            return True
    return False    

show_wh_map()

for i in inst:
    # print(i)
    if can_i_move('@',pos,i):
        pos = pos.next_pos(i)

print("end")
# show_wh_map()
print(pos.position())

sum = 0 
for r_ind, r in enumerate(wh_map):
    for c_ind, c in enumerate(r): 
        if c == 'O':
            sum += r_ind * 100 + c_ind


print(sum)
