data = []

with open('input.txt', 'r') as f:
    data = f.readlines()

left = []
right = []

for line in data:
    d = line.split("   ")
    left.append(int(d[0].strip()))
    right.append(int(d[1].strip()))

right_appearances = {}

for i in right:
    if i in right_appearances:
        right_appearances[i] += 1
    else:
        right_appearances[i] = 1

summ = 0

for i in left:
    if i in right_appearances:
        summ += (i * right_appearances[i])

print(summ)
