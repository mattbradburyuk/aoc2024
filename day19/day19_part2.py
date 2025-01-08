path_towels = "./day19/day19_input_towels.txt"
path_designs = "./day19/day19_input_designs.txt"

# path_towels = "./day19/day19_test_towels.txt"
# path_designs = "./day19/day19_test_designs.txt"

with open(path_towels) as towel_file:

    towels = set(towel_file.read().split(', '))

# print(towels)

with open(path_designs) as design_file:

    designs = design_file.read().splitlines()

# for d in designs:
#     print(d)

max_towel_len = len(max(towels, key = len))

count = 0 
for design in designs:

    combos = [0 for i in range(len(design))]

    for ind in range(len(design)):

        for off_set in range(1, max_towel_len + 1):
            
            start_ind = ind - off_set
            
            if start_ind == -1 :
                slice = design[:(ind + 1)]
                if slice in towels:
                    combos[ind] += 1
            elif combos[start_ind] > 0 and start_ind >= 0:  
                slice = design[start_ind + 1: ind + 1]
                if slice in towels: 
                    combos[ind] += combos[start_ind]

    num_combos = combos[len(combos)-1]
    print(f"count of possible designs for design {design}: {num_combos}")
    count += num_combos

print(f"total combos: {count}")