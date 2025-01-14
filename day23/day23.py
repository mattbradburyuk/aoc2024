

path = "./day23/day23_input.txt"
# path = "./day23/day23_test.txt"

with open(path) as file:
    lines = file.read().splitlines()

pairs = []
for line in lines: 
    pairs.append((line[0:2], line[3:5]))
    pairs.append((line[3:5], line[0:2]))

links = {}

for p in pairs:
    if p[0] in links:
        links[p[0]].append(p[1])
    else:
        links[p[0]] = [p[1]]

parties = set()

t_links = [link for link in links if link[0]== 't']

for key_1 in t_links:
    values_1 = links[key_1]
    for key_2 in values_1:
        values_2 = links[key_2]
        for key_3 in values_2:
            values_3 = links[key_3]
            if key_1 in values_3: 
                l = [key_1, key_2, key_3]
                l.sort()
                parties.add(tuple(l))
                pass



for p in parties: 
    print(p)

print(f"Number of parties: {len(parties)}")