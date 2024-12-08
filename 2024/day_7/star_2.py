data = []

with open('input.txt', 'r') as f:
    data = f.readlines()


def find_valid_equation(check, num, numbers: list[int]):
    if len(numbers) == 0:
        if num == check:
            return True
        return False

    new_num = numbers.pop(0)

    sum = find_valid_equation(check, num + new_num, numbers.copy())
    mult = find_valid_equation(check, num * new_num, numbers.copy())
    joins = find_valid_equation(check, int(f"{num}{new_num}"), numbers.copy())

    return sum or mult or joins


sum_of_valid = 0

for line in data:
    line = line.strip()
    line = line.split(':')

    check_number = int(line[0].strip())
    line = [int(x) for x in line[1].strip().split(' ')]

    if find_valid_equation(check_number, 0, line):
        sum_of_valid += check_number

print(sum_of_valid)
