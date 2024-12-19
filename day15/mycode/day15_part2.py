

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

    def value(self, coor):
        return self.wh_map[coor.r][coor.c]


    def move_robot(self, dir) -> bool:
        """
            Attempts to move the robot, returns True is successful, False if not
        """
        next_pos = self.robot_pos.next_pos(dir)
        next_pos_value = self.value(next_pos)
        
        can_move = False

        if next_pos_value == '#': 
            pass

        elif next_pos_value == '.': 
            can_move =  True

        elif next_pos_value == '[':
            can_move = self.move_box(next_pos, dir)
        
        elif next_pos_value == ']':
            can_move = self.move_box(next_pos.offset(0,-1), dir)  # box position is one to the left

        if can_move:
            self.wh_map[next_pos.r][next_pos.c] = '@'
            self.wh_map[self.robot_pos.r][self.robot_pos.c] = '.'
            return True
        else:
            return False

    def move_box(self, box_pos, dir):
        """
            Attempts to move a box, returns True is successful, False if not.
        """
    
        can_move = False

        if dir == '^':
            up_left = box_pos.offset(-1,0).value()
            up_right = box_pos.offset(-1,1).value()

            if up_left == '#' or up_right == '#': 
                can_move == False
            elif up_left == '.' and up_right == '.': 
                can_move = True
            elif up_left == ']' and up_right == '[':
                can_move = (self.move_box(box_pos.offset(-1,-1),dir) and 
                                self.move_box(box_pos.offset(-1,1),dir))
            elif up_left == ']':
                can_move = self.move_box(box_pos.offset(-1,-1) ,dir)
            elif up_left == '[':
                can_move = self.move_box(box_pos.offset(-1,0), dir)
            elif up_right == '[':
                can_move = self.move_box(box_pos.offset(-1,1) , dir) 

            if can_move:
                self.wh_map[box_pos.r - 1][box_pos.c] = '['
                self.wh_map[box_pos.r -1][box_pos.c + 1] = ']'
                self.wh_map[box_pos.r][box_pos.c] = '.'
                self.wh_map[box_pos.r][box_pos.c + 1] = '.'
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
                can_move = self.move_box(box_pos.offset(0,2), dir)

            if can_move:
                self.wh_map[box_pos.r][box_pos.c] = '.'
                self.wh_map[box_pos.r][box_pos.c + 1] = '['
                self.wh_map[box_pos.r][box_pos.c + 2] = ']'
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
                can_move = (self.move_box(box_pos.offset(1,-1),dir) and 
                                self.move_box(box_pos.offset(1,1),dir))
            elif down_left == ']':
                can_move = self.move_box(box_pos.offset(1,-1) ,dir)
            elif down_left == '[':
                can_move = self.move_box(box_pos.offset(1,0), dir)
            elif down_right == '[':
                can_move = self.move_box(box_pos.offset(1,1) , dir) 

            if can_move:
                self.wh_map[box_pos.r + 1][box_pos.c] = '['
                self.wh_map[box_pos.r + 1][box_pos.c + 1] = ']'
                self.wh_map[box_pos.r][box_pos.c] = '.'
                self.wh_map[box_pos.r][box_pos.c + 1] = '.'
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
                can_move = self.move_box(box_pos.offset(0,-2), dir)

            if can_move:
                self.wh_map[box_pos.r][box_pos.c + 1] = '.'
                self.wh_map[box_pos.r][box_pos.c ] = ']'
                self.wh_map[box_pos.r][box_pos.c -1 ] = '['
                return True
            else: 
                return False

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