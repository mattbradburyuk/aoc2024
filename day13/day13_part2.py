import re

path = "./day13/day13_input.txt"
# path = "./day13/day13_test.txt"

with open(path) as file:
    instructions = file.read()


# print(instructions)

regex = r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)"
inst_list = re.findall(regex,instructions)
inst_list = [[int(num) for num in inst] for inst in inst_list]


def calc_AB(inst):
    ax, ay, bx, by, tx, ty = inst

    tx = tx + 10000000000000
    ty = ty + 10000000000000

    """
    Maths: rearrange simultanious equations

    eq_1: ax * A + bx * B = tx
    eq_2: ay * A + by * B = ty 
    
    multiple eq 1 by 'by':

    eq_3: by * ax * A + by * bx * B = by * tx
    
    multiple eq_2 by '-bx':
    
    eq_4: -bx * ay * A - bx * by * B = -bx * ty 
    
    add eq_3 ad eq_4: (B expression cancels out)

    A * ( by * ax - bx * ay) = by * tx - bx * ty

    rearrange

    A = (by * tx - bx * ty) / ( by * ax - bx * ay)

    Get B from eq_1

    B = (tx - ax * A)/ bx

    """

    A = (by * tx - bx * ty) / (by * ax - bx * ay)
    B = (tx - ax * A)/ bx

    if A % 1 == 0 and B % 1 == 0: 
        
        return A, B
    else: 
        return None, None

sum = 0
for inst in inst_list:
    A, B = calc_AB(inst)
    
    if A: 
        sum += 3 * A + B
        # print("sol")

print(sum)

