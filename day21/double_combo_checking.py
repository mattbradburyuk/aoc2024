combos_double_map = {
    'AA': 'A',
    'A^': 'v<<A>>^A',
    'A>': 'v<A>^A',
    'Av': 'v<<A>A>^A',
    'A<': 'v<A<AA>>^A',
    '^A': 'vA^A',
    '^^': 'A',
    '^>': '<vA>A^A',
    '^v': 'v<A>^A',
    '^<': 'v<A<A>>^A',
    '>A': '<A>A',
    '>^': 'v<<A>^A>A',
    '>>': 'A',
    '>v': 'v<<A>>^A',
    '><': 'v<<AA>>^A',
    'vA': '<Av>A^A',
    'v^': '<A>A',
    'v>': 'vA^A',
    'vv': 'A',
    'v<': 'v<<A>>^A',
    '<A': 'vAA^<A>A',
    '<^': 'vA^<A>A',
    '<>': 'vAA^A',
    '<v': 'vA^A',
    '<<': 'A'
}

combos_map = {
    'AA': 'A', 
    'A^': '<A',
    'A>': 'vA',
    'Av': '<vA',
    'A<': 'v<<A',
    '^A': '>A',
    '^^': 'A',
    '^>': 'v>A',
    '^v': 'vA',
    '^<': 'v<A',
    '>A': '^A',
    '>^': '<^A',
    '>>': 'A',
    '>v': '<A',
    '><': '<<A',
    'vA': '>^A',
    'v^': '^A',
    'v>': '>A',
    'vv': 'A',
    'v<': '<A',
    '<A': '>>^A',
    '<^': '>^A',
    '<>': '>>A',
    '<v': '>A',
    '<<': 'A'
}


# check mappings

for seq in combos_map:
    output = ''
    for i in range(len(seq)-1):
        pair = seq[i:i+2]
        sub_seq =  'A' + combos_map[pair]
        for j in range(len(sub_seq)-1):
            sub_pair = sub_seq[j:j+2]
            output = output + combos_map[sub_pair]
    if output == combos_double_map[seq]: 
        print(f"{seq}, okay")
    else:
        print(f"{seq}, fail: \nclac: {output}\nlist: {combos_double_map[seq]}\n")