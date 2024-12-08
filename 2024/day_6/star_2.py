import copy

data = []

with open('input.txt', 'r') as f:
    data = f.readlines()

data = [list(x.strip()) for x in data]


def find_guard(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == '^':
                return i, j


guard_pos_x, guard_pos_y = find_guard(data)
data[guard_pos_x][guard_pos_y] = 'X'


def is_valid_move(char):
    if char in ['.', 'X']:
        return True
    return False


def is_blocker(char):
    if char in ['#', 'O']:
        return True
    return False


def count_x(data):
    x_pos = []

    count = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 'X':
                count += 1
                x_pos.append((i, j))

    return count, x_pos


def find_path(local_data, gp_x, gp_y):
    dir_up = True
    dir_right = False
    dir_down = False
    dir_left = False

    tree = {}

    is_loop = False

    while True:
        if dir_up:
            if gp_x - 1 >= 0:
                if is_blocker(local_data[gp_x - 1][gp_y]):
                    dir_up = False
                    dir_right = True
                elif is_valid_move(local_data[gp_x - 1][gp_y]):
                    gp_x -= 1
                    if tree.get(f"{gp_x + 1}_{gp_y}_U"):
                        is_loop = True
                        break
                    tree[f"{gp_x + 1}_{gp_y}_U"] = f"{gp_x}_{gp_y}_U"
                    local_data[gp_x][gp_y] = 'X'
            else:
                break
        elif dir_right:
            if gp_y + 1 < len(local_data[0]):
                if is_blocker(local_data[gp_x][gp_y + 1]):
                    dir_right = False
                    dir_down = True
                elif is_valid_move(local_data[gp_x][gp_y + 1]):
                    gp_y += 1
                    if tree.get(f"{gp_x}_{gp_y - 1}_R"):
                        is_loop = True
                        break
                    tree[f"{gp_x}_{gp_y - 1}_R"] = f"{gp_x}_{gp_y}_R"
                    local_data[gp_x][gp_y] = 'X'
            else:
                break
        elif dir_down:
            if gp_x + 1 < len(local_data):
                if is_blocker(local_data[gp_x + 1][gp_y]):
                    dir_down = False
                    dir_left = True
                elif is_valid_move(local_data[gp_x + 1][gp_y]):
                    gp_x += 1
                    if tree.get(f"{gp_x - 1}_{gp_y}_D"):
                        is_loop = True
                        break
                    tree[f"{gp_x - 1}_{gp_y}_D"] = f"{gp_x}_{gp_y}_D"
                    local_data[gp_x][gp_y] = 'X'
            else:
                break
        elif dir_left:
            if gp_y - 1 >= 0:
                if is_blocker(local_data[gp_x][gp_y - 1]):
                    dir_left = False
                    dir_up = True
                elif is_valid_move(local_data[gp_x][gp_y - 1]):
                    gp_y -= 1
                    if tree.get(f"{gp_x}_{gp_y + 1}_L"):
                        is_loop = True
                        break
                    tree[f"{gp_x}_{gp_y + 1}_L"] = f"{gp_x}_{gp_y}_L"
                    local_data[gp_x][gp_y] = 'X'
            else:
                break

    return is_loop, local_data


new_data = copy.deepcopy(data)
a, datad = find_path(new_data, guard_pos_x, guard_pos_y)
count, x_pos = count_x(datad)
# print(a, count, x_pos)

loops = 0

for x in x_pos:
    new_data = copy.deepcopy(data)
    new_data[x[0]][x[1]] = 'O'
    a, datad = find_path(new_data, guard_pos_x, guard_pos_y)
    if a:
        loops += 1

print(loops)
