data = []

with open('input.txt', 'r') as f:
    data = f.readlines()

data = [list(x.strip()) for x in data]


def xmas_count_at_index(data, x, y):
    count = 0

    if data[y][x] != "X":
        return count

    # right
    if len(data[y]) - x - 4 >= 0 and "".join(data[y][x:x+4]) == "XMAS":
        count += 1

    # right down
    if len(data[y]) - x - 4 >= 0 and len(data) - y - 4 >= 0 and "".join([data[y+i][x+i] for i in range(4)]) == "XMAS":
        count += 1

    # down
    if len(data) - y - 4 >= 0 and "".join([data[y+i][x] for i in range(4)]) == "XMAS":
        count += 1

    # left down
    if x - 3 >= 0 and len(data) - y - 4 >= 0 and "".join([data[y+i][x-i] for i in range(4)]) == "XMAS":
        count += 1

    # left
    if x - 3 >= 0 and "".join(data[y][x-3:x+1]) == "SAMX":  # XMAS reversed
        count += 1

    # left up
    if x - 3 >= 0 and y - 3 >= 0 and "".join([data[y-i][x-i] for i in range(4)]) == "XMAS":
        count += 1

    # up
    if y - 3 >= 0 and "".join([data[y-i][x] for i in range(4)]) == "XMAS":
        count += 1

    # right up
    if len(data[y]) - x - 4 >= 0 and y - 3 >= 0 and "".join([data[y-i][x+i] for i in range(4)]) == "XMAS":
        count += 1

    return count


global_count = 0

for y in range(len(data)):
    for x in range(len(data[y])):
        global_count += xmas_count_at_index(data, x, y)

print(global_count)
