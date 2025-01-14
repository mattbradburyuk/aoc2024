# path_ins = "./day24/day24_test1_ins.txt"
# path_gates = "./day24/day24_test1_gates.txt"

# path_ins = "./day24/day24_test2_ins.txt"
# path_gates = "./day24/day24_test2_gates.txt"

path_ins = "./day24/day24_input_ins.txt"
path_gates = "./day24/day24_input_gates.txt"

with open(path_ins) as file_ins:
    ins_strs = file_ins.read().splitlines()


# list of wires which will be set in order
wires_to_set = []
for ins_str in ins_strs:
    wire = ins_str[:3]
    wire_value = int(ins_str[-1])
    wires_to_set.append([wire,wire_value])

# print(wires_to_set)  

with open(path_gates) as file_gates:
    gate_strs = file_gates.read().splitlines()

# Map of wires to the gates that they go in to
gates = {}
for gate_str in gate_strs:
    wire_1, op, wire_2, _ , wire_out = gate_str.split(' ')
    if wire_1 in gates:
        gates[wire_1].append((op, wire_2, wire_out))
    else:
        gates[wire_1] = [(op, wire_2, wire_out)]
    
    if wire_2 in gates:
        gates[wire_2].append((op, wire_1, wire_out))
    else:
        gates[wire_2] = [(op,wire_1, wire_out)]

# for g in gates:
#     print(f"{g} -> {gates[g]}")

# Calculates the gate ouput
def calc_gate(val_1, val_2, operation): 
    if operation == 'OR': return val_1 | val_2
    if operation == 'AND': return val_1 & val_2
    if operation == 'XOR': return val_1 ^ val_2

# set of wires that have been set (for easy look up)
set_wires = {}

# loops through applying the wires_to_be set in order
# where a Gates has both inputs set the gate is calculated and 
# the output wire is added to wire_to_set
wire_ind = 0
while wire_ind < len(wires_to_set):
    # print(f"ind: {wire_ind}")
    wire_name = wires_to_set[wire_ind][0]
    wire_value = wires_to_set[wire_ind][1]

    set_wires[wire_name] = wire_value
    
    if wire_name in gates:
        gates_to_update = gates[wire_name]
        
        for gtu in gates_to_update: 
            gate_op, gate_in_2, gate_out = gtu
            if gate_in_2 in set_wires:
                gate_val = calc_gate(wire_value, set_wires[gate_in_2], gate_op)
                wires_to_set.append([gate_out, gate_val])

    wire_ind += 1

# filter wires_set for the output wires
z_wires = {k:v for k, v in set_wires.items() if k[0] == 'z'}

# turn into a sorted list
z_wires_sorted = sorted(z_wires.items())

# calc number from bit position
result = 0 
for ind, z in enumerate(z_wires_sorted):
    result += z[1] * (2 ** ind)

print(result)






