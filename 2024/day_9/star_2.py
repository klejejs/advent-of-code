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

listt_groups = []
group = []
st = None
for i in range(len(listt)):
    if listt[i] == "." or (len(group) > 0 and listt[i] != group[0]):
        if len(group) > 0:
            group.insert(0, st)
            listt_groups.append(group)
        if listt[i] == ".":
            group = []
            st = None
        else:
            group = [listt[i]]
            st = i
        continue

    if st == None:
        st = i

    group.append(listt[i])

if len(group) > 0:
    group.insert(0, st)
    listt_groups.append(group)

listt_groups.reverse()

for group in listt_groups:
    len_dots = 0
    idx = 0
    group_start_idx = group.pop(0)
    while len_dots < len(group) and idx < group_start_idx:
        if listt[idx] == ".":
            len_dots += 1
        else:
            len_dots = 0
        idx += 1

    if len_dots == len(group):
        for i in range(len(listt)):
            if listt[i] == group[0]:
                listt[i] = "."

        for i in range(len(group)):
            listt[idx - len(group) + i] = group[i]


checksum = 0

for i in range(len(listt)):
    if listt[i] == ".":
        continue

    checksum += (i * listt[i])

print(checksum)
