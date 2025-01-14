

# path = "./day23/day23_input.txt"
path = "./day23/day23_test.txt"

with open(path) as file:
    lines = file.read().splitlines()

pairs = []
for line in lines: 
    pairs.append([line[0:2], line[3:5]])
    pairs.append([line[3:5], line[0:2]])

file = None
line = None
lines = None

links = {}

for p in pairs:
    if p[0] in links:
        links[p[0]].add(p[1])
    else:
        links[p[0]] = {p[1]}


# start with list of 2 node parties begining with t

parties = [p for p in pairs if p[0][0] == 't']

p = None
pairs = None


ind = 0 

while ind < len(parties):

    if ind % 1000000 == 0:
        print(f"i: {ind}, len parties: {len(parties[-1])}")

    party = parties[ind]
    sets = []
    for comp in party:
        sets.append(links[comp])
    s = sets[0]
    intersects = sets[0].intersection(*sets[1:])

    for intersect in intersects:
        parties.append(party + [intersect])
    
    ind +=1

last_entry = parties[-1]
print(f"last_entry: {last_entry}")
last_entry.sort()
answer_string = ','.join(last_entry)
print(f"last_entry sorted: {last_entry}")
print(f"ans_string: {answer_string} ")


# pass      



