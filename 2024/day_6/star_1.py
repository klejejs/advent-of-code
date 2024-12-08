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


def count_x(data):
    count = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 'X':
                count += 1
    return count


dir_up = True
dir_right = False
dir_down = False
dir_left = False

while True:
    if dir_up:
        if guard_pos_x - 1 >= 0:
            if data[guard_pos_x - 1][guard_pos_y] == '#':
                dir_up = False
                dir_right = True
            elif is_valid_move(data[guard_pos_x - 1][guard_pos_y]):
                guard_pos_x -= 1
                data[guard_pos_x][guard_pos_y] = 'X'
        else:
            break
    elif dir_right:
        if guard_pos_y + 1 < len(data[0]):
            if data[guard_pos_x][guard_pos_y + 1] == '#':
                dir_right = False
                dir_down = True
            elif is_valid_move(data[guard_pos_x][guard_pos_y + 1]):
                guard_pos_y += 1
                data[guard_pos_x][guard_pos_y] = 'X'
        else:
            break
    elif dir_down:
        if guard_pos_x + 1 < len(data):
            if data[guard_pos_x + 1][guard_pos_y] == '#':
                dir_down = False
                dir_left = True
            elif is_valid_move(data[guard_pos_x + 1][guard_pos_y]):
                guard_pos_x += 1
                data[guard_pos_x][guard_pos_y] = 'X'
        else:
            break
    elif dir_left:
        if guard_pos_y - 1 >= 0:
            if data[guard_pos_x][guard_pos_y - 1] == '#':
                dir_left = False
                dir_up = True
            elif is_valid_move(data[guard_pos_x][guard_pos_y - 1]):
                guard_pos_y -= 1
                data[guard_pos_x][guard_pos_y] = 'X'
        else:
            break

print(count_x(data))
