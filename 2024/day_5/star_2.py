data = []

with open('input.txt', 'r') as f:
    data = f.readlines()


page_map = {}
prints = []

while (line := data.pop(0)) != '\n':
    line = line.strip().split('|')

    if page_map.get(int(line[0])):
        page_map[int(line[0])].append(int(line[1]))
    else:
        page_map[int(line[0])] = [int(line[1])]

for line in data:
    prints.append([int(i) for i in line.strip().split(',')])


def is_print_in_correct_order(line):
    for item_before, list_only_after in page_map.items():
        if item_before in line:
            idx = line.index(item_before)
            for item_only_after in list_only_after:
                if item_only_after in line[:idx]:
                    return False
    return True


def get_print_middle_page(line):
    if len(line) == 1:
        return 0

    if len(line) % 2 == 0:
        return line[len(line) // 2 - 1]
    else:
        return line[len(line) // 2]


def fix_print_order(line):
    fixed_line = [line[0]]
    for item in line[1:]:
        for idx in range(len(fixed_line)):
            if fixed_line[idx] in page_map and item in page_map[fixed_line[idx]] and idx != len(fixed_line) - 1:
                continue
            else:
                if fixed_line[idx] in page_map and item in page_map[fixed_line[idx]] and idx == len(fixed_line) - 1:
                    fixed_line.append(item)
                else:
                    fixed_line.insert(idx, item)
                break

    return fixed_line


summ = 0

for line in prints:
    if not is_print_in_correct_order(line):
        fixed_line = fix_print_order(line)
        summ += get_print_middle_page(fixed_line)

print(summ)
