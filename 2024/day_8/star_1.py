import itertools

data = []

with open('input.txt', 'r') as f:
    data = f.readlines()

tree = {}

data = [list(x.strip()) for x in data]

max_x = len(data[0])
max_y = len(data)

for y_idx, line in enumerate(data):
    for x_idx, n in enumerate(line):
        if n != '.':
            if n not in tree:
                tree[n] = [(x_idx, y_idx)]
            else:
                tree[n].append((x_idx, y_idx))


def get_mirrors(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2

    if x1 == x2:
        diff = abs(y1 - y2)
        return [(x1, y1 + diff), (x2, y2 - diff)]

    if y1 == y2:
        diff = abs(x1 - x2)
        return [(x1 + diff, y1), (x2 - diff, y2)]

    diff_x = abs(x1 - x2)
    diff_y = abs(y1 - y2)
    if x1 < x2:
        if y1 < y2:
            return [(x1 - diff_x, y1 - diff_y), (x2 + diff_x, y2 + diff_y)]
        else:
            return [(x1 - diff_x, y1 + diff_y), (x2 + diff_x, y2 - diff_y)]
    else:
        if y1 < y2:
            return [(x1 + diff_x, y1 - diff_y), (x2 - diff_x, y2 + diff_y)]
        else:
            return [(x1 + diff_x, y1 + diff_y), (x2 - diff_x, y2 - diff_y)]


def get_antinodes(positions):
    antinodes = []
    for comb in itertools.combinations(positions, 2):
        for pos in get_mirrors(comb[0], comb[1]):
            if (pos[0] >= 0 and pos[0] < max_x) and (pos[1] >= 0 and pos[1] < max_y):
                antinodes.append(pos)

    return antinodes


all_locs = set()

for value in tree.values():
    an = get_antinodes(value)
    all_locs.update(an)


print(len(all_locs))
