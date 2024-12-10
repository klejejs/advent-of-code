data = []

with open('input.txt', 'r') as f:
    data = f.readlines()

data = [
    [int(cell) for cell in list(row.strip())]
    for row in data
]

summ = 0


directions = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]


def find_paths_from_trailhead(x, y, stepper):
    count = 0
    for direction in directions:
        new_x = x + direction[0]
        new_y = y + direction[1]

        if new_x < 0 or new_x >= len(data[0]) or new_y < 0 or new_y >= len(data):
            continue

        if data[new_y][new_x] == 9 and stepper == 8:
            count += 1
            continue

        if data[new_y][new_x] - 1 == stepper:
            count += find_paths_from_trailhead(new_x, new_y, stepper + 1)

    return count


for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == 0:
            paths = find_paths_from_trailhead(x, y, 0)
            summ += paths

print(summ)
