path_gates = "./day24/day24_input_gates.txt"

with open(path_gates) as file_gates:
    gate_strs = file_gates.read().splitlines()

gates = [s for s in gate_strs if s[0] == 'x' ]
reverse_gates = [s for s in gate_strs if s[8] == 'x']


def swap_gates(gate_string):
    in_1, op, in_2, arrow , out = gate_string.split(' ')
    return f"{in_2} {op} {in_1} {arrow} {out}"

gates_2 = list(map(swap_gates, reverse_gates))

gates += gates_2

gates.sort()

for g in gates:
        print(g)