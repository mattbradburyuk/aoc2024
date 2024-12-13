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
    # print(ax, ay, bx, by, tx, ty)
    
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

print(sum)