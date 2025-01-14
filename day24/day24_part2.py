# builds up the adders units one at a time and makes sure it can find the gates it needs, if it can't it 
# indicates a mis-wiring.
# Then go back an adder and start mapping out the expected connects, then see where they don't match the actual ones.
# Then, put a correction into the list of gates and re run. 
# Repeat until all corrections found and it runs till the end.

path_gates = "./day24/day24_input_gates.txt"

with open(path_gates) as file_gates:
    gate_strs = file_gates.read().splitlines()

class Gate():
    def __init__(self, gate_str):
        self.in_1, self.op, self.in_2, _, self.out = gate_str.split(' ')

def rev_gate_string(gate_str):
    in_1, op, in_2, _ , out = gate_str.split(' ')
    return f"{in_2} {op} {in_1} -> {out}"

gates = []
for gate_str in gate_strs:
    gates.append(Gate(gate_str))
    gates.append(Gate(rev_gate_string(gate_str)))


class Adder():

    def __init__(self, gates, xn, yn, c_prev):
        self.gates = gates
        self.n = xn[1:]
        self.xn = xn
        self.yn = yn
        self.c_prev = c_prev
        self.w1 = self.get_w1()
        self.w2 = self.get_w2()
        self.zn = self.get_zn()
        self.w3 = self.get_w3()
        self.cn = self.get_cn()

    def get_w1(self):
        gate = [g for g in gates if g.in_1 == self.xn and g.op == 'XOR' and g.in_2 == self.yn]
        if gate:
            return gate[0].out
        else:
            print(f"error: missing {self.xn} XOR {self.yn} -> ??")
            return None
    
    def get_w2(self):
        gate = [g for g in gates if g.in_1 == self.xn and g.op == 'AND' and g.in_2 == self.yn]
        if gate:
            return gate[0].out
        else:
            print(f"error: missing {self.xn} XOR {self.yn} -> ??")
            return None
    
    def get_zn(self):
        gate = [g for g in gates if g.in_1 == self.c_prev and g.op == 'XOR' and g.in_2 == self.w1]
        if gate:
            return gate[0].out
        else:
            print(f"error: missing {self.c_prev} XOR {self.w1} -> z{self.n:02}")
            return None
    
    def get_w3(self):
        gate = [g for g in gates if g.in_1 == self.c_prev and g.op == 'AND' and g.in_2 == self.w1]
        if gate:
            return gate[0].out
        else:
            print(f"error: missing {self.c_prev} XOR {self.w1} -> ??")
            return None

    def get_cn(self):
        gate = [g for g in gates if g.in_1 == self.w2 and g.op == 'OR' and g.in_2 == self.w3]
        if gate:
            return gate[0].out
        else:
            print(f"error: missing {self.w2} XOR {self.w3} -> ??")
            return None

def correct_gate(gate_str, new_out):
    in_1, op, in_2, _, old_out = gate_str.split(' ') 
    gate_ind = [i for i, gate in enumerate(gates) if gate.in_1 == in_1 and gate.op == op and gate.in_2 == in_2 and gate.out == old_out][0]
    del gates[gate_ind]
    rev_gate_ind = [i for i, gate in enumerate(gates) if gate.in_1 == in_2 and gate.op == op and gate.in_2 == in_1 and gate.out == old_out][0]
    del gates[rev_gate_ind]
    gates.append(Gate(f"{in_1} {op} {in_2} -> {new_out}"))
    gates.append(Gate(f"{in_2} {op} {in_1} -> {new_out}"))


correct_gate('vkd XOR scp -> fhc', 'z06')
correct_gate('vsv OR jnt -> z06', 'fhc')
correct_gate('rmd XOR nmm -> qhj', 'z11')
correct_gate('rmd AND nmm -> z11', 'qhj')
correct_gate('y23 XOR x23 -> mwh', 'ggt')
correct_gate('y23 AND x23 -> ggt', 'mwh')
correct_gate('kwj XOR bhv -> hqk', 'z35')
correct_gate('y35 AND x35 -> z35', 'hqk')


carry = 'rdm'
adders = ['x']
for a in range(1,45):
    adder = Adder(gates, f"x{a:02}", f"y{a:02}", carry)
    carry = adder.cn
    adders.append(adder)

pass

swapped_gates = ['z06', 'fhc', 'z11', 'qhj', 'ggt', 'mwh', 'z35', 'hqk']

swapped_gates.sort()

ans = ','.join(swapped_gates)

print(ans)