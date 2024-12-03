import re

data = []

with open('input.txt', 'r') as f:
    data = f.readlines()

data = "".join(data)

sum = 0

for mch in re.finditer(r'mul\(\d{1,3},\d{1,3}\)', data):
    cur_data = mch.group()

    cur_data = cur_data.replace('mul(', '').replace(')', '')

    num_0, num_1 = cur_data.split(',')

    sum += int(num_0) * int(num_1)

print(sum)
