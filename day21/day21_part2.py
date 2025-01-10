import time

def dif_coor(start, end): return(end[0] - start[0], end[1] - start[1])

def add_coor(start, end): return(end[0] + start[0], end[1] + start[1])

def door_coor(button):
    button_pad = '789456123X0A'
    ind = button_pad.find(button)
    return (ind // 3, ind % 3)

def controller_coor(button):
    button_pad = 'X^A<v>'
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
    # return seqs

def controller_checker(seqs):
    controller_grid = [['X','^','A'],['<','v','>']]
    legal_seqs = []
    start_pos = (0,2)
    for seq in seqs:
        okay = True
        pos = start_pos
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
    # return seqs


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


def sequencer(input_seq, coor_fun, checker_fun):
    """
        Takes required actions sequences and ouputs the lists of required control movements.
    """

    # generate possible output sequences
    output_seqs = []
    input_seq = 'A'+ input_seq  
    for i in range(len(input_seq) - 1):
        
        output_seq = ''

        start = coor_fun(input_seq[i])
        end = coor_fun(input_seq[i+1])

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

    output_seqs = checker_fun(output_seqs)

    return output_seqs

def seq_complexity(seq): 
    
    radiation_seqs = sequencer(seq, door_coor, door_checker)
    print("radiation_seqs:")
    for rs in radiation_seqs: print(rs) 

    print(f"radiation_seqs len: {len(radiation_seqs)}")
    print(f"radiation_seqs min len: {len(min(radiation_seqs, key=len))}")
    print(f"radiation_seqs max len: {len(max(radiation_seqs, key=len))}")

    cold_seqs = []
    for rs in radiation_seqs:
        cold_seqs += sequencer(rs, controller_coor, controller_checker)

    # print("cold_seq:")
    # for cs in cold_seqs: print(cs)
    print(f"cold_seqs len: {len(cold_seqs)}")
    print(f"cold_seq min len: {len(min(cold_seqs, key=len))}")
    print(f"cold_seq max len: {len(max(cold_seqs, key=len))}")

    my_seqs = []
    for cs in cold_seqs:
        my_seqs += sequencer(cs, controller_coor, controller_checker)
        print(f"cs len: {len(cs)}, my_seq min len: {len(min(my_seqs, key=len))}, my_seq max len: {len(max(my_seqs, key=len))}")
    
    # print("my_seqs:")
    # for ms in my_seqs: print(ms)

    # print(f"my_seqs len: {len(my_seqs)}")
    # print(f"my_seq min len: {len(min(my_seqs, key=len))}")
    # print(f"my_seq max len: {len(max(my_seqs, key=len))}")
    # print(len(my_seqs))    



    seq_num = int(seq[:3])
    seq_len = len(min(my_seqs, key=len))
    print(f"seq: {seq}, seq_num: {seq_num}, seq_len: {seq_len}, product: {seq_len * seq_num}")
    
    return seq_len * seq_num

# codes = ['671A', '083A', '582A', '638A', '341A']
# codes = ['029A', '980A', '179A', '456A', '379A']
codes = ['379A']
# codes = ['179A']
sum = 0 

# for c in codes: 
#     tic = time.time()
#     print(f"code: {c}")
#     sum += seq_complexity(c)
#     toc = time.time()
#     print(f"time taken: {toc - tic}")

# print(f"sum: {sum}")

s = 'A^'
print(sequencer(s, controller_coor, controller_checker))