
path = "./day22/day22_input.txt"

with open(path) as file:
    input_as_strs = file.read().splitlines()


nums = [int(s) for s in input_as_strs]

# test_nums = [1,2,3,2024]
# test_nums = [123]
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

seq_map = {}

iterations = 2000

for ind, n in enumerate(nums):

    difs = []
    buyer_map = {}
    sn = n
    price = sn % 10
    prices = [price]
    
    # generate difs and prices for this buyer
    for i in range(iterations):
        sn_new = generate_next_number(sn)
        price_new = sn_new % 10
        dif = price_new - price
        difs.append(dif)
        prices.append(price_new)
        sn = sn_new
        price = price_new

    # Put price for first occurance in map of difs -> price for this buyer
    for i in range(4, iterations):
        changes = tuple(difs[i-4:i])
        price = prices[i]
        if changes not in buyer_map:
            buyer_map[changes] = price
    
    # add prices on to cumulative prices for all buyers
    for key in buyer_map:
        if key in seq_map:
            seq_map[key] += buyer_map[key]
        else:
            seq_map[key] = buyer_map[key]
        
max_seq = max(seq_map, key=seq_map.get)
print(f"seq: {max_seq}, num of bananas: {seq_map[max_seq]}")
