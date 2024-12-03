import re

data = []

with open('input.txt', 'r') as f:
    data = f.readlines()

data = "".join(data)

sum = 0

should_do = True

for mch in re.finditer(r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)', data):
    cur_data = mch.group()

    if cur_data == 'do()':
        should_do = True
        continue

    if cur_data == 'don\'t()':
        should_do = False
        continue

    cur_data = cur_data.replace('mul(', '').replace(')', '')

    num_0, num_1 = cur_data.split(',')

    if should_do:
        sum += int(num_0) * int(num_1)

print(sum)
