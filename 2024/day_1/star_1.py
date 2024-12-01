data = []

with open('input.txt', 'r') as f:
    data = f.readlines()

left = []
right = []

for line in data:
    d = line.split("   ")
    left.append(int(d[0].strip()))
    right.append(int(d[1].strip()))

left = sorted(left)
right = sorted(right)

summ = 0

for (i, j) in zip(left, right):
    if i > j:
        summ += (i - j)
    else:
        summ += (j - i)

print(summ)
