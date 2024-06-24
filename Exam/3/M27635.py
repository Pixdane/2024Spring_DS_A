# M27635:判断无向图是否连通有无回路
from collections import deque

n, m = map(int, input().split())
vertices = list(range(n))
connectivity = {i: [] for i in vertices}
for _ in range(m):
    u, v = map(int, input().split())
    connectivity[u].append(v)
    connectivity[v].append(u)

def dfs(vertex, traversed=None, father=None):
    loop = 0
    if traversed == None:
        traversed = []
    res = [vertex]
    traversed.append(vertex)
    for ad in connectivity[vertex]:
        if ad not in traversed:
            r = dfs(ad, traversed, vertex)
            res += r[0]
            loop = loop or r[1]
        elif ad != father:
            loop = 1
    return res, loop

l = 0
c = 1
for i in vertices:
    d = dfs(i)
    if d[1] == 1:
        l = 1
    if len(d[0]) < n:
        c = 0
# print(f'connected:{'yes' if c else 'no'}')
# print(f'loop:{'yes' if l else 'no'}')
if c:
    print('connected:yes')
else:
    print('connected:no')
if l:
    print('loop:yes')
else:
    print('loop:no')
