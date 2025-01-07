

# Input
program = [2,4,1,5,7,5,1,6,0,3,4,2,5,5,3,0]

class Computer():

    def __init__(self, reg_A, reg_B, reg_C, program):
        self.reg_A = reg_A
        self.reg_B = reg_B
        self.reg_C = reg_C
        self.program = program
        self.prog_ind = 0
        self.out = []

    def combo(self, lit_op):
        if lit_op in range(4):
            return lit_op
        elif lit_op == 4: return self.reg_A
        elif lit_op == 5: return self.reg_B
        elif lit_op == 6: return self.reg_C
        else: print("invalid combo operand")

    def adv_0(self, lit_op):
        num = self.reg_A
        den = (2 ** self.combo(lit_op))
        self.reg_A = num // den
        self.prog_ind += 2
        
    def bxl_1(self, lit_op):
        ans = self.reg_B ^ lit_op
        self.reg_B = ans
        self.prog_ind += 2

    def bst_2(self, lit_op):
        self.reg_B = self.combo(lit_op) % 8
        self.prog_ind += 2

    def jnz_3(self, lit_op):
        if self.reg_A > 0: 
            self.prog_ind = lit_op
        else: 
            self.prog_ind += 2

    def bxc_4(self, lit_op):
        self.reg_B = self.reg_B ^ self.reg_C
        self.prog_ind += 2

    def out_5(self, lit_op):
        ans = self.combo(lit_op) % 8
        self.out.append(ans)
        self.prog_ind += 2

    def bdv_6(self, lit_op):
        num = self.reg_A
        den = (2 ** self.combo(lit_op))
        self.reg_B = num // den
        self.prog_ind += 2

    def cdv_7(self, lit_op):
        num = self.reg_A
        den = (2 ** self.combo(lit_op))
        self.reg_C = num // den
        self.prog_ind += 2

    def run_program(self): 
        program = self.program

    
        while self.prog_ind <  len(program): 
            if program[self.prog_ind] == 0: fun = self.adv_0
            elif program[self.prog_ind] == 1: fun = self.bxl_1
            elif program[self.prog_ind] == 2: fun = self.bst_2
            elif program[self.prog_ind] == 3: fun = self.jnz_3
            elif program[self.prog_ind] == 4: fun = self.bxc_4
            elif program[self.prog_ind] == 5: fun = self.out_5
            elif program[self.prog_ind] == 6: fun = self.bdv_6
            elif program[self.prog_ind] == 7: fun = self.cdv_7
            else: 
                print("unrecognised op_code: , program[i]")

            fun(program[self.prog_ind + 1])

    def read_out(self): 
        out = ','.join(map(str,self.out))
        print("out: ", out)



reg_A = 106086382266778
program = [2,4,1,5,7,5,1,6,0,3,4,2,5,5,3,0]
print(program)
op_test = Computer(reg_A,0,0,program)
op_test.run_program()
op_test.read_out()

# reg_A = 16308406516322
# program = [2,4,1,5,7,5,1,6,0,3,4,2,5,5,3,0]
# op_test = Computer(reg_A,0,0,program)
# op_test.run_program()
# op_test.read_out()



# print("reg_A: ", op_test.reg_A)
# print("reg_B: ", op_test.reg_B)
# print("reg_C: ", op_test.reg_C)

# reg_A = 117440
# program = [0,3,5,4,3,0]
# op_test2 = Computer(reg_A,0,0,program)
# op_test2.run_program()
# op_test2.read_out()
# print(program)



# attempt 1

# def cal_base(results):
#     rev_results = results[::-1]
#     base = 0
#     for ind, r in enumerate(rev_results):
#         base += r * (8 ** (ind +1))
#     return base

# print(cal_base([]))

# rev_prog = program[::-1]
# results = []

# for ind, rp in enumerate(rev_prog):

#     base = cal_base(results)

#     for j in range(8**4): 
#         reg_A = base + j
#         comp = Computer(reg_A,0,0,program)
#         comp.run_program()
#         if comp.out[0] == rp:
#             results.append(j)
#             print(f"comp.out: {comp.out}")
#             break



# Attempt 2 - don't need to store base as Octs, just use a running total and x8 each time to shift over

# rev_prog = program[::-1]
# base = 0 

# for ind, rp in enumerate(rev_prog):

#     base = base * 8

#     for j in range(8**8): 
#         reg_A = base + j
#         comp = Computer(reg_A,0,0,program)
#         comp.run_program()
#         if comp.out[0] == rp:
#             base += j
#             print(f"j: {j}")
#             print(f"program:  {program[-(ind+1):]}")
#             print(f"comp.out: {comp.out}")
#             break


# Attempt 3 - need to compare more than last out, as they sometimes inteferwith previous numbers

rev_prog = program[::-1]
base = 0 

for ind, rp in enumerate(rev_prog):
    print(f"rp: {rp}")
    base = base * 8

    for j in range(8**8):       # arbitrary large number
        reg_A = base + j
        comp = Computer(reg_A,0,0,program)
        comp.run_program()
        if comp.out == program[-(ind+1):]:
            base += j
            print(f"j: {j}")
            print(f"program:  {program[-(ind+1):]}")
            print(f"comp.out: {comp.out}")
            print(f"reg_A: {reg_A}")
            break

print()

# test answer

reg_A = 106086382266778
program = [2,4,1,5,7,5,1,6,0,3,4,2,5,5,3,0]
print(program)
op_test = Computer(reg_A,0,0,program)
op_test.run_program()
op_test.read_out()