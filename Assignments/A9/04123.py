#04123:马走日
directions = [(1, 2), (2, 1), (1, -2), (2, -1), (-1, 2), (-2, 1), (-1, -2), (-2, -1)]
def dfs(n, m, x, y, traversed):
    if len(traversed) == n * m:
        return 1
    res = 0
    for dx, dy in directions:
        xx, yy = x + dx, y + dy
        if (xx, yy) in traversed or xx < 0 or xx >= n or yy < 0 or yy >= m:
            continue
        else:
            res += dfs(n, m, xx, yy, traversed + [(xx, yy)])
    return res

l = int(input())
for _ in range(l):
    n, m, x, y = map(int, input().split())
    print(dfs(n, m, x, y, [(x, y)]))
