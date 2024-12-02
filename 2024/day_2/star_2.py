data = []

with open('input.txt', 'r') as f:
    data = f.readlines()

data = [[int(x) for x in line.split(' ')] for line in data]

safe = 0


def check_if_line_is_safe(line):
    is_increasing = line[-1] - line[2] > 0
    is_safe = True
    faulty_index = -1

    for i in range(1, len(line)):
        if line[i - 1] == line[i]:
            is_safe = False
            faulty_index = i
            break
        elif line[i - 1] > line[i] and is_increasing:
            is_safe = False
            faulty_index = i
            break
        elif line[i - 1] < line[i] and not is_increasing:
            is_safe = False
            faulty_index = i
            break

        if abs(line[i - 1] - line[i]) > 3:
            is_safe = False
            faulty_index = i
            break

    return is_safe, faulty_index


for line in data:
    is_safe, unsafe_idx = check_if_line_is_safe(line)

    if not is_safe:
        for idx in [unsafe_idx - 1, unsafe_idx]:
            line_a = line[:idx] + line[idx + 1:]
            is_safe, _ = check_if_line_is_safe(line_a)

            if is_safe:
                break

    if is_safe:
        safe += 1

print(safe)
