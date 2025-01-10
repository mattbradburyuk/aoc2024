
# Workout length after number of rounds

combos_map = {
    'AA': 'A', 
    'A^': '<A',
    'A>': 'vA',
    'Av': '<vA', 
    'A<': 'v<<A', 
    '^A': '>A',
    '^^': 'A',
    '^>': 'v>A', 
    '^v': 'vA',
    '^<': 'v<A', #
    '>A': '^A',
    '>^': '<^A', 
    '>>': 'A',
    '>v': '<A',
    '><': '<<A',
    'vA': '^>A', 
    'v^': '^A',
    'v>': '>A',
    'vv': 'A',
    'v<': '<A',
    '<A': '>>^A',
    '<^': '>^A',
    '<>': '>>A',
    '<v': '>A',
    '<<': 'A'
}

tally = {
    'AA': 0, 'A^': 0, 'A>': 0, 'Av': 0, 'A<': 0,
    '^A': 0, '^^': 0, '^>': 0, '^v': 0, '^<': 0,
    '>A': 0, '>^': 0, '>>': 0, '>v': 0, '><': 0,
    'vA': 0, 'v^': 0, 'v>': 0, 'vv': 0, 'v<': 0,
    '<A': 0, '<^': 0, '<>': 0, '<v': 0, '<<': 0
}

staging = {
    'AA': 0, 'A^': 0, 'A>': 0, 'Av': 0, 'A<': 0,
    '^A': 0, '^^': 0, '^>': 0, '^v': 0, '^<': 0,
    '>A': 0, '>^': 0, '>>': 0, '>v': 0, '><': 0,
    'vA': 0, 'v^': 0, 'v>': 0, 'vv': 0, 'v<': 0,
    '<A': 0, '<^': 0, '<>': 0, '<v': 0, '<<': 0
}

def show_staging():
    print("staging:")
    for ind, key in enumerate(staging):
        print(f"{key}: {staging[key]}",end="\t")
        if ind % 5 == 4 : print("")

def show_tally():
    print("tally:")
    for ind, key in enumerate(tally):
        print(f"{key}: {tally[key]}", end="\t")
        if ind % 5 == 4 : print("")

def length_after_rounds(seq, rounds):
    
    for key in tally: tally[key] = 0
    for key in staging: staging[key] = 0 

    seq = 'A' + seq
    for i in range(len(seq) -1):
        pair = seq[i:i+2]
        tally[pair] += 1

    for round in range(rounds):
        for key in tally:
            seq = combos_map[key]
            seq = 'A' + seq
            for i in range(len(seq)-1):
                pair = seq[i:i+2]
                staging[pair] += tally[key]

        for key in tally:
            tally[key] = staging[key]
            staging[key] = 0

    return sum(tally.values())

# get instructions for door code (minimising length after 2 rounds)

def dif_coor(start, end): return(end[0] - start[0], end[1] - start[1])
def add_coor(start, end): return(end[0] + start[0], end[1] + start[1])

