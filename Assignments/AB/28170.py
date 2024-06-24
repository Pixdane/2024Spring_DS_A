# 28170:算鹰
from itertools import product
WIDTH = 10
DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
board = [[1 if x == '.' else 0 for x in input()] for _ in range(WIDTH)]
traversed = [[0] * WIDTH for _ in range(WIDTH)]


def is_out_of_bound(point):
    x, y = point
    return x < 0 or x >= WIDTH or y < 0 or y >= WIDTH


def dfs(point):
    x, y = point
    if traversed[x][y]:
        return
    traversed[x][y] = 1
    for dx, dy in DIRECTIONS:
        new_point = (x + dx, y + dy)
        if not is_out_of_bound(new_point) and board[x][y]:
            dfs(new_point)


res = 0
for pointin in product(range(WIDTH), range(WIDTH)):
    xin, yin = pointin
    if not traversed[xin][yin] and board[xin][yin]:
        res += 1
        dfs(pointin)
print(res)
