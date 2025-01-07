
# # Test
# reg_A = 729
# reg_B = 0
# reg_C = 0
# program = [0,1,5,4,3,0]

# # part 2 Test
# reg_A = 117440
# reg_B = 0
# reg_C = 0
# program = [0,3,5,4,3,0]


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

# part 1

# Input
reg_A = 44348299
reg_B = 0
reg_C = 0
program = [2,4,1,5,7,5,1,6,0,3,4,2,5,5,3,0]

part1_comp = Computer(reg_A, reg_B, reg_C, program)
part1_comp.run_program()
part1_comp.read_out()  #  out:  6,5,4,7,1,6,0,3,1 - part 1 correct