def door_coor(button):
    button_pad = '789456123X0A'
    ind = button_pad.find(button)
    return (ind // 3, ind % 3)

def door_checker(seqs):
    
    door_grid = [[7,8,9],[4,5,6],[1,2,3],['X',0,'A']]
    legal_seqs = []
    start_pos = (3,2)
    for seq in seqs:
        okay = True
        pos = start_pos
        for s in seq:
            if s == '^': pos = add_coor(pos,(-1,0))
            if s == '>': pos = add_coor(pos,(0,1))
            if s == 'v': pos = add_coor(pos,(1,0))
            if s == '<': pos = add_coor(pos,(0,-1))
            if door_grid[pos[0]][pos[1]] == 'X': 
                okay = False
                # print(f"seq: {seq}, rejected for illegal door move")
        if okay: 
            legal_seqs.append(seq)
    
    return legal_seqs

# generates permutations of a string of characters
def permutations(seq): 
    perms = set()
    if len(seq) == 1: return [seq]
    else:
        for ind,s in enumerate(seq):
            remainder = seq[:ind] + seq[ind+1:]
            x = permutations(remainder)
            for p in x:
                perms.add(s + p)

    # return sorted(perms)
    return perms

# strips of the last A , generates permutations and puts the last A back on. 
def perms_with_A(seq):

    if seq == 'A': return seq

    seq_no_a = seq[:-1]
    perms_no_a = permutations(seq_no_a)

    perms =[]
    for pna in perms_no_a:
        perms.append(pna + 'A') 

    return perms

def door_sequencer(input_seq):
    """
        Takes the required door code and works out an instruction sequence, checking it 
        gives the shortest instruction sequence after 5 robot rounds
    """

    # generate possible output sequences
    output_seqs = []
    input_seq = 'A'+ input_seq  
    for i in range(len(input_seq) - 1):
    
        output_seq = ''

        start = door_coor(input_seq[i])
        end = door_coor(input_seq[i+1])
        dif = dif_coor(start, end)

          
        if dif[1] > 0: 
            output_seq = output_seq + '>' * dif[1]  
        if dif[0] < 0: 
            output_seq = output_seq + '^' * abs(dif[0])
        if dif[0] > 0: 
            output_seq = output_seq + 'v' * dif[0]
        if dif[1] < 0:
            output_seq = output_seq + '<' * abs(dif[1])     
    
        output_seq = output_seq + 'A'

        perms = perms_with_A(output_seq)

        if not output_seqs: 
            output_seqs = perms
        else:
            new_output_seqs = []
            for oss in output_seqs:
                for p in perms: 
                    new_output_seqs.append(oss+p)
            output_seqs = new_output_seqs

    # remove any illegal moves

    output_seqs = door_checker(output_seqs)

    for s in output_seqs:
        print(f"seq: {s}, 1 round: {length_after_rounds(s,1)}, 2 rounds: {length_after_rounds(s,2)}, 3 rounds: {length_after_rounds(s,3)}")

    return min(output_seqs, key= lambda k: length_after_rounds(k,25))

def controller_coor(button):
    button_pad = 'X^A<v>'
    ind = button_pad.find(button)
    return (ind // 3, ind % 3)

def controller_checker(seqs, start_char):
    controller_grid = [['X','^','A'],['<','v','>']]
    legal_seqs = []
    for seq in seqs:
        okay = True
        pos = [(r,c) for r in range(2) for c in range(3) if controller_grid[r][c] == start_char][0]
        for s in seq:
            if s == '^': pos = add_coor(pos,(-1,0))
            if s == '>': pos = add_coor(pos,(0,1))
            if s == 'v': pos = add_coor(pos,(1,0))
            if s == '<': pos = add_coor(pos,(0,-1))
            if controller_grid[pos[0]][pos[1]] == 'X': 
                okay = False
                # print(f"seq: {seq}, rejected for illegal controller move")
        if okay: 
            legal_seqs.append(seq)
    
    return legal_seqs

# does not assume starting at 'A' position
def controller_sequencer(input_seq):

    output_seqs = []
    for i in range(len(input_seq) - 1):
        output_seq = ''
        start = controller_coor(input_seq[i])
        end = controller_coor(input_seq[i+1])
        dif = dif_coor(start, end)

        if dif[1] > 0: 
            output_seq = output_seq + '>' * dif[1] 
        if dif[0] < 0: 
            output_seq = output_seq + '^' * abs(dif[0])     
        if dif[0] > 0: 
            output_seq = output_seq + 'v' * dif[0]
        if dif[1] < 0:
            output_seq = output_seq + '<' * abs(dif[1])

        output_seq = output_seq + 'A'
        perms = perms_with_A(output_seq)

        if not output_seqs: 
            output_seqs = perms
        else:
            new_output_seqs = []
            for oss in output_seqs:
                for p in perms: 
                    new_output_seqs.append(oss+p)
            output_seqs = new_output_seqs
        
        # remove any illegal moves
        output_seqs = controller_checker(output_seqs, input_seq[0])

        return output_seqs


# checking to make sure maps are legal
# for key in combos_map:
#     print(f"{key}: {controller_sequencer(key)}")
#     if combos_map[key] not in controller_sequencer(key): print("error")




# codes = ['029A', '980A', '179A', '456A', '379A']
codes = ['671A', '083A', '582A', '638A', '341A']
# codes = ['179A']
# codes = ['379A']

total_sum = 0

for c in codes:     
    print(f"\ncode: {c}")
    #reset maps
    for key in tally: tally[key] = 0
    for key in staging: staging[key] = 0   

    seq = door_sequencer(c)
    
    code_sum = length_after_rounds(seq, 25)

    print(int(c[:-1]))
    total_sum += int(c[:-1]) * code_sum
    print(f"code: {c}, seq: {seq}, total in tally: {code_sum}")

print(f" total sum: {total_sum}")

# seq = '^>A'
# print(f"{seq}: {length_after_rounds(seq, 4)}")
# seq = '>^A'
# print(f"{seq}: {length_after_rounds(seq, 4)}")