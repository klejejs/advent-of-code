data = []

with open('input.txt', 'r') as f:
    data = f.readlines()

data = [[int(x) for x in line.split(' ')] for line in data]

safe = 0

for line in data:
    is_increasing = len(line) > 1 and line[0] < line[1]
    is_safe = True

    for i in range(1, len(line)):
        if line[i - 1] == line[i]:
            is_safe = False
            break
        elif line[i - 1] > line[i] and is_increasing:
            is_safe = False
            break
        elif line[i - 1] < line[i] and not is_increasing:
            is_safe = False
            break

        if abs(line[i - 1] - line[i]) > 3:
            is_safe = False
            break

    if is_safe:
        safe += 1

print(safe)
