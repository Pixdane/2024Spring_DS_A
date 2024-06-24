#03441:4 Values whose Sum is 0
from itertools import product

n = int(input())
a = []
b = []
c = []
d = []

for _ in range(n):
    i, j, k, l = map(int, input().split())
    a.append(i)
    b.append(j)
    c.append(k)
    d.append(l)
left = sorted(list(map(sum, product(a, b))))
right = sorted(list(map(lambda x: -sum(x), product(c, d))))

res = 0
lpointer = len(left) - 1
rpointer = len(right) - 1
same_flag = 0

while lpointer >= 0 and rpointer >= 0:
    if rpointer - same_flag < 0:
        if same_flag != 0:
            same_flag = 0
        lpointer -= 1
        continue
    if right[rpointer - same_flag] > left[lpointer]:
        rpointer -= 1
        continue
    if right[rpointer - same_flag] < left[lpointer]:
        if same_flag != 0:
            same_flag = 0
        lpointer -= 1
        continue
    if right[rpointer - same_flag] == left[lpointer]:
        same_flag += 1
        res += 1

print(res)
