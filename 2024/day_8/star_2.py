import itertools

data = []

with open('input.txt', 'r') as f:
    data = f.readlines()

tree = {}

data = [list(x.strip()) for x in data]

max_x = len(data[0])
max_y = len(data)


def is_within_bounds(pos):
    x, y = pos
    return (x >= 0 and x < max_x) and (y >= 0 and y < max_y)


for y_idx, line in enumerate(data):
    for x_idx, n in enumerate(line):
        if n != '.':
            if n not in tree:
                tree[n] = [(x_idx, y_idx)]
            else:
                tree[n].append((x_idx, y_idx))


def get_mirrors(pos1, pos2):
    if not is_within_bounds(pos1) or not is_within_bounds(pos2):
        return []

    x1, y1 = pos1
    x2, y2 = pos2

    if x1 == x2:
        diff = abs(y1 - y2)

        lst = [(x1, y1), (x2, y2)]
        while y1 + diff < max_y:
            lst.append((x1, y1 + diff))
            y1 += diff
        while y1 - diff >= 0:
            lst.append((x1, y1 - diff))
            y1 -= diff

        return lst

    if y1 == y2:
        diff = abs(x1 - x2)

        lst = [(x1, y1), (x2, y2)]
        while x1 + diff < max_x:
            lst.append((x1 + diff, y1))
            x1 += diff
        while x1 - diff >= 0:
            lst.append((x1 - diff, y1))
            x1 -= diff

        return lst

    diff_x = abs(x1 - x2)
    diff_y = abs(y1 - y2)
    if x1 < x2:
        if y1 < y2:
            lst = [(x1, y1), (x2, y2)]
            while x1 - diff_x >= 0 and y1 - diff_y >= 0:
                lst.append((x1 - diff_x, y1 - diff_y))
                x1 -= diff_x
                y1 -= diff_y
            while x2 + diff_x < max_x and y2 + diff_y < max_y:
                lst.append((x2 + diff_x, y2 + diff_y))
                x2 += diff_x
                y2 += diff_y

            return lst
        else:
            lst = [(x1, y1), (x2, y2)]
            while x1 - diff_x >= 0 and y1 + diff_y < max_y:
                lst.append((x1 - diff_x, y1 + diff_y))
                x1 -= diff_x
                y1 += diff_y
            while x2 + diff_x < max_x and y2 - diff_y >= 0:
                lst.append((x2 + diff_x, y2 - diff_y))
                x2 += diff_x
                y2 -= diff_y

            return lst
    else:
        if y1 < y2:
            lst = [(x1, y1), (x2, y2)]
            while x1 + diff_x < max_x and y1 - diff_y >= 0:
                lst.append((x1 + diff_x, y1 - diff_y))
                x1 += diff_x
                y1 -= diff_y
            while x2 - diff_x >= 0 and y2 + diff_y < max_y:
                lst.append((x2 - diff_x, y2 + diff_y))
                x2 -= diff_x
                y2 += diff_y

            return lst
        else:
            lst = [(x1, y1), (x2, y2)]
            while x1 + diff_x < max_x and y1 + diff_y < max_y:
                lst.append((x1 + diff_x, y1 + diff_y))
                x1 += diff_x
                y1 += diff_y
            while x2 - diff_x >= 0 and y2 - diff_y >= 0:
                lst.append((x2 - diff_x, y2 - diff_y))
                x2 -= diff_x
                y2 -= diff_y

            return lst


def get_antinodes(positions):
    antinodes = []
    pos_if_antinodes = []
    for comb in itertools.combinations(positions, 2):
        for pos in get_mirrors(comb[0], comb[1]):
            if is_within_bounds(pos):
                antinodes.append(pos)

    return antinodes + pos_if_antinodes


all_locs = set()

for value in tree.values():
    an = get_antinodes(value)
    all_locs.update(an)


print(len(all_locs))
