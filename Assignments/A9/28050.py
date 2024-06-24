#28050:骑士周游
directions = [(1, 2), (2, 1), (1, -2), (2, -1), (-1, 2), (-2, 1), (-1, -2), (-2, -1)]
def dfs(n, x, y, traversed):
    if n % 2 == 1:
        return True
    if len(traversed) == n ** 2:
        return True
    for dx, dy in directions:
        xx, yy = x + dx, y + dy
        if (xx, yy) in traversed or xx < 0 or xx >= n or yy < 0 or yy >= n:
            continue
        if dfs(n, xx, yy, traversed + [(xx, yy)]):
            return True
    return False

n = int(input())
x, y = map(int, input().split())
print("success" if dfs(n, x, y, [(x, y)]) else "fail")
