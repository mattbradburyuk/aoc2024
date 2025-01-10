"""
671A
083A
582A
638A
341A
"""

def dif_coor(start, end): return(end[0] - start[0], end[1] - start[1])

def door_coor(button):
    button_pad = '789456123X0A'
    ind = button_pad.find(button)
    return (ind // 3, ind % 3)

def controller_coor(button):
    button_pad = 'X^A<v>'
    ind = button_pad.find(button)
    return (ind // 3, ind % 3)

def sequencer(input_seq):
    """
        Takes a numeric sequence and ouputs required control movements for the door robot.
    """

    input_seq = 'A'+ input_seq    
    output_seq = ''

    for i in range(len(input_seq) - 1):

        start = door_coor(input_seq[i])
        end = door_coor(input_seq[i+1])

        dif = dif_coor(start, end)

        if dif[0] > 0: 
            output_seq = output_seq + 'v' * dif[0]
        if dif[0] < 0: 
            output_seq = output_seq + '^' * abs(dif[0])  
        if dif[1] > 0: 
            output_seq = output_seq + '>' * dif[1]
        if dif[1] < 0:
            output_seq = output_seq + '<' * abs(dif[1])
    
        output_seq = output_seq + 'A'

    return output_seq


print(sequencer('029A'))