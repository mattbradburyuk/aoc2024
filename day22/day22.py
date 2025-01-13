
path = "./day22/day22_input.txt"

with open(path) as file:
    input_as_strs = file.read().splitlines()


nums = [int(s) for s in input_as_strs]

test_nums = [1,10,100,2024]

# print(nums)

def generate_next_number(num):

    temp_1 = num * 64
    num  = num ^ temp_1
    num = num % (2 ** 24)

    temp_2 = num // 32
    num = num ^ temp_2    
    num = num % (2 ** 24) 

    temp_3 = num * 2048
    num = num ^ temp_3
    num = num % (2 ** 24)

    return num

results = []


for ind, n in enumerate(nums):

    sn = n
    for i in range(2000):
        sn = generate_next_number(sn)
    results.append(sn)

print(sum(results))