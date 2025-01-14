

path = "./day23/day23_input.txt"
# path = "./day23/day23_test.txt"

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

intersects = {}

print(f"len links: {len(links)}")
for l1 in links: 
    for l2 in links:
        if l1 != l2: 
            x = links[l1].union({l1})
            y = links[l2].union({l2})
            intersect = x.intersection(y)
            if len(intersect) > 12:
                intersect_list = list(intersect)
                intersect_list.sort()
                key = tuple(intersect_list)
                if key in intersects:
                    intersects[key] += 1
                else:
                    intersects[key] = 1


tup = max(intersects, key = intersects.get)

print(','.join(tup))



