data = []

with open('input.txt', 'r') as f:
    data = f.readlines()

data = list(data[0].strip())

listt = []

is_mem = True
mem_idx = 0

for d in data:
    if is_mem:
        for i in range(int(d)):
            listt.append(mem_idx)
        mem_idx += 1
    else:
        for i in range(int(d)):
            listt.append(".")

    is_mem = not is_mem

idx_start = 0
idx_end = len(listt) - 1

while idx_start < idx_end:
    if listt[idx_start] != ".":
        idx_start += 1
        continue

    if listt[idx_end] == ".":
        idx_end -= 1
        continue

    listt[idx_start], listt[idx_end] = listt[idx_end], listt[idx_start]
    idx_start += 1
    idx_end -= 1

checksum = 0

for i in range(len(listt)):
    if listt[i] == ".":
        continue

    checksum += (i * listt[i])

print(checksum)
