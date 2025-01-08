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

    combos = {}

    for ind in range(len(design)):

        for off_set in range(1, max_towel_len + 1):
            
            start_ind = ind - off_set
            
            if start_ind < 0:
                slice = design[:(ind + 1)]
                if slice in towels:
                    combos[ind] = [slice]
                    break
            
            elif start_ind in combos and start_ind >= 0:  
                slice = design[start_ind + 1: ind + 1]
                if slice in towels: 
                    combos[ind] = combos[ind - off_set] + [slice]
                    break

    if len(design)-1 in combos:
        count += 1

    # if len(design)-1 in combos:
    #     print(f"design {design} possilble")
    # else:
    #     print(f"design {design} not possilble")
    
print(f"count of possible designs: {count}")


print()

# for c in combos:
#     print(c)    