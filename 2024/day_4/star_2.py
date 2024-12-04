data = []

with open('input.txt', 'r') as f:
    data = f.readlines()

data = [list(x.strip()) for x in data]


def is_a_mas_x(data, x, y):
    if data[y][x] != 'A':
        return False

    if x - 1 < 0 or x + 1 >= len(data[y]) or y - 1 < 0 or y + 1 >= len(data):
        return False

    if (
        (
            (data[y-1][x-1] == "M" and data[y+1][x+1] == "S") or
            data[y-1][x-1] == "S" and data[y+1][x+1] == "M"
        ) and
        (
            (data[y-1][x+1] == "M" and data[y+1][x-1] == "S") or
            data[y-1][x+1] == "S" and data[y+1][x-1] == "M")
    ):
        return True

    return False


global_count = 0

for y in range(len(data)):
    for x in range(len(data[y])):
        if is_a_mas_x(data, x, y):
            global_count += 1

print(global_count)
