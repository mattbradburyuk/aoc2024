

def dif_coor(start, end): return(end[0] - start[0], end[1] - start[1])

def door_coor(button):
    button_pad = '789456123X0A'
    ind = button_pad.find(button)
    return (ind // 3, ind % 3)

def controller_coor(button):
    button_pad = 'X^A<v>'
    ind = button_pad.find(button)
    return (ind // 3, ind % 3)

def sequencer(input_seq, coor_fun):
    """
        Takes a numeric sequence and ouputs required control movements for the door robot.
    """

    input_seq = 'A'+ input_seq    
    output_seq = ''

    for i in range(len(input_seq) - 1):

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

    return output_seq

def seq_complexity(seq): 
    radiation_seq = sequencer(seq, door_coor)
    # print(f"radiation_seq: {radiation_seq}")

    cold_seq = sequencer(radiation_seq, controller_coor)
    # print(f"cold_seq: {cold_seq}")
    
    my_seq = sequencer(cold_seq, controller_coor)
    # print(f"my_seq: {my_seq}")

    seq_num = int(seq[:3])
    seq_len = len(my_seq)
    print(f"seq: {seq}, seq_num: {seq_num}, seq_len: {seq_len}, product: {seq_len * seq_num}")
    return seq_len * seq_num

# codes = ['671A', '083A', '582A', '638A', '341A']
codes = ['029A', '980A', '179A', '456A', '379A']
# codes = ['379A']
# codes = ['179A']
sum = 0 

for c in codes: 
    sum += seq_complexity(c)

# print(sum)




# seq = '<>>A'
# res = sequencer(seq, controller_coor)
# print(f"{seq} : {res}, len: {len(res)}")




# print(f"7 : {sequencer('37',door_coor)}")
# print(f"9 : {sequencer('79',door_coor)}")
# print(f"A : {sequencer('9A',door_coor)}")


# print(f"^ : {sequencer('^',controller_coor)}")
# print(f"> : {sequencer('>',controller_coor)}")
# print(f"v : {sequencer('v',controller_coor)}")
# print(f"< : {sequencer('<',controller_coor)}")
# print(f"A : {sequencer('A',controller_coor)}")