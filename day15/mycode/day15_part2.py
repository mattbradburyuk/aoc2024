
import time

class Warehouse:
    """
        Solves day15 part 2
    """

    # Loads the original map and transforms it to part2 expanded warehouse
    def __init__(self, map_path, inst_path, original=True):
        
        if original:
            self.load_original_map(map_path)
        else:
            self.load_expanded_map(map_path)


        # Extract instructions
        with open(inst_path) as inst_file:
            inst = inst_file.read()
            inst = [s for row in inst for s in row if s != '\n']  # flatten inst + remove return
            self.inst = inst

            self.visited = [[0 for col in row] for row in self.wh_map]
            self.visited[self.robot_pos.r][self.robot_pos.c] += 1

    
    def load_original_map(self, map_path):
        
        # Extract map 
        with open(map_path) as map_file:
            original_map = map_file.read().splitlines()

        self.original_map = [[s for s in row] for row in original_map]

        wh_map = []
        for row in self.original_map:
            new_row = []
            for tile in row: 
                if tile == '#': new_row += ['#', '#']
                if tile == 'O': new_row += ['[', ']']
                if tile == '.': new_row += ['.', '.']
                if tile == '@': new_row += ['@', '.']
            wh_map.append(new_row)
        
        self.wh_map = wh_map
        self.get_start_pos()
    
    def load_expanded_map(self, map_path):
        # Extract map 
        with open(map_path) as map_file:
            original_map = map_file.read().splitlines()

        self.wh_map = [[s for s in row] for row in original_map]
        self.get_start_pos()

    def get_start_pos(self):
        # get start position in wh_map
        self.start = [(row, col) for row in range(len(self.wh_map)) for col in range(len(self.wh_map[0])) if self.wh_map[row][col] == '@'][0]
        self.robot_pos = Coor(self.start)
    
    def show_wh_map(self):
        for r in self.wh_map:
            row = "".join(r)
            print(row)
    
    def show_visited(self):
        print("")
        for r_ind, row in enumerate(self.visited):
            new_row = ""
            for c_ind, col in enumerate(row):
                s = str(col)
                if len(s) == 1: 
                    s = "  " + s
                else: 
                    s = " " + s 

                if self.value(Coor((r_ind, c_ind))) == '#':
                    s = " ##"
                new_row = new_row + s    
            print(new_row)

    def value(self, coor):
        return self.wh_map[coor.r][coor.c]


    def move_robot(self, dir) -> bool:
        """
            Attempts to move the robot, returns True is successful, False if not
        """
        next_pos = self.robot_pos.next_pos(dir)
        next_pos_value = self.value(next_pos)
        
        can_move = False
        updates = []

        if next_pos_value == '#': 
            pass

        elif next_pos_value == '.': 
            can_move =  True

        elif next_pos_value == '[':
            can_move = self.move_box(next_pos, dir, updates)
        
        elif next_pos_value == ']':
            can_move = self.move_box(next_pos.offset(0,-1), dir, updates)  # box position is one to the left

        if can_move:            
            updates.append([next_pos.r, next_pos.c, '@'])
            updates.append([self.robot_pos.r, self.robot_pos.c, '.'])
            
            # dedupe but retain order - so that don't try to move a box more than once. 
            # (its a bit of a hack)
            deduped_updates = []
            for u in updates:
                if u not in deduped_updates:
                    deduped_updates.append(u)
            
            # Apply updates
            for u in deduped_updates:
                print(u)
                self.wh_map[u[0]][u[1]] = u[2]
            
            self.visited[self.robot_pos.r][self.robot_pos.c] += 1
            self.robot_pos = next_pos
            return True
        else:
            return False

    def move_box(self, box_pos, dir, updates):
        """
            Attempts to move a box, returns True is successful, False if not.
        """
    
        can_move = False

        if dir == '^':
            up_left = self.value(box_pos.offset(-1,0))
            up_right = self.value(box_pos.offset(-1,1))

            if up_left == '#' or up_right == '#': 
                can_move = False
            elif up_left == '.' and up_right == '.': 
                can_move = True
            elif up_left == ']' and up_right == '[':
                can_move = (self.move_box(box_pos.offset(-1,-1),dir, updates) and 
                                self.move_box(box_pos.offset(-1,1),dir, updates))
            elif up_left == ']':
                can_move = self.move_box(box_pos.offset(-1,-1) ,dir, updates)
            elif up_left == '[':
                can_move = self.move_box(box_pos.offset(-1,0), dir, updates)
            elif up_right == '[':
                can_move = self.move_box(box_pos.offset(-1,1) , dir, updates) 

            if can_move:
                updates.append([box_pos.r - 1, box_pos.c , '['])
                updates.append([box_pos.r - 1, box_pos.c + 1 , ']'])
                updates.append([box_pos.r , box_pos.c , '.'])
                updates.append([box_pos.r , box_pos.c + 1, '.'])
                
                return True
            else: 
                return False
            
        if dir == '>':
            right = self.value(box_pos.offset(0,2))
            
            if right == '#': 
                can_move = False
            elif right == '.': 
                can_move = True
            elif right == '[':
                can_move = self.move_box(box_pos.offset(0,2), dir, updates)

            if can_move:
                updates.append([box_pos.r, box_pos.c, '.'])
                updates.append([box_pos.r, box_pos.c + 1, '['])
                updates.append([box_pos.r, box_pos.c + 2, ']'])
                return True
            else: 
                return False

        if dir == 'v':
            down_left = self.value(box_pos.offset(1,0))
            down_right = self.value(box_pos.offset(1,1))

            if down_left == '#' or down_right == '#': 
                can_move = False
            elif down_left == '.' and down_right == '.': 
                can_move = True
            elif down_left == ']' and down_right == '[':
                can_move = (self.move_box(box_pos.offset(1,-1),dir, updates) and 
                                self.move_box(box_pos.offset(1,1),dir, updates))
            elif down_left == ']':
                can_move = self.move_box(box_pos.offset(1,-1) ,dir, updates)
            elif down_left == '[':
                can_move = self.move_box(box_pos.offset(1,0), dir, updates)
            elif down_right == '[':
                can_move = self.move_box(box_pos.offset(1,1) , dir, updates) 

            if can_move:
                updates.append([box_pos.r + 1, box_pos.c, '['])
                updates.append([box_pos.r + 1, box_pos.c + 1, ']'])
                updates.append([box_pos.r , box_pos.c, '.'])
                updates.append([box_pos.r , box_pos.c + 1, '.'])
                return True
            else: 
                return False

        if dir == '<':
            left = self.value(box_pos.offset(0,-1))
            
            if left == '#': 
                can_move = False
            elif left == '.': 
                can_move = True
            elif left == ']':
                can_move = self.move_box(box_pos.offset(0,-2), dir, updates)

            if can_move:
                updates.append([box_pos.r, box_pos.c + 1, '.'])
                updates.append([box_pos.r, box_pos.c, ']'])
                updates.append([box_pos.r, box_pos.c - 1, '['])
                return True
            else: 
                return False


    def execute_instructions(self):
        for i_ind, i in enumerate(self.inst):
            print(i)
            self.move_robot(i)
            self.show_wh_map()
        self.show_visited()


    def cal_gps(self):
        sum = 0 
        for r_ind, r in enumerate(self.wh_map):
            for c_ind, c in enumerate(r): 
                if c == '[':
                    sum += r_ind * 100 + c_ind
        return sum
    


class Coor:
        """
            Class for handling coordinates in the map
        """
    
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
        
        def __call__(self):
            return (self.r, self.c)